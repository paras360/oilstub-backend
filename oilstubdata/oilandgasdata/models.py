from uuid import uuid4

from django.db import models


class TrackModel(models.Model):
    uuid = models.UUIDField(db_index=True, primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class OgCountyLeaseCycle(TrackModel):
    oil_gas_code = models.CharField(max_length=20)
    district_no = models.CharField(max_length=20)
    lease_no = models.CharField(max_length=20)
    cycle_year = models.CharField(max_length=20)
    cycle_month = models.CharField(max_length=20)
    county_no = models.CharField(max_length=20)
    operator_no = models.CharField(max_length=20)
    field_no = models.CharField(max_length=20)
    cycle_year_month = models.CharField(max_length=20)
    field_type = models.CharField(max_length=50)
    gas_well_no = models.CharField(max_length=20)
    prod_report_field_flag = models.CharField(max_length=50)
    cnty_lse_oil_prod_vol = models.IntegerField
    cnty_lse_oil_allow = models.CharField(max_length=20)
    cnty_lse_oil_ending_bal = models.CharField(max_length=20)
    cnty_lse_gas_prod_vol = models.CharField(max_length=20)
    cnty_lse_gas_allow = models.CharField(max_length=20)
    cnty_lse_gas_lift_inj_vol = models.CharField(max_length=20)
    cnty_lse_cond_prod_vol = models.CharField(max_length=20)
    cnty_lse_cond_limit = models.CharField(max_length=20)
    cnty_lse_cond_ending_bal = models.CharField(max_length=20)
    cnty_lse_csgd_prod_vol = models.CharField(max_length=20)
    cnty_lse_csgd_limit = models.CharField(max_length=20)
    cnty_lse_csgd_gas_lift = models.CharField(max_length=20)
    cnty_lse_oil_tot_disp = models.CharField(max_length=20)
    cnty_lse_gas_tot_disp = models.CharField(max_length=20)
    cnty_lse_cond_tot_disp = models.CharField(max_length=20)
    cnty_lse_csgd_tot_disp = models.CharField(max_length=20)
    district_name = models.CharField(max_length=50)
    lease_name = models.CharField(max_length=50)
    operator_name = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)
    county_name = models.CharField(max_length=50)


class GpCountyData(TrackModel):
    county_no = models.CharField(max_length=20)
    district_name = models.CharField(max_length=50)
    county_name = models.CharField(max_length=50)
    county_fips_code = models.CharField(max_length=20)
    district_no = models.CharField(max_length=50)
    on_shore_flag = models.CharField(max_length=20)
    onshore_assc_cnty_flag = models.CharField(max_length=20)


class GpDateRangeCycleData(TrackModel):
    oldest_prod_cycle_year_month = models.CharField(max_length=20)
    newest_prod_cycle_year_month = models.CharField(max_length=20)
    newest_sched_cycle_year_month = models.CharField(max_length=20)
    gas_extract_date = models.CharField(max_length=50)
    oil_extract_date = models.CharField(max_length=50)


class GpDistrictData(TrackModel):
    district_no = models.CharField(max_length=50)
    district_name = models.CharField(max_length=50)
    office_phone_no = models.CharField(max_length=20)
    office_location = models.CharField(max_length=50)


class OgCountyCycleData(TrackModel):
    county_no = models.CharField(max_length=20)
    district_no = models.CharField(max_length=50)
    district_name = models.CharField(max_length=50)
    cycle_year = models.CharField(max_length=20)
    cycle_month = models.CharField(max_length=20)
    cycle_year_month = models.CharField(max_length=20)
    cnty_oil_prod_vol = models.IntegerField()
    cnty_oil_allow = models.CharField(max_length=20)
    cnty_oil_ending_bal = models.CharField(max_length=20)
    cnty_gas_prod_vol = models.CharField(max_length=20)
    cnty_gas_allow = models.CharField(max_length=20)
    cnty_gas_lift_inj_vol = models.CharField(max_length=20)
    cnty_cond_prod_vol = models.CharField(max_length=20)
    cnty_cond_limit = models.CharField(max_length=20)
    cnty_cond_ending_bal = models.CharField(max_length=20)
    cnty_csgd_prod_vol = models.CharField(max_length=20)
    cnty_csgd_limit = models.CharField(max_length=20)
    cnty_csgd_gas_lift = models.CharField(max_length=20)
    cnty_oil_tot_disp = models.CharField(max_length=20)
    cnty_gas_tot_disp = models.CharField(max_length=20)
    cnty_cond_tot_disp = models.CharField(max_length=20)
    cnty_csgd_tot_disp = models.CharField(max_length=20)
    county_name = models.CharField(max_length=50)
    oil_gas_code = models.CharField(max_length=20)


class OgDistrictCycleData(TrackModel):
    district_no = models.CharField(max_length=50)
    district_name = models.CharField(max_length=50)
    cycle_year = models.CharField(max_length=20)
    cycle_month = models.CharField(max_length=20)
    cycle_year_month = models.CharField(max_length=20)
    dist_oil_prod_vol = models.CharField(max_length=20)
    dist_gas_prod_vol = models.CharField(max_length=20)
    dist_cond_prod_vol = models.CharField(max_length=20)
    dist_csgd_prod_vol = models.CharField(max_length=20)


class OgFieldCycleData(TrackModel):
    field_no = models.CharField(max_length=20)
    field_name = models.CharField(max_length=50)
    district_no = models.CharField(max_length=50)
    district_name = models.CharField(max_length=50)
    cycle_year = models.CharField(max_length=20)
    cycle_month = models.CharField(max_length=20)
    cycle_year_month = models.CharField(max_length=20)
    field_oil_prod_vol = models.CharField(max_length=20)
    field_gas_prod_vol = models.CharField(max_length=20)
    field_cond_prod_vol = models.CharField(max_length=20)
    field_csgd_prod_vol = models.CharField(max_length=20)


class OgFieldDwData(TrackModel):
    field_no = models.CharField(max_length=20)
    field_name = models.CharField(max_length=50)
    district_no = models.CharField(max_length=50)
    district_name = models.CharField(max_length=50)
    field_class = models.CharField(max_length=50)
    field_h2s_flag = models.CharField(max_length=50)
    field_manual_rev_flag = models.CharField(max_length=50)
    wildcat_flag = models.CharField(max_length=50)
    o_derived_rule_type_code = models.CharField(max_length=50)
    g_derived_rule_type_code = models.CharField(max_length=50)
    o_rescind_dt = models.CharField(max_length=50)
    g_rescind_dt = models.CharField(max_length=50)
    o_salt_dome_flag = models.CharField(max_length=50)
    g_salt_dome_flag = models.CharField(max_length=50)
    o_offshore_code = models.CharField(max_length=50)
    g_offshore_code = models.CharField(max_length=50)
    o_dont_permit = models.CharField(max_length=50)
    g_dont_permit = models.CharField(max_length=50)
    o_noa_man_rev_rule = models.CharField(max_length=50)
    g_noa_man_rev_rule = models.CharField(max_length=50)
    o_county_no = models.CharField(max_length=50)
    g_county_no = models.CharField(max_length=50)
    o_discovery_dt = models.CharField(max_length=50)
    g_discovery_dt = models.CharField(max_length=50)
    o_sched_remarks = models.CharField(max_length=50)
    g_sched_remarks = models.CharField(max_length=50)
    o_comments = models.CharField(max_length=50)
    g_comments = models.CharField(max_length=50)
    create_by = models.CharField(max_length=50)
    create_dt = models.CharField(max_length=120)
    modify_by = models.CharField(max_length=50)
    modify_dt = models.CharField(max_length=120)


class OgLeaseCycleData(TrackModel):
    oil_gas_code = models.CharField(max_length=20)
    district_no = models.CharField(max_length=50)
    lease_no = models.CharField(max_length=50)
    operator_no = models.CharField(max_length=50)
    field_no = models.CharField(max_length=50)
    cycle_year_month_min = models.CharField(max_length=50)
    cycle_year_month_max = models.CharField(max_length=50)
    district_name = models.CharField(max_length=50)
    lease_name = models.CharField(max_length=50)
    operator_name = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)


class OgLeaseCycleDispData(TrackModel):
    oil_gas_code = models.CharField(max_length=20)
    district_no = models.CharField(max_length=50)
    lease_no = models.CharField(max_length=50)
    operator_no = models.CharField(max_length=50)
    field_no = models.CharField(max_length=50)
    cycle_year = models.CharField(max_length=50)
    cycle_month = models.CharField(max_length=50)
    cycle_year_month = models.CharField(max_length=50)
    lease_oil_dispcd00_vol = models.CharField(max_length=128)
    lease_oil_dispcd01_vol = models.CharField(max_length=128)
    lease_oil_dispcd02_vol = models.CharField(max_length=128)
    lease_oil_dispcd03_vol = models.CharField(max_length=128)
    lease_oil_dispcd04_vol = models.CharField(max_length=128)
    lease_oil_dispcd05_vol = models.CharField(max_length=128)
    lease_oil_dispcd06_vol = models.CharField(max_length=128)
    lease_oil_dispcd07_vol = models.CharField(max_length=128)
    lease_oil_dispcd09_vol = models.CharField(max_length=128)
    lease_oil_dispcd09_vol = models.CharField(max_length=128)
    lease_oil_dispcd99_vol = models.CharField(max_length=128)
    lease_gas_dispcd01_vol = models.CharField(max_length=128)
    lease_gas_dispcd02_vol = models.CharField(max_length=128)
    lease_gas_dispcd03_vol = models.CharField(max_length=128)
    lease_gas_dispcd04_vol = models.CharField(max_length=128)
    lease_gas_dispcd05_vol = models.CharField(max_length=128)
    lease_gas_dispcd06_vol = models.CharField(max_length=128)
    lease_gas_dispcd07_vol = models.CharField(max_length=128)
    lease_gas_dispcd08_vol = models.CharField(max_length=128)
    lease_gas_dispcd09_vol = models.CharField(max_length=128)
    lease_gas_dispcd99_vol = models.CharField(max_length=128)
    lease_cond_dispcd00_vol = models.CharField(max_length=128)
    lease_cond_dispcd01_vol = models.CharField(max_length=128)
    lease_cond_dispcd02_vol = models.CharField(max_length=128)
    lease_cond_dispcd03_vol = models.CharField(max_length=128)
    lease_cond_dispcd04_vol = models.CharField(max_length=128)
    lease_cond_dispcd05_vol = models.CharField(max_length=128)
    lease_cond_dispcd06_vol = models.CharField(max_length=128)
    lease_cond_dispcd07_vol = models.CharField(max_length=128)
    lease_cond_dispcd08_vol = models.CharField(max_length=128)
    lease_cond_dispcd09_vol = models.CharField(max_length=128)
    lease_cond_dispcd99_vol = models.CharField(max_length=128)
    lease_csgd_dispcd01_vol = models.CharField(max_length=128)
    lease_csgd_dispcd02_vol = models.CharField(max_length=128)
    lease_csgd_dispcd03_vol = models.CharField(max_length=128)
    lease_csgd_dispcd04_vol = models.CharField(max_length=128)
    lease_csgd_dispcd05_vol = models.CharField(max_length=128)
    lease_csgd_dispcd06_vol = models.CharField(max_length=128)
    lease_csgd_dispcd07_vol = models.CharField(max_length=128)
    lease_csgd_dispcd08_vol = models.CharField(max_length=128)
    lease_csgd_dispcd09_vol = models.CharField(max_length=128)
    lease_csgd_dispcd99_vol = models.CharField(max_length=128)
    district_name = models.CharField(max_length=50)
    lease_name = models.CharField(max_length=50)
    operator_name = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)


class OgOperatorCycleData(TrackModel):
    operator_no = models.CharField(max_length=50)
    cycle_year = models.CharField(max_length=50)
    cycle_month = models.CharField(max_length=50)
    cycle_year_month = models.CharField(max_length=50)
    operator_name = models.CharField(max_length=50)
    oper_oil_prod_vol = models.CharField(max_length=50)
    oper_gas_prod_vol = models.CharField(max_length=50)
    oper_cond_prod_vol = models.CharField(max_length=50)
    oper_csgd_prod_vol = models.CharField(max_length=50)


class OgOperatorDwData(TrackModel):
    operator_no = models.CharField(max_length=50)
    operator_name = models.CharField(max_length=50)
    p5_status_code = models.CharField(max_length=50)
    p5_last_field_dt = models.CharField(max_length=50)
    operator_tax_cert_flag = models.CharField(max_length=50)
    operator_sb639_flag = models.CharField(max_length=50)
    fa_option_code = models.CharField(max_length=50)
    record_status_code = models.CharField(max_length=50)
    efile_status_code = models.CharField(max_length=50)
    efile_effective_dt = models.CharField(max_length=50)
    create_by = models.CharField(max_length=50)
    create_dt = models.CharField(max_length=120)
    modify_by = models.CharField(max_length=50)
    modify_dt = models.CharField(max_length=120)


class OgRegulatorLeaseDwData(TrackModel):
    oil_gas_code = models.CharField(max_length=20)
    district_no = models.CharField(max_length=50)
    lease_no = models.CharField(max_length=50)
    operator_no = models.CharField(max_length=50)
    field_no = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)
    district_name = models.CharField(max_length=50)
    lease_name = models.CharField(max_length=50)
    operator_name = models.CharField(max_length=50)
    well_no = models.CharField(max_length=50)
    lease_off_sched_flag = models.CharField(max_length=50)
    lease_severance_flag = models.CharField(max_length=50)


class OgSummaryMasterLargeData(TrackModel):
    oil_gas_code = models.CharField(max_length=20)
    district_no = models.CharField(max_length=50)
    lease_no = models.CharField(max_length=50)
    operator_no = models.CharField(max_length=50)
    field_no = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)
    district_name = models.CharField(max_length=50)
    lease_name = models.CharField(max_length=50)
    operator_name = models.CharField(max_length=50)
    cycle_year_month_min = models.CharField(max_length=50)
    cycle_year_month_max = models.CharField(max_length=50)


class OgSummaryOnShoreLeaseData(TrackModel):
    oil_gas_code = models.CharField(max_length=20)
    district_no = models.CharField(max_length=50)
    lease_no = models.CharField(max_length=50)
    operator_no = models.CharField(max_length=50)
    field_no = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)
    district_name = models.CharField(max_length=50)
    lease_name = models.CharField(max_length=50)
    operator_name = models.CharField(max_length=50)
    cycle_year_month_min = models.CharField(max_length=50)
    cycle_year_month_max = models.CharField(max_length=50)


class OgWellCompletionData(TrackModel):
    oil_gas_code = models.CharField(max_length=20)
    district_no = models.CharField(max_length=50)
    lease_no = models.CharField(max_length=50)
    well_no = models.CharField(max_length=50)
    district_name = models.CharField(max_length=50)
    county_name = models.CharField(max_length=50)
    api_county_code = models.CharField(max_length=50)
    api_unique_no = models.CharField(max_length=50)
    onshore_assc_cnty = models.CharField(max_length=50)
    oil_well_unit_no = models.CharField(max_length=50)
    well_root_no = models.CharField(max_length=50)
    wellbore_shutin_dt = models.CharField(max_length=50)
    well_shutin_dt = models.CharField(max_length=50)
    well_14b2_status_code = models.CharField(max_length=50)
    well_subject_14b2_flag = models.CharField(max_length=50)
    wellbore_location_code = models.CharField(max_length=50)
