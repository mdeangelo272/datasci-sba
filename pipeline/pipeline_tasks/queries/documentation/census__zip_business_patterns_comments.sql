COMMENT ON TABLE data_ingest.census__zip_business_patterns IS 'ZIP Code Business Patterns by Employment Size Class: 2015 (http://www2.census.gov/econ2015/CB/sector00/CB1500CZ21.zip)';
COMMENT ON COLUMN data_ingest.census__zip_business_patterns.geo_id IS 'Geographic identifier code';
COMMENT ON COLUMN data_ingest.census__zip_business_patterns.geo_ttl IS 'Id2';
COMMENT ON COLUMN data_ingest.census__zip_business_patterns.footid_geo IS 'Geographic area name';
COMMENT ON COLUMN data_ingest.census__zip_business_patterns.naics2012 IS '2012 NAICS code';
COMMENT ON COLUMN data_ingest.census__zip_business_patterns.naics2012_ttl IS 'Meaning of 2012 NAICS code';
COMMENT ON COLUMN data_ingest.census__zip_business_patterns.year IS 'Year';
COMMENT ON COLUMN data_ingest.census__zip_business_patterns.empszes IS 'Employment size of establishment';
COMMENT ON COLUMN data_ingest.census__zip_business_patterns.empszes_ttl IS 'Meaning of Employment size of establishment';
COMMENT ON COLUMN data_ingest.census__zip_business_patterns.estab IS 'Number of establishments';