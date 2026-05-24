import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")
st.title("Global Superstore Business Dashboard")

# 2. Data Loading (Cached for performance)
@st.cache_data
def load_data():
    # Update this filename if your downloaded file has a different name or extension (.xls)
    df = pd.read_csv('Global_Superstore2.csv', encoding='latin1')
    return df

df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Filter Data")

# Get unique values for filters
region_list = df['Region'].unique().tolist()
category_list = df['Category'].unique().tolist()

# Create multi-select filters
selected_regions = st.sidebar.multiselect("Select Region(s)", region_list, default=region_list)
selected_categories = st.sidebar.multiselect("Select Category(s)", category_list, default=category_list)

# Apply filters to the dataframe
filtered_df = df[
    (df['Region'].isin(selected_regions)) & 
    (df['Category'].isin(selected_categories))
]

# 4. Key Performance Indicators (KPIs)
st.subheader("Key Performance Indicators")
col1, col2, col3 = st.columns(3)

total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
profit_margin = (total_profit / total_sales) * 100 if total_sales > 0 else 0

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Profit Margin", f"{profit_margin:.2f}%")

st.markdown("---")

# 5. Visualizations
col_chart1, col_chart2 = st.columns(2)

# Chart 1: Sales by Sub-Category
with col_chart1:
    st.subheader("Sales by Sub-Category")
    subcat_sales = filtered_df.groupby('Sub-Category')['Sales'].sum().reset_index()
    subcat_sales = subcat_sales.sort_values(by='Sales', ascending=False)
    
    fig_sales = px.bar(subcat_sales, x='Sub-Category', y='Sales', color='Sales', color_continuous_scale='Blues')
    st.plotly_chart(fig_sales, use_container_width=True)

# Chart 2: Top 5 Customers by Sales
with col_chart2:
    st.subheader("Top 5 Customers")
    top_customers = filtered_df.groupby('Customer Name')['Sales'].sum().reset_index()
    top_customers = top_customers.sort_values(by='Sales', ascending=False).head(5)
    
    fig_cust = px.bar(top_customers, x='Sales', y='Customer Name', orientation='h', color='Sales', color_continuous_scale='Greens')
    # Reverse y-axis so the highest is at the top
    fig_cust.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig_cust, use_container_width=True)