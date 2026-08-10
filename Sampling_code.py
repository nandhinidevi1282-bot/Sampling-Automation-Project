
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sampling Techniques",
    layout="wide"
)

def load_data(file):

      try:
        global df

        df = pd.read_csv(file)

        return df

      except FileNotFoundError:

        st.error("File Not Found")

      except pd.errors.EmptyDataError:

        st.error("CSV File is Empty")

      except Exception as e:

        st.error(e)

      finally:

        st.info("Loading Process Completed")      


st.title("Sampling Techniques Automation")

menu = st.sidebar.selectbox(
    "Select Menu",
    (
        "Home",
        "Dataset Info & Sampling Techinques"
        
    )
)

if menu == "Home":

    st.header("Welcome")

    st.write("""
This application is used to perform various Sampling Techniques.

### Features

##### Dataset Information 

        ✔ Missing Values

        ✔ Duplicate Values

        ✔ Statistical Summary

##### Sampling Techniques

        ✔ Simple Random Sampling

        ✔ Systematic Sampling

        ✔ Stratified Sampling

        ✔ Cluster Sampling

""")

elif menu == "Dataset Info & Sampling Techinques":

    st.header("Dataset Info & Sampling Techinques")

    uploaded_file = st.sidebar.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    import numpy as np 

  

    if uploaded_file is not None:

        df = load_data(uploaded_file)

        st.dataframe(df)
  

    
        st.write("Rows and Columns")

        st.write(df.shape)

        st.write("Data Types")

        st.write(df.dtypes)

        st.subheader("Missing Values")

        st.write(df.isnull().sum())

        st.subheader("Removed NullValues")

        
        if df.isnull().sum().sum() > 0:

            if st.button("Remove Null Values"):

                df = df.dropna()

                st.success("Null Values Removed Successfully.")

                st.dataframe(df)
        else:
            st.success("There is no Null Values")


        st.subheader("Duplicate Values")

        st.write(df.duplicated().sum())

        st.subheader("Removed Duplicates ")

        if df.duplicated().sum() > 0:

            if st.button("Remove Duplicate Rows"):

                df = df.drop_duplicates()

                st.success("Duplicate Rows Removed Successfully.")

                st.dataframe(df)
            else:
                print("There is no Duplicate values")


        st.subheader("Statistical Summary")

        st.write(df.describe())  


        st.header("Sampling Techinques")
        
        sampling = st.selectbox(
            "Choose Sampling Technique",
            [
                "Simple Random Sampling",
                "Systematic Sampling",
                "Stratified Sampling",
                "Cluster Sampling"
            ]
        )

        if sampling == "Simple Random Sampling":

            sample_size = st.number_input(
                "Enter Sample Size",
                min_value=1,
                max_value=len(df),
                value=5
            )

            if st.button("Generate Sample"):

                sample = df.sample(
                    n=sample_size,
                    random_state=42
                )

                st.write(sample)

        elif sampling == "Systematic Sampling":

            interval = st.number_input(
                "Enter Interval (k)",
                min_value=1,
                value=2
            )

            if st.button("Generate Sample"):

                sample = df.iloc[::interval]

                st.write(sample)


        elif sampling == "Stratified Sampling":

            category = st.selectbox(
                "Select Category Column",
                df.select_dtypes(include="object").columns
            )

            sample_size = st.number_input(
                "Sample Size per Group",
                min_value=1,
                value=2
            )

            if st.button("Generate Sample"):

                sample = df.groupby(category).apply(
                    lambda x: x.sample(
                        min(len(x), sample_size),
                        random_state=42
                    )
                )

                st.write(sample)  

        elif sampling == "Cluster Sampling":

            category = st.selectbox(
                "Select Cluster Column",
                df.select_dtypes(include="object").columns
            )

            cluster = st.selectbox(
                "Select Cluster",
                df[category].unique()
            )

            if st.button("Generate Sample"):

                sample = df[df[category] == cluster]
                st.write(sample)   

    else:
        st.warning("Please upload a dataset first.")   
else:          

        st.info("Please select an option from the sidebar.")
    
