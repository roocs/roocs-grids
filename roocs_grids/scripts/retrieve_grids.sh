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
        filebase=$( basename $file )
        if [[ ! -e "$TargetPath/$filebase" ]]
        then
            curl $Link/$file -sSf -L -o $TargetPath/$filebase && echo "... '$filebase' retrieved successfully." || echo "Error: Grid '$filebase' could not be retrieved!"
        else
            echo "... '$filebase' already exists. Skipping download."
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



# Retrieve target grids from ESGF as submitted to CMIP6

ESGFLink=http://
declare -a ESGFGrids
ESGFGrids+=( esgf-data3.ceda.ac.uk/thredds/fileServer/esg_cmip6/CMIP6/HighResMIP/MPI-M/MPI-ESM1-2-XR/highresSST-present/r1i1p1f1/Amon/sfcWind/gn/v20190923/sfcWind_Amon_MPI-ESM1-2-XR_highresSST-present_r1i1p1f1_gn_195001-195012.nc )
ESGFGrids+=( esgf3.dkrz.de/thredds/fileServer/cmip6/CMIP/MPI-M/MPI-ESM1-2-LR/1pctCO2/r1i1p1f1/fx/areacella/gn/v20190710/areacella_fx_MPI-ESM1-2-LR_1pctCO2_r1i1p1f1_gn.nc
)
ESGFGrids+=( esgf3.dkrz.de/thredds/fileServer/cmip6/CMIP/MPI-M/MPI-ESM1-2-LR/1pctCO2/r1i1p1f1/fx/sftlf/gn/v20190710/sftlf_fx_MPI-ESM1-2-LR_1pctCO2_r1i1p1f1_gn.nc )
ESGFGrids+=( esgf3.dkrz.de/thredds/fileServer/cmip6/ScenarioMIP/DKRZ/MPI-ESM1-2-HR/ssp370/r3i1p1f1/fx/sftlf/gn/v20190710/sftlf_fx_MPI-ESM1-2-HR_ssp370_r3i1p1f1_gn.nc )
ESGFGrids+=( esgf3.dkrz.de/thredds/fileServer/cmip6/ScenarioMIP/DKRZ/MPI-ESM1-2-HR/ssp245/r1i1p1f1/fx/areacella/gn/v20190710/areacella_fx_MPI-ESM1-2-HR_ssp245_r1i1p1f1_gn.nc )

echo -e "\nDownloading ESGF target grids from '$ESGFLink'..."
download $targetpath $ESGFLink ${ESGFGrids[@]}



# Apply fixes
echo -e "\nApplying fixes to the netCDF files..."
for nc in  ${CMIP6Grids[@]} ${ATLASGrids[@]}; do
    # 1 # Takes too long for big grids
    #ncdump $targetpath/$nc > $targetpath/${nc}.cdl
    # Find and replace "since NA" with "2001-01-01 00:00:00" in CDL version of file
    #grep -q "since NA" $targetpath/${nc}.cdl && {
    #  echo "  fixing time@units for $targetpath/${nc}..."
    #  perl -p -i -w -e 's/since NA/since 2001-01-01 00:00:00/g;' $targetpath/${nc}.cdl
    #  ncgen -o $targetpath/$nc $targetpath/${nc}.cdl && echo "  ...successful." || echo "  ...failed!"
    #}
    #rm -f $targetpath/${nc}.cdl
    # 2 #
    ncdump -h $targetpath/$nc | grep -q "days since NA" && {
        ncatted -O -a units,time,m,c,"days since 2001-01-01 00:00:00" $targetpath/$nc && echo "  ...successful for '$nc'." ||  echo "  ...failed for '$nc'!"
    }
done
echo -e "...done!"



# Post Process ESGF Files
echo -e "\nPost-processing ESGF files..."

# Extract and merge variables
[[ ! -e $targetpath/grid_T255.nc ]] && {
    mv $targetpath/sfcWind_Amon_MPI-ESM1-2-XR_highresSST-present_r1i1p1f1_gn_195001-195012.nc $targetpath/grid_T255.nc
    ncks -O -h -x -v sfcWind,time,time_bnds $targetpath/grid_T255.nc $targetpath/grid_T255.nc > /dev/null
    nccopy -d 9 -s $targetpath/grid_T255.nc $targetpath/grid_T255_def.nc
    mv $targetpath/grid_T255_def.nc $targetpath/grid_T255.nc
}
[[ ! -e $targetpath/grid_T127_lsm_binary.nc ]] && {
    mv $targetpath/sftlf_fx_MPI-ESM1-2-HR_ssp370_r3i1p1f1_gn.nc $targetpath/grid_T127_lsm_binary.nc
    ncks -A -h -v areacella $targetpath/areacella_fx_MPI-ESM1-2-HR_ssp245_r1i1p1f1_gn.nc $targetpath/grid_T127_lsm_binary.nc
    nccopy -d 9 -s $targetpath/grid_T127_lsm_binary.nc $targetpath/grid_T127_lsm_binary_def.nc
    mv $targetpath/grid_T127_lsm_binary_def.nc $targetpath/grid_T127_lsm_binary.nc
}
[[ ! -e $targetpath/grid_T63_lsm_binary.nc ]] && {
    mv $targetpath/sftlf_fx_MPI-ESM1-2-LR_1pctCO2_r1i1p1f1_gn.nc $targetpath/grid_T63_lsm_binary.nc
    ncks -A -h -v areacella $targetpath/areacella_fx_MPI-ESM1-2-LR_1pctCO2_r1i1p1f1_gn.nc $targetpath/grid_T63_lsm_binary.nc
    nccopy -d 9 -s $targetpath/grid_T63_lsm_binary.nc $targetpath/grid_T63_lsm_binary_def.nc
    mv $targetpath/grid_T63_lsm_binary_def.nc $targetpath/grid_T63_lsm_binary.nc
}

# Clean up
rm -f $targetpath/areacella_fx_MPI-ESM1-2-HR_ssp245_r1i1p1f1_gn.nc $targetpath/areacella_fx_MPI-ESM1-2-LR_1pctCO2_r1i1p1f1_gn.nc $targetpath/sfcWind_Amon_MPI-ESM1-2-XR_highresSST-present_r1i1p1f1_gn_195001-195012.nc $targetpath/sftlf_fx_MPI-ESM1-2-HR_ssp370_r3i1p1f1_gn.nc $targetpath/sftlf_fx_MPI-ESM1-2-LR_1pctCO2_r1i1p1f1_gn.nc

# Remove unnecessary attributes
atts=(description nco_openmp_thread_number NCO history_of_appended_files activity_id realm branch_method branch_time_in_child branch_time_in_parent contact creation_date experiment experiment_id external_variables forcing_index frequency further_info_url history initialization_index institution institution_id mip_era activity_id parent_activity_id parent_experiment_id parent_mip_era parent_source_id parent_time_units parent_variant_label physics_index product project_id realization_index references source data_specs_version source_id source_type sub_experiment_id sub_experiment table_id table_info title variable_id variant_label license cmor_version tracking_id)
vatts=(history original_name original_units comment)

for ifile in grid_T127_lsm_binary.nc grid_T63_lsm_binary.nc grid_T255.nc
do
    for att in ${atts[@]}; do
        ncatted -O -h -a $att,global,d,, $targetpath/$ifile
    done
    if [[ "$ifile" != *"T255"* ]]; then
        for vatt in ${vatts[@]}; do
            ncatted -O -h -a $vatt,sftlf,d,, $targetpath/$ifile
            ncatted -O -h -a $vatt,areacella,d,, $targetpath/$ifile
        done
    fi
done
echo -e "...done!"



exit 0
