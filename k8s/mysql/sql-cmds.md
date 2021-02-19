# SQL Database command
---

- Run mysql client
  `kubectl run -it --rm --image=mysql:5.6 --restart=Never mysql-client -- mysql -h mysql -p'oracle!2345#'`
- Create Database
  `create database test_db;`
- Use Database
  ` use test_db;`
- Show Database
  `show databases;`
- Create Table
  ```
  create table [table name] (personid int(50) not null auto_increment primary key,firstname varchar(35),middlename varchar(50),lastname varchar(50) default 'bato');

  create table test_table (id int(50) not null auto_increment primary key, firstname varchar(35), lastname varchar(50));
  ```
- Insert Row - based on Table created (id, first and last name)
  ```
  INSERT INTO `test_table`  VALUES (1, 'john', 'doe');
  INSERT INTO `test_table`  VALUES (2, 'jane', 'doe');
  INSERT INTO `test_table`  VALUES (3, 'bob',  'smith');
  ```
- List Table
  `select * from test_table;`

