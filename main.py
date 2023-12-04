import time
from mongo_db import MongoDB
from sql_server_db import SqlServerDB

# Використовуємо MS SQL Server i MongoDB
mongo_db_url = "mongodb://localhost:27017/"
mongo_db_name = "ITDB"

sql_server_connection_string = "Driver={ODBC Driver 18 for SQL Server};Server=(LocalDB)\\MSSQLLocalDB; Database=ITDB; Integrated Security=True; MultipleActiveResultSets=true"

mongo_db_s = MongoDB(mongo_db_url, mongo_db_name)

sql_server_db_s = SqlServerDB(sql_server_connection_string)
n = 50
start_mongo = time.time()
for i in range(n):
    mongo_db_s.crud_m()
mongo_time = time.time() - start_mongo
print(f"Time for CRUD in MongoDB: {mongo_time}")

start_sql = time.time()
for i in range(n):
    sql_server_db_s.crud_sql()
sql_time = time.time() - start_sql
print(f"Time for CRUD in SQL: {sql_time}")