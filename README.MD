## Take note that snowflake cannot used for OLTP (databases)

# OLAP-BASED ANALYSIS OF DATA FINDING THE MOST COST EFFECTIVE, UNDERRATED, OR SKILLED BASKETBALL PLAYERS.

database - OLTP

data warehosue - OLAP

**In this project, we will construct a database and data warehouse from scratch to store NBA basketball player data in order to demonstrate and gain experience setting up a database and data warehouse, as well as establishing a relationship between the entities.**

Thus, perform OLAP analysis in data warehouse and Tableau to find the solution.

PostgreSQL will used in this project


## Objectives 


This project is aimed to help in properly choosing a roster that is the most optimal in terms of player value and performance with a minimum budget.

The solution is to find players that have adequate skills and pay but can further show their potential on the field by playing the correct position in the games.

## Isuuse faced

1. The main issue in building a team is the limited budget presented to a team that is only newly formed.

2. With a small budget, there are chances of unskilled players being included in the roster.



## Why PostgreSQL

1.  According to Gabriele Bartolini, the founder of the Italian PostgreSQL, PostgreSQL can serve as both a data warehouse and a database.

2. Not every SMB can afford a cloud-based data warehouse such as snowflake and Redshift. Consequently, learning posgrelSQL is beneficial.

3. free

4. reliable

5. community support


##  Architecture

![Architecture](https://github.com/soonkienyuan/OLAP-Analysis-using-postgreSQL/blob/main/image/database%20architecture.jpg?raw=true)

Data source avalable on Kaggel : [click here](https://www.kaggle.com/datasets/wyattowalsh/basketball)

You may notice that, the data source is in the SQLite format.

so, we need to extract and transform it  into a specified format that can be accepted by the relational database management system (RDBMS), PostgreSQL database. Then load into PostgreSQL. (ETL)

The RDBMS will be the platform for online transaction processing (OLTP), where online transactions like INSERT, UPDATE, DELETE occur.

Since we use same platform for RDBMS and data warehouse, then extract, load, and transform (ELT) will be the best solution to improve the efficiency of a process and save time.

However, there are some data in RDBMS are not suitable in data warehouse for Online analytical processing (OLAP). 

Hence, transforming step occur in the data warehouse. (ELT)

Lastly, Machine learning and analytic included OLAP and visualization can be performed by connecting to the data warehouse

In detail, Tableau will used to perform the OLAP and visualization by connecting to the data warehouse we developed.

## Database 

The names of the RDBMS and data warehouse are listed below.

RDBMS - basket_db3 

data warehouse - basket_dw_backup

To load into your PosgreSQL, please follow steps below:

1. Download it
2. open pgAdmin
3. create a ner database or use existing database
4. right click it and select restore

### ERD of RDBMS (basket_db3)
ERD- [click here](https://github.com/soonkienyuan/OLAP-Analysis-using-postgreSQL/blob/main/image/database_erd.pgerd%20(1).png)
- contains 16 tables.
- Because few tables have more than 50 columns or attributes, it is not possible to present as a figure on this page.
- ERD was built using PostgreSQL, and that PostgreSQL also auto aligned the ERD so that it appears in the correct order.

### data warehosue Data schema (basket_dw)

This is the final transformed data warehouse data schema

draw.io version - [click here](https://github.com/soonkienyuan/OLAP-Analysis-using-postgreSQL/blob/main/image/Galaxy%20schema.jpg)

Full version - [click here](https://github.com/soonkienyuan/OLAP-Analysis-using-postgreSQL/blob/main/image/Galaxy%20schema%20in%20erd.png)

It is a galaxy schema.

## ETL Pipeline

### ETL (from data source to RDBMS)

![ETL 1](https://github.com/soonkienyuan/OLAP-Analysis-using-postgreSQL/blob/main/image/ETL%20Pipeline.jpg?raw=true)

Due to the fact that SQLite and PostgreSQL implement distinct data types, which cannot be directly exchanged with each other. We will use python to perform ETL before the data goes into database.

1. Download and import SQLite, SQLAlchemy and pandas library.
3. Use connect function that provided by SQLite python library to connect the SQLite database.
4. Run a query in python that displays all accessible tables to see what kinds of tables SQLite has and how many of each kind there are. (query= "SELECT name FROM sqlite_master WHERE type='table';")
5. Create an engine that based on PostgreSQL for the next step.
6. Use read_sql_query() function provided by pandas to read data from the SQLite database, and then convert into pandas data frame
7. In the final step, the data frame is converted to SQL using the dataframe.to sql() function, and then the engine created in step 4 is used to insert data into the database by running SQL operations.

### ELT (from RDBMS to Data Warehosue)

![ETL 1](https://github.com/soonkienyuan/OLAP-Analysis-using-postgreSQL/blob/main/image/ETL%20pipeline2.jpg?raw=true)

Since we use the same platform (PostgreSQL) for both RDBMS and data warehousing. So, we don't have to transform the data before loading it into a data warehouse.

When it was necessary, various transformation procedures, including drop table, sort table, join table, aggregate table, and Lookup, were applied.

1. Drop table - to remove a table and all its rows - we succeed dropped 9 tables for OLAP in data warehouse, basket_dw 
2. Aggregate table - Creating aggregate tables reduces data warehouse access. More than one aggregate table can improve schema performance. (MIN, MAX,SUM,COUNT,AVG and so on) 
3. Joining table - Joining multiple attributes into one. (Inner join, outer join, full join and so on) 
4. Sorting - sorting data or row data or tuple based on the basis of some attribute. (Order by)




## Results and Data Analysis

Tableau excels in working with relational databases, and while it can connect to OLAP cubes, doing so duplicates Tableau's aggregation and hierarchy features. Tableau is also suited for a variety of non-SQL and big data solutions, such as the direct Google Big Query connector.

- Bradley Beal, who plays for the Cleveland Cavaliers, is the player who is both the most cost effective and the most underrated that we discovered using OLAP analysis in 2021.

- New Orleans Pelicans had the highest pick among all teams, this indicates that they are the most likely team to be likely to succeed and potential.

## Challenges and Conclusion

- Data in modern computing is stored in a wide variety of locations and formats, which, with a few exceptions, are incompatible with one another, we need to construct a complicated ETL pipeline.

- In certain circumstances, a non-SQL database is a much better option than an RDBMS due to the complex ETL process and the requirement of a pre-defined format.

- PostgreSQL is unsuitable for use as a data warehouse over the long term, particularly if your company is growing rapidly and generating large amounts of data.

- Due to the fact that the formats, data structures, and logical schemas of various databases are all distinct from one another. The process of migrating data from RDBMS to data warehouse is limited by the lack of available resources and free solutions in internet. It was necessary to spend money on hiring a data warehousing specialist to complete it.








