CREATE or replace TABLE SELF_REPORTING_RAW
(
INCIDENT_TYPE VARCHAR(50),
INCIDENT_DESCRIPTION VARCHAR(200),
LOCATION_OF_INCIDENT VARCHAR(50), 
--DATE_OF_INCIDENT DATE,
--TIME_OF_INCIDENT DATETIME,
REPORTED_TO_THE_POLICE VARCHAR(50),
VICTIM_AGE VARCHAR(50),
VICTIM_GENDER VARCHAR(50),
VICTIM_ETHNICITY VARCHAR(200), 
PERP_GENDER VARCHAR(50),
PERP_KNOWN_TO_VICTIM VARCHAR(50)
)
;