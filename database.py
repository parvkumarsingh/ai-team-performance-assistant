import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    print("Database connected")

except Exception as e:
    print("Database connection failed:", e)


def run_query(sql):
    print("Running SQL:", sql)
    
    cursor = conn.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)

    return df