COMMENT ON TABLE data_ingest.irs__zip_data IS 'Staging table containing the IRS Income tax statistics from 2014 (https://www.irs.gov/uac/soi-tax-stats-individual-income-tax-statistics-2014-zip-code-data-soi)';
COMMENT ON COLUMN data_ingest.irs__zip_data.state_fips IS 'The State Federal Information Processing System (FIPS) code';
COMMENT ON COLUMN data_ingest.irs__zip_data.state IS 'The State associated with the ZIP code';
COMMENT ON COLUMN data_ingest.irs__zip_data.zipcode IS '5-digit Zip code';
COMMENT ON COLUMN data_ingest.irs__zip_data.agi_stub IS 'Size of adjusted gross income; 1 = $1 under $25,000; 2 = $25,000 under $50,000; 3 = $50,000 under $75,000; 4 = $75,000 under $100,000; 6 = $200,000 or more+D1:D10';
COMMENT ON COLUMN data_ingest.irs__zip_data.n1 IS 'Number of returns';
COMMENT ON COLUMN data_ingest.irs__zip_data.mars1 IS 'Number of single returns';
COMMENT ON COLUMN data_ingest.irs__zip_data.mars2 IS 'Number of joint returns';
COMMENT ON COLUMN data_ingest.irs__zip_data.mars4 IS 'Number of head of household returns';
COMMENT ON COLUMN data_ingest.irs__zip_data.prep IS 'Number of returns with paid preparers signature';
COMMENT ON COLUMN data_ingest.irs__zip_data.n2 IS 'Number of exemptions';
COMMENT ON COLUMN data_ingest.irs__zip_data.numdep IS 'Number of dependents';
COMMENT ON COLUMN data_ingest.irs__zip_data.total_vita IS 'Total number of volunteer prepared returns [3]';
COMMENT ON COLUMN data_ingest.irs__zip_data.vita IS 'Number of volunteer income tax assistance (VITA) prepared returns [3]';
COMMENT ON COLUMN data_ingest.irs__zip_data.tce IS 'Number of tax counseling for the elderly (TCE) prepared returns [3]';
COMMENT ON COLUMN data_ingest.irs__zip_data.a00100 IS 'Adjust gross income (AGI) [2]';
COMMENT ON COLUMN data_ingest.irs__zip_data.n02650 IS 'Number of returns with total income';
COMMENT ON COLUMN data_ingest.irs__zip_data.a02650 IS 'Total income amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n00200 IS 'Number of returns with salaries and wages';
COMMENT ON COLUMN data_ingest.irs__zip_data.a00200 IS 'Salaries and wages amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n00300 IS 'Number of returns with taxable interest';
COMMENT ON COLUMN data_ingest.irs__zip_data.a00300 IS 'Taxable interest amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n00600 IS 'Number of returns with ordinary dividends ';
COMMENT ON COLUMN data_ingest.irs__zip_data.a00600 IS 'Ordinary dividends amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n00650 IS 'Number of returns with qualified dividends';
COMMENT ON COLUMN data_ingest.irs__zip_data.a00650 IS 'Qualified dividends amount [4]';
COMMENT ON COLUMN data_ingest.irs__zip_data.n00700 IS 'Number of returns with state and local income tax refunds';
COMMENT ON COLUMN data_ingest.irs__zip_data.a00700 IS 'State and local income tax refunds amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n00900 IS 'Number of returns with business or professional net income (less loss)';
COMMENT ON COLUMN data_ingest.irs__zip_data.a00900 IS 'Business or professional net income (less loss) amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n01000 IS 'Number of returns with net capital gain (less loss)';
COMMENT ON COLUMN data_ingest.irs__zip_data.a01000 IS 'Net capital gain (less loss) amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n01400 IS 'Number of returns with taxable individual retirement arrangements distributions';
COMMENT ON COLUMN data_ingest.irs__zip_data.a01400 IS 'Taxable individual retirement arrangements distributions amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n01700 IS 'Number of returns with taxable pensions and annuities';
COMMENT ON COLUMN data_ingest.irs__zip_data.a01700 IS 'Taxable pensions and annuities amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.schf IS 'Number of farm returns';
COMMENT ON COLUMN data_ingest.irs__zip_data.n02300 IS 'Number of returns with unemployment compensation';
COMMENT ON COLUMN data_ingest.irs__zip_data.a02300 IS 'Unemployment compensation amount [5]';
COMMENT ON COLUMN data_ingest.irs__zip_data.n02500 IS 'Number of returns with taxable Social Security benefits';
COMMENT ON COLUMN data_ingest.irs__zip_data.a02500 IS 'Taxable Social Security benefits amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n26270 IS 'Number of returns with partnership/S-corp net income (less loss)';
COMMENT ON COLUMN data_ingest.irs__zip_data.a26270 IS 'Partnership/S-corp net income (less loss) amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n02900 IS 'Number of returns with total statutory adjustments';
COMMENT ON COLUMN data_ingest.irs__zip_data.a02900 IS 'Total statutory adjustments amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n03220 IS 'Number of returns with educator expenses';
COMMENT ON COLUMN data_ingest.irs__zip_data.a03220 IS 'Educator expenses amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n03300 IS 'Number of returns with self-employment retirement plans';
COMMENT ON COLUMN data_ingest.irs__zip_data.a03300 IS 'Self-employment retirement plans amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n03270 IS 'Number of returns with self-employment health insurance deduction';
COMMENT ON COLUMN data_ingest.irs__zip_data.a03270 IS 'Self-employment health insurance deduction amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n03150 IS 'Number of returns with IRA payments';
COMMENT ON COLUMN data_ingest.irs__zip_data.a03150 IS 'IRA payments amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n03210 IS 'Number of returns with student loan interest deduction';
COMMENT ON COLUMN data_ingest.irs__zip_data.a03210 IS 'Student loan interest deduction amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n03230 IS 'Number of returns with tuition and fees deduction';
COMMENT ON COLUMN data_ingest.irs__zip_data.a03230 IS 'Tuition and fees deduction amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n03240 IS 'Returns with domestic production activities deduction';
COMMENT ON COLUMN data_ingest.irs__zip_data.a03240 IS 'Domestic production activities deduction amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n04470 IS 'Number of returns with itemized deductions';
COMMENT ON COLUMN data_ingest.irs__zip_data.a04470 IS 'Total itemized deductions amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.a00101 IS 'Amount of AGI for itemized returns';
COMMENT ON COLUMN data_ingest.irs__zip_data.n18425 IS 'Number of returns with State and local income taxes';
COMMENT ON COLUMN data_ingest.irs__zip_data.a18425 IS 'State and local income taxes amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n18450 IS 'Number of returns with State and local general sales tax';
COMMENT ON COLUMN data_ingest.irs__zip_data.a18450 IS 'State and local general sales tax amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n18500 IS 'Number of returns with real estate taxes';
COMMENT ON COLUMN data_ingest.irs__zip_data.a18500 IS 'Real estate taxes amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n18300 IS 'Number of returns with taxes paid';
COMMENT ON COLUMN data_ingest.irs__zip_data.a18300 IS 'Taxes paid amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n19300 IS 'Number of returns with mortgage interest paid';
COMMENT ON COLUMN data_ingest.irs__zip_data.a19300 IS 'Mortgage interest paid amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n19700 IS 'Number of returns with contributions';
COMMENT ON COLUMN data_ingest.irs__zip_data.a19700 IS 'Contributions amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n04800 IS 'Number of returns with taxable income';
COMMENT ON COLUMN data_ingest.irs__zip_data.a04800 IS 'Taxable income amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n05800 IS 'Number of returns with income tax before credits';
COMMENT ON COLUMN data_ingest.irs__zip_data.a05800 IS 'Income tax before credits amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n09600 IS 'Number of returns with alternative minimum tax ';
COMMENT ON COLUMN data_ingest.irs__zip_data.a09600 IS 'Alternative minimum tax amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n05780 IS 'Number of returns with excess advance premium tax credit repayment';
COMMENT ON COLUMN data_ingest.irs__zip_data.a05780 IS 'Excess advance premium tax credit repayment amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n07100 IS 'Number of returns with total tax credits';
COMMENT ON COLUMN data_ingest.irs__zip_data.a07100 IS 'Total tax credits amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n07300 IS 'Number of returns with foreign tax credit';
COMMENT ON COLUMN data_ingest.irs__zip_data.a07300 IS 'Foreign tax credit amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n07180 IS 'Number of returns with child and dependent care credit';
COMMENT ON COLUMN data_ingest.irs__zip_data.a07180 IS 'Child and dependent care credit amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n07230 IS 'Number of returns with nonrefundable education credit';
COMMENT ON COLUMN data_ingest.irs__zip_data.a07230 IS 'Nonrefundable education credit amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n07240 IS 'Number of returns with retirement savings contribution credit';
COMMENT ON COLUMN data_ingest.irs__zip_data.a07240 IS 'Retirement savings contribution credit amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n07220 IS 'Number of returns with child tax credit';
COMMENT ON COLUMN data_ingest.irs__zip_data.a07220 IS 'Child tax credit amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n07260 IS 'Number of returns with residential energy tax credit';
COMMENT ON COLUMN data_ingest.irs__zip_data.a07260 IS 'Residential energy tax credit amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n09400 IS 'Number of returns with self-employment tax';
COMMENT ON COLUMN data_ingest.irs__zip_data.a09400 IS 'Self-employment tax amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n85770 IS 'Number of returns with total premium tax credit';
COMMENT ON COLUMN data_ingest.irs__zip_data.a85770 IS 'Total premium tax credit amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n85775 IS 'Number of returns with advance premium tax credit';
COMMENT ON COLUMN data_ingest.irs__zip_data.a85775 IS 'Advance premium tax credit amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n09750 IS 'Number of returns with health care individual responsibility payment';
COMMENT ON COLUMN data_ingest.irs__zip_data.a09750 IS 'Health care individual responsibility payment amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n10600 IS 'Number of returns with total tax payments';
COMMENT ON COLUMN data_ingest.irs__zip_data.a10600 IS 'Total tax payments amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n59660 IS 'Number of returns with earned income credit';
COMMENT ON COLUMN data_ingest.irs__zip_data.a59660 IS 'Earned income credit amount [6]  ';
COMMENT ON COLUMN data_ingest.irs__zip_data.n59720 IS 'Number of returns with excess earned income credit';
COMMENT ON COLUMN data_ingest.irs__zip_data.a59720 IS 'Excess earned income credit (refundable) amount [7]  ';
COMMENT ON COLUMN data_ingest.irs__zip_data.n11070 IS 'Number of returns with additional child tax credit';
COMMENT ON COLUMN data_ingest.irs__zip_data.a11070 IS 'Additional child tax credit amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n10960 IS 'Number of returns with refundable education credit';
COMMENT ON COLUMN data_ingest.irs__zip_data.a10960 IS 'Refundable education credit amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n11560 IS 'Number of returns with net premium tax credit';
COMMENT ON COLUMN data_ingest.irs__zip_data.a11560 IS 'Net premium tax credit amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n06500 IS 'Number of returns with income tax';
COMMENT ON COLUMN data_ingest.irs__zip_data.a06500 IS 'Income tax amount [8]  ';
COMMENT ON COLUMN data_ingest.irs__zip_data.n10300 IS 'Number of returns with tax liability';
COMMENT ON COLUMN data_ingest.irs__zip_data.a10300 IS 'Total tax liability amount [9]  ';
COMMENT ON COLUMN data_ingest.irs__zip_data.n85530 IS 'Number of returns with additional Medicare tax';
COMMENT ON COLUMN data_ingest.irs__zip_data.a85530 IS 'Additional Medicare tax amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n85300 IS 'Number of returns with net investment income tax';
COMMENT ON COLUMN data_ingest.irs__zip_data.a85300 IS 'Net investment income tax amount';
COMMENT ON COLUMN data_ingest.irs__zip_data.n11901 IS 'Number of returns with tax due at time of filing';
COMMENT ON COLUMN data_ingest.irs__zip_data.a11901 IS 'Tax due at time of filing amount [10]  ';
COMMENT ON COLUMN data_ingest.irs__zip_data.n11902 IS 'Number of returns with overpayments refunded';
COMMENT ON COLUMN data_ingest.irs__zip_data.a11902 IS 'Overpayments refunded amount [11]  ';