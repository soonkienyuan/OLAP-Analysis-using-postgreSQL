## Take note that snowflake cannot used for OLTP (databases)

# OLAP-BASED ANALYSIS OF DATA FINDING THE MOST COST EFFECTIVE, UNDERRATED, OR SKILLED BASKETBALL PLAYERS.

database - OLTP
data warehosue - OLAP

In this project, we will construct a database and data warehouse from scratch to store NBA basketball player data in order to demonstrate and gain experience setting up a database and data warehouse, as well as establishing a relationship between the entities.

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













