
create or replace table incident_map 
(
crime_type varchar
,lsoa_code varchar
,longitude float
,latitude float
,region varchar
,outcome varchar
,victim_age varchar
,perp_age varchar
,victim_ethnicity varchar
,perp_ethnicity varchar
,incident_time timestamp(0)
,incident_date date
,reported_to_police varchar(1)
,reported_on_survey varchar(1)
,self_reported varchar(1)
);
