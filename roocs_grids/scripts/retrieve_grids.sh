#!/bin/bash
#
#
####################################################################################
#
# Short script to download the reference target grids used by the roocs regridder
# 
# Downloads CMIP6 reference grids provided by 
#  Charles Zender via a http download server and
#  ATLAS reference grids from the github repo SantanderMetGroup/ATLAS.
#
####################################################################################



# Download function
download () {
    TargetPath=$1
    Link=$2
    FileArr=( ${@:3} )

    [[ ! -d "$TargetPath" ]] && { echo "Error: the target directory '$TargetPath' does not exist!" && exit 1 ; }
    echo "... target directory '$TargetPath'..."

    for file in ${FileArr[@]}
    do
        if [[ ! -e "$TargetPath/$file" ]]
        then
            curl $Link/$file -sSf -L -o $TargetPath/$file && echo "... '$file' retrieved successfully." || echo "Error: Grid '$file' could not be retrieved!"
        else
            echo "... '$file' already exists. Skipping download."
        fi
    done
    echo "... done."
}



# Specify target directory
ScriptPath=$( readlink -f $0 )
targetpath=$( dirname $ScriptPath )/../grids/


# Retrieve grids from the ATLAS repository

ATLASLink=https://raw.githubusercontent.com/SantanderMetGroup/ATLAS/master/reference-grids/
declare -a ATLASGrids
ATLASGrids+=( land_sea_mask_1degree.nc4 )
ATLASGrids+=( land_sea_mask_2degree.nc4 )
ATLASGrids+=( land_sea_mask_025degree_ERA5.nc )
ATLASGrids+=( land_sea_mask_05degree.nc4 )
ATLASGrids+=( land_sea_mask_025degree_binary.nc4 )
ATLASGrids+=( land_sea_mask_1degree_binary.nc4 )
ATLASGrids+=( land_sea_mask_2degree_binary.nc4 )
#ATLASGrids+=( mountain_ranges_mask_025degree.nc4 )
#ATLASGrids+=( mountain_ranges_mask_05degree.nc4 )
#ATLASGrids+=( mountain_ranges_mask_1degree.nc4 )
#ATLASGrids+=( mountain_ranges_mask_2degree.nc4 )
#ATLASGrids+=(  )



echo "Downloading ATLAS reference-grids from '$ATLASLink'..."
download $targetpath $ATLASLink ${ATLASGrids[@]}



# Retrieve CMIP6 target grids provided by Charles Zender

CMIP6Link=http://dust.ess.uci.edu/grids/
declare -a CMIP6Grids
CMIP6Grids+=( cmip6_72x144_scrip.20181001.nc )
CMIP6Grids+=( cmip6_145x288_scrip.20181001.nc )
CMIP6Grids+=( cmip6_180x360_scrip.20181001.nc )
CMIP6Grids+=( cmip6_241x480_scrip.20181001.nc )
CMIP6Grids+=( cmip6_361x576_scrip.20181001.nc )
CMIP6Grids+=( cmip6_720x1440_scrip.20181001.nc )
CMIP6Grids+=( cmip6_721x1440_scrip.20181001.nc )
#CMIP6Grids+=(  )

echo -e "\nDownloading CMIP6 reference grids from '$CMIP6Link'..." 
download $targetpath $CMIP6Link ${CMIP6Grids[@]}



exit 0
