# blog link :- https://rohan-anand.hashnode.dev/automatically-document-your-database-in-markdown

import mysql.connector
from mysql.connector import errorcode


config = {
    'user': 'root',
    'password': 'rohan',
    'host': 'localhost',
    'database': 'sakila'
}

# Connect to the database
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

# Query the database schema
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# Generate Markdown documentation for each table
for table in tables:
    table_name = table[0]
    cursor.execute(f"DESCRIBE {table_name}")
    columns = cursor.fetchall()

    # Create a Markdown table with column information
    table_md = f"## Table {table_name}\n\n"
    table_md += "| Column | Type | Null | Key | Default | Extra |\n"
    table_md += "| ------ | ---- | ---- | --- | ------- | ----- |\n"

    for column in columns:
        column_md = "| " + " | ".join(str(x) for x in column) + " |\n"
        table_md += column_md

    # Append the Markdown document to the file
    with open(f"{table_name}.md", "a") as f:
        f.write(table_md)

    # # Print the contents of the file
    # with open(f"{table_name}.md", "r") as f:
    #     print(f.read())

# Close the database connection
cursor.close()
cnx.close()
