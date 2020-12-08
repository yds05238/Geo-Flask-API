CREATE DATABASE api_dev;
CREATE DATABASE api_test;

\connect api_dev;
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_raster;
CREATE EXTENSION postgis_topology;


\connect api_test;
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_raster;
CREATE EXTENSION postgis_topology;

SELECT postgis_full_version();