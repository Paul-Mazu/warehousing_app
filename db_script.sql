drop database warehouse;

create database warehouse;

\c warehouse 

CREATE TABLE warehouse(
    id SERIAL PRIMARY KEY,
    name VARCHAR(15) NOT NULL
);

CREATE TABLE item(
    id SERIAL PRIMARY KEY,
    state VARCHAR(30) NOT NULL,
    category VARCHAR(30) NOT NULL,
    date_of_stock TIMESTAMP NOT NULL,
    warehouse_id INT REFERENCES warehouse(id) ON DELETE CASCADE
);

CREATE EXTENSION pgcrypto;

CREATE TABLE employee(
    id SERIAL,
    user_name VARCHAR(20) NOT NULL PRIMARY KEY,
    password TEXT NOT NULL,
    lead_by VARCHAR(20) REFERENCES employee(user_name)
);