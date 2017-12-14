import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as pg

METADATA = sa.MetaData()

DATA_INGEST__CENSUS__ZIP_BUSINESS_PATTERNS = sa.Table(
    'census__zip_business_patterns', METADATA,
    sa.Column('st', sa.Text),
    sa.Column('zipcode', sa.Text),
    sa.Column('geo_id', sa.Text),
    sa.Column('geo_ttl', sa.Text),
    sa.Column('footid_geo', sa.Numeric),
    sa.Column('naics2012', sa.Text),
    sa.Column('naics2012_ttl', sa.Text),
    sa.Column('footid_naics', sa.Numeric),
    sa.Column('year', sa.Text),
    sa.Column('empszes', sa.Text),
    sa.Column('empszes_ttl', sa.Text),
    sa.Column('estab', sa.Text),
    sa.Column('estab_f', sa.Numeric),
    schema='data_ingest')


DATA_INGEST__IRS__ZIP_DATA = sa.Table(
    'irs__zip_data', METADATA,
    sa.Column('state_fips', sa.BigInteger),
    sa.Column('state', sa.Text),
    sa.Column('zipcode', sa.BigInteger),
    sa.Column('agi_stub', sa.BigInteger),
    sa.Column('n1', sa.Numeric),
    sa.Column('mars1', sa.Numeric),
    sa.Column('mars2', sa.Numeric),
    sa.Column('mars4', sa.Numeric),
    sa.Column('prep', sa.Numeric),
    sa.Column('n2', sa.Numeric),
    sa.Column('numdep', sa.Numeric),
    sa.Column('total_vita', sa.Numeric),
    sa.Column('vita', sa.Numeric),
    sa.Column('tce', sa.Numeric),
    sa.Column('a00100', sa.Numeric),
    sa.Column('n02650', sa.Numeric),
    sa.Column('a02650', sa.Numeric),
    sa.Column('n00200', sa.Numeric),
    sa.Column('a00200', sa.Numeric),
    sa.Column('n00300', sa.Numeric),
    sa.Column('a00300', sa.Numeric),
    sa.Column('n00600', sa.Numeric),
    sa.Column('a00600', sa.Numeric),
    sa.Column('n00650', sa.Numeric),
    sa.Column('a00650', sa.Numeric),
    sa.Column('n00700', sa.Numeric),
    sa.Column('a00700', sa.Numeric),
    sa.Column('n00900', sa.Numeric),
    sa.Column('a00900', sa.Numeric),
    sa.Column('n01000', sa.Numeric),
    sa.Column('a01000', sa.Numeric),
    sa.Column('n01400', sa.Numeric),
    sa.Column('a01400', sa.Numeric),
    sa.Column('n01700', sa.Numeric),
    sa.Column('a01700', sa.Numeric),
    sa.Column('schf', sa.Numeric),
    sa.Column('n02300', sa.Numeric),
    sa.Column('a02300', sa.Numeric),
    sa.Column('n02500', sa.Numeric),
    sa.Column('a02500', sa.Numeric),
    sa.Column('n26270', sa.Numeric),
    sa.Column('a26270', sa.Numeric),
    sa.Column('n02900', sa.Numeric),
    sa.Column('a02900', sa.Numeric),
    sa.Column('n03220', sa.Numeric),
    sa.Column('a03220', sa.Numeric),
    sa.Column('n03300', sa.Numeric),
    sa.Column('a03300', sa.Numeric),
    sa.Column('n03270', sa.Numeric),
    sa.Column('a03270', sa.Numeric),
    sa.Column('n03150', sa.Numeric),
    sa.Column('a03150', sa.Numeric),
    sa.Column('n03210', sa.Numeric),
    sa.Column('a03210', sa.Numeric),
    sa.Column('n03230', sa.Numeric),
    sa.Column('a03230', sa.Numeric),
    sa.Column('n03240', sa.Numeric),
    sa.Column('a03240', sa.Numeric),
    sa.Column('n04470', sa.Numeric),
    sa.Column('a04470', sa.Numeric),
    sa.Column('a00101', sa.Numeric),
    sa.Column('n18425', sa.Numeric),
    sa.Column('a18425', sa.Numeric),
    sa.Column('n18450', sa.Numeric),
    sa.Column('a18450', sa.Numeric),
    sa.Column('n18500', sa.Numeric),
    sa.Column('a18500', sa.Numeric),
    sa.Column('n18300', sa.Numeric),
    sa.Column('a18300', sa.Numeric),
    sa.Column('n19300', sa.Numeric),
    sa.Column('a19300', sa.Numeric),
    sa.Column('n19700', sa.Numeric),
    sa.Column('a19700', sa.Numeric),
    sa.Column('n04800', sa.Numeric),
    sa.Column('a04800', sa.Numeric),
    sa.Column('n05800', sa.Numeric),
    sa.Column('a05800', sa.Numeric),
    sa.Column('n09600', sa.Numeric),
    sa.Column('a09600', sa.Numeric),
    sa.Column('n05780', sa.Numeric),
    sa.Column('a05780', sa.Numeric),
    sa.Column('n07100', sa.Numeric),
    sa.Column('a07100', sa.Numeric),
    sa.Column('n07300', sa.Numeric),
    sa.Column('a07300', sa.Numeric),
    sa.Column('n07180', sa.Numeric),
    sa.Column('a07180', sa.Numeric),
    sa.Column('n07230', sa.Numeric),
    sa.Column('a07230', sa.Numeric),
    sa.Column('n07240', sa.Numeric),
    sa.Column('a07240', sa.Numeric),
    sa.Column('n07220', sa.Numeric),
    sa.Column('a07220', sa.Numeric),
    sa.Column('n07260', sa.Numeric),
    sa.Column('a07260', sa.Numeric),
    sa.Column('n09400', sa.Numeric),
    sa.Column('a09400', sa.Numeric),
    sa.Column('n85770', sa.Numeric),
    sa.Column('a85770', sa.Numeric),
    sa.Column('n85775', sa.Numeric),
    sa.Column('a85775', sa.Numeric),
    sa.Column('n09750', sa.Numeric),
    sa.Column('a09750', sa.Numeric),
    sa.Column('n10600', sa.Numeric),
    sa.Column('a10600', sa.Numeric),
    sa.Column('n59660', sa.Numeric),
    sa.Column('a59660', sa.Numeric),
    sa.Column('n59720', sa.Numeric),
    sa.Column('a59720', sa.Numeric),
    sa.Column('n11070', sa.Numeric),
    sa.Column('a11070', sa.Numeric),
    sa.Column('n10960', sa.Numeric),
    sa.Column('a10960', sa.Numeric),
    sa.Column('n11560', sa.Numeric),
    sa.Column('a11560', sa.Numeric),
    sa.Column('n06500', sa.Numeric),
    sa.Column('a06500', sa.Numeric),
    sa.Column('n10300', sa.Numeric),
    sa.Column('a10300', sa.Numeric),
    sa.Column('n85530', sa.Numeric),
    sa.Column('a85530', sa.Numeric),
    sa.Column('n85300', sa.Numeric),
    sa.Column('a85300', sa.Numeric),
    sa.Column('n11901', sa.Numeric),
    sa.Column('a11901', sa.Numeric),
    sa.Column('n11902', sa.Numeric),
    sa.Column('a11902', sa.Numeric),
    schema='data_ingest')


DATA_INGEST__SBA__FOIA_504_1991_PRESENT = sa.Table(
    'sba__foia_504_1991_present', METADATA,
    sa.Column('program', sa.Text),
    sa.Column('borr_name', sa.Text),
    sa.Column('borr_street', sa.Text),
    sa.Column('borr_city', sa.Text),
    sa.Column('borr_state', sa.Text),
    sa.Column('borr_zip', sa.Text),
    sa.Column('cdc_name', sa.Text),
    sa.Column('cdc_street', sa.Text),
    sa.Column('cdc_city', sa.Text),
    sa.Column('cdc_state', sa.Text),
    sa.Column('cdc_zip', sa.Text),
    sa.Column('third_party_lender_name', sa.Text),
    sa.Column('third_party_lender_city', sa.Text),
    sa.Column('third_party_lender_state', sa.Text),
    sa.Column('third_party_dollars', sa.Numeric),
    sa.Column('gross_approval', sa.BigInteger),
    sa.Column('approval_date', sa.DateTime),
    sa.Column('approval_fiscal_year', sa.BigInteger),
    sa.Column('first_disbursement_date', sa.DateTime),
    sa.Column('delivery_method', sa.Text),
    sa.Column('subprogram_description', sa.Text),
    sa.Column('initial_interest_rate', sa.Numeric),
    sa.Column('term_in_months', sa.BigInteger),
    sa.Column('naics_code', sa.Numeric),
    sa.Column('naics_description', sa.Text),
    sa.Column('franchise_code', sa.Text),
    sa.Column('franchise_name', sa.Text),
    sa.Column('project_county', sa.Text),
    sa.Column('project_state', sa.Text),
    sa.Column('sba_district_office', sa.Text),
    sa.Column('congressional_district', sa.Numeric),
    sa.Column('business_type', sa.Text),
    sa.Column('loan_status', sa.Text),
    sa.Column('chargeoff_date', sa.Date),
    sa.Column('gross_chargeoff_amount', sa.BigInteger),
    sa.Column('jobs_supported', sa.BigInteger),
    schema='data_ingest')


DATA_INGEST__SBA__FOIA_7A_1991_1999 = sa.Table(
    'sba__foia_7a_1991_1999', METADATA,
    sa.Column('program', sa.Text),
    sa.Column('borr_name', sa.Text),
    sa.Column('borr_street', sa.Text),
    sa.Column('borr_city', sa.Text),
    sa.Column('borr_state', sa.Text),
    sa.Column('borr_zip', sa.Text),
    sa.Column('bank_name', sa.Text),
    sa.Column('bank_street', sa.Text),
    sa.Column('bank_city', sa.Text),
    sa.Column('bank_state', sa.Text),
    sa.Column('bank_zip', sa.Text),
    sa.Column('gross_approval', sa.BigInteger),
    sa.Column('sba_guaranteed_approval', sa.BigInteger),
    sa.Column('approval_date', sa.DateTime),
    sa.Column('approval_fiscal_year', sa.BigInteger),
    sa.Column('first_disbursement_date', sa.DateTime),
    sa.Column('delivery_method', sa.Text),
    sa.Column('subprogram_description', sa.Text),
    sa.Column('initial_interest_rate', sa.Numeric),
    sa.Column('term_in_months', sa.BigInteger),
    sa.Column('naics_code', sa.Numeric),
    sa.Column('naics_description', sa.Text),
    sa.Column('franchise_code', sa.Text),
    sa.Column('franchise_name', sa.Text),
    sa.Column('project_county', sa.Text),
    sa.Column('project_state', sa.Text),
    sa.Column('sba_district_office', sa.Text),
    sa.Column('congressional_district', sa.Numeric),
    sa.Column('business_type', sa.Text),
    sa.Column('loan_status', sa.Text),
    sa.Column('chargeoff_date', sa.Date),
    sa.Column('gross_chargeoff_amount', sa.BigInteger),
    sa.Column('revolver_status', sa.BigInteger),
    sa.Column('jobs_supported', sa.BigInteger),
    schema='data_ingest')


DATA_INGEST__SBA__FOIA_7A_2000_2009 = sa.Table(
    'sba__foia_7a_2000_2009', METADATA,
    sa.Column('program', sa.Text),
    sa.Column('borr_name', sa.Text),
    sa.Column('borr_street', sa.Text),
    sa.Column('borr_city', sa.Text),
    sa.Column('borr_state', sa.Text),
    sa.Column('borr_zip', sa.Text),
    sa.Column('bank_name', sa.Text),
    sa.Column('bank_street', sa.Text),
    sa.Column('bank_city', sa.Text),
    sa.Column('bank_state', sa.Text),
    sa.Column('bank_zip', sa.Text),
    sa.Column('gross_approval', sa.BigInteger),
    sa.Column('sba_guaranteed_approval', sa.BigInteger),
    sa.Column('approval_date', sa.DateTime),
    sa.Column('approval_fiscal_year', sa.BigInteger),
    sa.Column('first_disbursement_date', sa.DateTime),
    sa.Column('delivery_method', sa.Text),
    sa.Column('subprogram_description', sa.Text),
    sa.Column('initial_interest_rate', sa.Numeric),
    sa.Column('term_in_months', sa.BigInteger),
    sa.Column('naics_code', sa.Numeric),
    sa.Column('naics_description', sa.Text),
    sa.Column('franchise_code', sa.Text),
    sa.Column('franchise_name', sa.Text),
    sa.Column('project_county', sa.Text),
    sa.Column('project_state', sa.Text),
    sa.Column('sba_district_office', sa.Text),
    sa.Column('congressional_district', sa.Numeric),
    sa.Column('business_type', sa.Text),
    sa.Column('loan_status', sa.Text),
    sa.Column('chargeoff_date', sa.Date),
    sa.Column('gross_chargeoff_amount', sa.BigInteger),
    sa.Column('revolver_status', sa.BigInteger),
    sa.Column('jobs_supported', sa.BigInteger),
    schema='data_ingest')


DATA_INGEST__SBA__FOIA_7A_2010_PRESENT = sa.Table(
    'sba__foia_7a_2010_present', METADATA,
    sa.Column('program', sa.Text),
    sa.Column('borr_name', sa.Text),
    sa.Column('borr_street', sa.Text),
    sa.Column('borr_city', sa.Text),
    sa.Column('borr_state', sa.Text),
    sa.Column('borr_zip', sa.Text),
    sa.Column('bank_name', sa.Text),
    sa.Column('bank_street', sa.Text),
    sa.Column('bank_city', sa.Text),
    sa.Column('bank_state', sa.Text),
    sa.Column('bank_zip', sa.Text),
    sa.Column('gross_approval', sa.BigInteger),
    sa.Column('sba_guaranteed_approval', sa.BigInteger),
    sa.Column('approval_date', sa.DateTime),
    sa.Column('approval_fiscal_year', sa.BigInteger),
    sa.Column('first_disbursement_date', sa.DateTime),
    sa.Column('delivery_method', sa.Text),
    sa.Column('subprogram_description', sa.Text),
    sa.Column('initial_interest_rate', sa.Numeric),
    sa.Column('term_in_months', sa.BigInteger),
    sa.Column('naics_code', sa.Numeric),
    sa.Column('naics_description', sa.Text),
    sa.Column('franchise_code', sa.Text),
    sa.Column('franchise_name', sa.Text),
    sa.Column('project_county', sa.Text),
    sa.Column('project_state', sa.Text),
    sa.Column('sba_district_office', sa.Text),
    sa.Column('congressional_district', sa.Numeric),
    sa.Column('business_type', sa.Text),
    sa.Column('loan_status', sa.Text),
    sa.Column('chargeoff_date', sa.Date),
    sa.Column('gross_chargeoff_amount', sa.BigInteger),
    sa.Column('revolver_status', sa.BigInteger),
    sa.Column('jobs_supported', sa.BigInteger),
    schema='data_ingest')


INFORMATION_SCHEMA__COLUMNS = sa.Table(
    'columns', METADATA,
    sa.Column('table_schema', sa.Text),
    sa.Column('table_name', sa.Text),
    sa.Column('column_name', sa.Text),
    sa.Column('data_type', sa.Text),
    schema='information_schema')

STG_ANALYTICS__SBA_SFDO_ZIPS = sa.Table(
    'sba_sfdo_zips', METADATA,
    sa.Column('zipcode', sa.Text),
    schema='stg_analytics')

STG_ANALYTICS__SBA_SFDO_API_CALLS = sa.Table(
    'sba_sfdo_api_calls', METADATA,
    sa.Column('sba_sfdo_id', sa.BigInteger),
    sa.Column('full_address', sa.Text),
    sa.Column('yelp_rating', sa.Numeric),
    sa.Column('yelp_total_reviews', sa.Numeric),
    sa.Column('yelp_url', sa.Text),
    sa.Column('yelp_timestamp', sa.DateTime),
    sa.Column('civics_district', sa.Text),
    sa.Column('civics_timestamp', sa.DateTime),
    sa.Column('geocode_lat', sa.Numeric),
    sa.Column('geocode_long', sa.Numeric),
    sa.Column('geocode_timestamp', sa.DateTime),
    schema='stg_analytics')
