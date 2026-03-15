from transformers import pipeline

# Load lightweight SQL model
generator = pipeline(
    "text-generation",
    model="NumbersStation/nsql-350M",
    max_new_tokens=100
)

def generate_sql(question):

    prompt = f"""
You are an SQL assistant.

Database Table: team_performance

Columns:
employee_name
task_completed
minutes_worked
performance_score

Generate ONLY a valid SQL query.

Question: {question}

SQL:
"""

    result = generator(prompt)[0]["generated_text"]

    # Extract SQL starting from SELECT
    sql_start = result.upper().find("SELECT")

    if sql_start != -1:
        sql = result[sql_start:]
    else:
        sql = "SELECT * FROM team_performance"

    # Stop SQL at first semicolon
    if ";" in sql:
        sql = sql.split(";")[0] + ";"
    else:
        sql = sql + ";"

    return sql.strip()