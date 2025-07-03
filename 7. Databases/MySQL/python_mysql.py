# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database = "learning"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
# cursorObject.execute("CREATE DATABASE learning")

#####

# creating table
# studentRecord = """ create table student ( Id int not null, Name varchar(20), Course varchar(20), primary key(Id))"""

# table created
# cursorObject.execute(studentRecord) 
 
#####

# Inserting Values

# ins = """ insert into student values(1,'Shiffana','Information Technology')"""

# cursorObject.execute(ins) - this is used to execute the query
# dataBase.commit() - this is used to save the changes

######

# Inserting Multiple Values

# ins = """ insert into student (Id, Name, Course) values (%s,%s,%s)"""
# val = [(2,'Madhih','Electrical'), 
#        (3,'David','Mechanical'),
#        (4,'Sam','Biology')]

# cursorObject.executemany(ins,val)
# dataBase.commit()

#######

# Selecting from the Table
# query = "select * from student"
# query = "select name, id from student"

# cursorObject.execute(query)
# result = cursorObject.fetchall()

# for x in result:
#     print(x)

######

# Other Commands

# Where Clause
# query = "select * from student where id = 1"

# Order by
# query = "select * from student order by id desc"

# Limit Clause
# query = "select * from student limit 2"

# Offset Clause
# query = "select * from student limit 2 offset 1"

# Update Statement
# update = "update student set course = 'Computer Science' where id = 1"

# Delete Statement
# delete = "delete from student where id = 1"

# Drop Table
# drop = "drop table student"

# Drop Table if exists
# drop = "drop table if exists student"

# cursorObject.execute(drop)
# dataBase.commit()

######

# disconnecting from server
# dataBase.close()