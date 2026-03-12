import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Sales Data Analytics Dashboard", layout="wide")

st.title("📊 Sales Data Analytics Dashboard")

st.write("Upload a CSV file to analyze sales data.")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:

    # Read dataset with encoding fix
    try:
        df = pd.read_csv(uploaded_file, encoding="utf-8")
    except:
        df = pd.read_csv(uploaded_file, encoding="latin1")

    # Show dataset
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Dataset info
    st.subheader("Dataset Information")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    # Summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Missing values
    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    # Show column names
    st.subheader("Column Names")
    st.write(df.columns)

    # Sales by Category chart
    if "Category" in df.columns and "Sales" in df.columns:

        st.subheader("Sales by Category")

        category_sales = df.groupby("Category")["Sales"].sum()

        fig = plt.figure()
        plt.bar(category_sales.index, category_sales.values)
        plt.xlabel("Category")
        plt.ylabel("Sales")
        plt.title("Sales by Category")

        st.pyplot(fig)

    # Sales by Region chart
    if "Region" in df.columns and "Sales" in df.columns:

        st.subheader("Sales by Region")

        region_sales = df.groupby("Region")["Sales"].sum()

        fig = plt.figure()
        plt.bar(region_sales.index, region_sales.values)
        plt.xlabel("Region")
        plt.ylabel("Sales")
        plt.title("Sales by Region")

        st.pyplot(fig)

    # Show full data
    st.subheader("Complete Dataset")
    st.dataframe(df)

else:
    st.info("Please upload a CSV file to start analysis.")