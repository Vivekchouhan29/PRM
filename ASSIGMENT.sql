CREATE DATABASE ASSIGMENT;
USE  ASSIGMENT;

CREATE TABLE countries( 
COUNTRY_ID varchar(2),
COUNTRY_NAME varchar(40),
CHECK(COUNTRY_NAME IN('Italy','India','China')),
REGION_ID decimal(10,0)
);

