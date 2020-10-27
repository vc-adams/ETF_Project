-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/jCWWo0
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.
-- -- ---------------------------------------------------------------------------------------------------------------------
-- -- IF YOU MAKE A MISTAKE AND NEED TO START OVER, YOU'D NEED TO DROP THE TABLES AND RECREATE THEM

-- DROP TABLE Auto_Insurance_Data;
-- DROP TABLE Weather_Data;

-- -- ---------------------------------------------------------------------------------------------------------------------
-- -- CREATE TABLES

CREATE TABLE Weather_Data (
	ID SERIAL,
    Zip_Code Integer   NOT NULL,
    Weather_Forecast Varchar   NOT NULL,
    Weather_Description Varchar   NOT NULL,
    Max_Temperature Float   NOT NULL,
    Min_Temperature Float   NOT NULL,
    Humidity Float   NOT NULL,
	PRIMARY KEY (ID)
);

CREATE TABLE Auto_Insurance_Data (
	ID SERIAL,
    State Varchar   NOT NULL,
    Zip_Code Integer   NOT NULL,
    City Varchar   NOT NULL,
    Average_Auto_Insurance_Rate Float   NOT NULL,
	PRIMARY KEY (ID)
);

-- -- ---------------------------------------------------------------------------------------------------------------------
-- -- IMPORT DATA
-- -- Right click the table and select Import/Export and import the csv for the corresponding table

-- -- ---------------------------------------------------------------------------------------------------------------------
-- -- CREATE JOINED TABLE

-- SELECT a.State, a.Zip_Code, w.Zip_Code, a.city, w.Weather_Forecast, w.Weather_Description, w.Max_Temperature,
-- 	   w.Min_Temperature, w.Humidity
-- FROM Auto_Insurance_Data AS a
-- INNER JOIN Weather_Data AS w 
-- ON a.Zip_Code = w.Zip_Code;