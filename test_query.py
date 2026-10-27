
from database import create_database, execute_query
from sql_generator import generate_sql

create_database()

question = input("Ask a question about employees: ")

sql = generate_sql(question)
print("\nGenerated SQL:")
print(sql)

columns, rows = execute_query(sql)

print("\nResults:")
print(columns)

for row in rows:
    print(row)
