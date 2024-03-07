insert into incident_map(
    crime_type 
    ,lsoa_code 
    ,longitude
    ,latitude 
    ,outcome 
    ,incident_date 
    ,reported_to_police 
    ,reported_on_survey 
    ,self_reported
    ) select
        "Crime_Type"
        ,"LSOA_Code"
        ,"Latitude"
        ,"Longitude"
        ,"Last_Outcome_Category"
        ,"Effective_Snapshot_Date"
        ,'Y'
        ,null
        ,null
        from FACTS_AND_DIMENSIONS_ALL_DATA."Police"."fact_Crimes"
         where contains("Crime_Type",'sex');

create or replace table survey_groping as select * from WID_HACKATHON_PRIVATE_DATASETS.SURVEY_FEATURES.SAFETY_SURVEY_DATA where experienced_public_groping = 1;

CREATE OR REPLACE TABLE WID_HACKATHON.DATA.survey_rape AS 
  SELECT * 
FROM WID_HACKATHON_PRIVATE_DATASETS.SURVEY_FEATURES.SAFETY_SURVEY_DATA
WHERE EXPERIENCED_PUBLIC_RAPE = 1 OR EXPERIENCED_PRIVATE_RAPE;

insert into wid_hackathon.data.incident_map(
    CRIME_TYPe
    , region
    , VICTIM_AGE
    , VICTIM_ETHNICITY
    , REPORTED_TO_POLICE
    , REPORTED_ON_SURVEY
    ,SELF_REPORTED 
) SELECT
    'Sexual Assault'
    , "DEMOG_REGION"
    , DEMOG_AGE
    , DEMOG_ETHNICITY
    , CASE WHEN REPORTED_PUBLIC_GROPING = 1 THEN 'Y' ELSE 'N' END
    , 'Y'
    , null
    FROM survey_groping;

INSERT INTO WID_HACKATHON.DATA.INCIDENT_MAP (
    CRIME_TYPE
    , region
    , VICTIM_AGE
    , VICTIM_ETHNICITY
    , REPORTED_TO_POLICE
    , REPORTED_ON_SURVEY
    ,SELF_REPORTED 
) SELECT
    'Rape'
    , "DEMOG_REGION"
    , DEMOG_AGE
    , DEMOG_ETHNICITY
    , CASE WHEN REPORTED_PUBLIC_RAPE = 1 THEN 'Y' ELSE 'N' END
    , 'Y'
    , null
    FROM SURVEY_RAPE;
