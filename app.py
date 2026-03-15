import streamlit as st
import pandas as pd
from ai_engine import generate_sql
from database import run_query

st.set_page_config(page_title="AI Team Performance Assistant")

st.title("AI Team Performance Assistant")
st.write("Ask a question about team performance data.")

# User input
question = st.text_input("Enter your question")

if question:

    # Generate SQL
    sql = generate_sql(question)

    st.subheader("Generated SQL")
    st.code(sql)

    # Run query
    result = run_query(sql)

    st.subheader("Result")
    st.dataframe(result)

    # Stop if no data
    if result.empty:
        st.warning("Query returned no results.")
        st.stop()

    # ---------- CHART ----------
    numeric_cols = result.select_dtypes(include=['int64','float64']).columns

    if len(numeric_cols) > 0:

        st.subheader("Visualization")

        chart_column = st.selectbox(
            "Choose column for chart",
            numeric_cols
        )

        st.bar_chart(result[chart_column])

    else:
        st.info("No numeric columns available for chart.")

    # ---------- AI INSIGHTS ----------
    if len(numeric_cols) > 0:

        col = numeric_cols[0]

        max_value = result[col].max()
        min_value = result[col].min()
        avg_value = result[col].mean()

        st.subheader("AI Insight")

        st.write(f"Highest {col}: {max_value}")
        st.write(f"Lowest {col}: {min_value}")
        st.write(f"Average {col}: {round(avg_value,2)}")

    else:
        st.info("No numeric columns available for insights.")