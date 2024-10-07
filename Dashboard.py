import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Financial Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    data = {
        'Date': ['2024/09/16-2024/09/22', '2024/09/23-2024/09/29', '2024/09/30-2024/10/06', '2024/10/07-2024/10/13', '2024/10/14-2024/10/20'],
        'Labor': [2726.2, 2700.8, 2765.4, 2850.5, 2780.3],
        'Food_Cost': [3409.72, 3380.5, 3425.8, 3550.25, 3480.6],
        'Total_Sales': [8440.43, 8300.25, 8500.6, 8750.8, 8600.2],
        'Profit': [2304.51, 2218.95, 2309.4, 2350.05, 2339.3],
        'Labor_Percent': [32.30, 32.54, 32.53, 32.57, 32.33],
        'Food_Cost_Percent': [40.40, 40.73, 40.30, 40.57, 40.47],
        'Profit_Percent': [27.30, 26.73, 27.17, 26.86, 27.20]
    }
    return pd.DataFrame(data)

df = load_data()

# Dashboard title
st.title("Financial Performance Dashboard")

# Summary metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Average Weekly Sales", f"${df['Total_Sales'].mean():.2f}")
col2.metric("Average Weekly Profit", f"${df['Profit'].mean():.2f}")
col3.metric("Average Labor %", f"{df['Labor_Percent'].mean():.2f}%")
col4.metric("Average Food Cost %", f"{df['Food_Cost_Percent'].mean():.2f}%")

# Line chart of Sales, Labor, and Food Cost
st.subheader("Weekly Sales, Labor, and Food Cost")
fig = px.line(df, x='Date', y=['Total_Sales', 'Labor', 'Food_Cost'], 
               title='Weekly Financial Metrics')
st.plotly_chart(fig, use_container_width=True)

# Bar chart of Profit
st.subheader("Weekly Profit")
fig = px.bar(df, x='Date', y='Profit', title='Weekly Profit')
st.plotly_chart(fig, use_container_width=True)

# Pie chart of average cost distribution
st.subheader("Average Cost Distribution")
avg_labor = df['Labor'].mean()
avg_food_cost = df['Food_Cost'].mean()
avg_profit = df['Profit'].mean()
fig = px.pie(values=[avg_labor, avg_food_cost, avg_profit], 
             names=['Labor', 'Food Cost', 'Profit'], 
             title='Average Cost Distribution')
st.plotly_chart(fig, use_container_width=True)

# Data table
st.subheader("Raw Data")
st.dataframe(df)
