import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit UI
st.title("Interactive Data Analysis Dashboard")


def display_records(tab,df):
        col1, col2  = tab.columns(2)
        with col1:
            tab.dataframe(df, 
                column_config={
                    "Project name": "Project",
                    "Client name": "Client",
                    "Department": "Department",
                    "Project value": st.column_config.NumberColumn(
                        "Value",
                        format="$%d ")
                },
                hide_index=True,
            )
        with col2:
             tab.line_chart(
                df,
                x="Project name",
                y=["Project value",],
                color=["#0000FF"]
            )
        
def scope_breakdown(tab,df):
     # Count occurrences of each Project Scope
    scope_counts = df["Project scope"].value_counts()

    # Matplotlib Visualization
    fig, ax = plt.subplots(figsize=(8, 5))
    scope_counts.plot(kind="bar", color=["blue", "orange", "green"], ax=ax)
    ax.set_xlabel("Project Scope")
    ax.set_ylabel("Number of Projects")
    ax.set_title("Project Scope Breakdown")
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    # Display in Streamlit
    tab.pyplot(fig)     

def delay(tab,df):
    # Sort data by delay for better visualization
    df = df.sort_values(by="Project Delay cycle", ascending=False)
    # Plot Project Delays
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(df["Project name"], df["Project Delay cycle"], color="red")
    ax.set_xlabel("Delay Cycle (in Days)")
    ax.set_ylabel("Project Name")
    ax.set_title("Project Delay Across Each Project")
    ax.grid(axis="x", linestyle="--", alpha=0.7)

    # Display in Streamlit
    tab.pyplot(fig)


def payment_cycle(tab,df):
     # Sort data by delay for better visualization
    df = df.sort_values(by="Payment Cycle", ascending=False)
    # Plot Payment Cycle
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(df["Project name"], df["Project Delay cycle"], color="green")
    ax.set_xlabel("Payment Cycle (in Days)")
    ax.set_ylabel("Project Name")
    ax.set_title("Payment Across Each Project")
    ax.grid(axis="x", linestyle="--", alpha=0.7)

    # Display in Streamlit
    tab.pyplot(fig)


def app():
    uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
         
        tab1, tab2, tab3, tab4 = st.tabs(["$Project Value", "Project Scope Breakdown","Project Delay","Payment Cycle"])
       #Summary of Projects and thier value
        tab1.subheader("Summary of Project and Total $ Value")
        trim_df =  df[["Project name", "Client name", "Department", "Project value"]]
        display_records(tab1,trim_df)

        #Project Breakdown
        scope_breakdown(tab2,df)

        #Delay Cycle
        delay(tab3,df)

        #Payment Cycle
        payment_cycle(tab4,df)

if __name__ == "__main__":
    app()
