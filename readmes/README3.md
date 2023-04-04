# Database - Basic Usage

## Topics covered

SQL's DDL and DML.

## Goal achieved

You will define a database structure to store the data of your application. You will also generate an SQL file with all the data as insert statements to populate the tables and will test the structure by defining and running some queries.

## Steps

### Create the database structure

Create a new database to store the data of the Warehouse application. Create tables for each one of the entities you have previously defined as classes. That is:

- Employee
- Item
- Warehouse

> The User class does not require a database table as it contains no data and it is only used to implement non-employees.

Define the SQL statements to create these tables with their fields. Then, execute them to create the tables on the new database. You can use Dbeaver to create the database and tables.

### Loading the data

After creating the tables, write a Python script that reads the data from the JSON files and writes a file with the SQL statements required to insert the data into the database tables.

Once you have the inserts in a file, execute it from the command-line (because the file may become big, it is a good idea to import it without opening the file first).

### Test the tables and data

When the tables are populated, write and execute the SQL statements to obtain the following information:

1. How many smartphones are there in stock?
```
176
```

2. How many `blue` items are there in stock in warehouse 1?
```
90
```

3. Show a list of all warehouses, with their `name` and the `amount` of items in stock. Sort the list by amount of items, so that the warehouses with most items appear on top.
```
    name     | count
-------------+-------
 Warehouse 1 |  1345
 Warehouse 2 |  1254
 Warehouse 4 |  1220
 Warehouse 3 |  1168
(4 rows)
```
