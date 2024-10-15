import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Dashboard")
st.header('Leap Uptime Dashboard 2024')
#st.subheader('LEAP App')

# Add a simple example
#st.write("Welcome to the LEAP Uptime Dashboard for Year 2024")

# Load DataFrame
excel_file = 'Sample.xlsx'
sheet_name = 'Data'

df = pd.read_excel(excel_file,
                   sheet_name,
                   usecols = 'A:I',
                   header = 0)

st.dataframe(df)

#application = df['Application'].unique().tolist()
#application_selection = st.multiselect('Application:',
#                                        application,
#                                        default=application)

#mask = df['Application'].isin(application_selection)
#number_of_results = df[mask].shape[0]
#st.markdown(f'*Available Results : {number_of_results}*')


## Application Created Chart
app_his_chart = px.histogram(df,
                   x = 'Month',
                   y = 'Applications Created',
                   color='Application',
                   barmode='group',
                   title = 'Applications Created')

st.plotly_chart(app_his_chart)

## RNA Completed Chart
rna_his_chart = px.histogram(df,
                   x = 'Month',
                   y = 'RNA Completed',
                   color='Application',
                   barmode='group',
                   title = 'RNA Completed')

st.plotly_chart(rna_his_chart)

## Payment Completed Chart
pay_his_chart = px.histogram(df,
                   x = 'Month',
                   y = 'Payment Completed',
                   color='Application',
                   barmode='group',
                   title = 'Payment Completed')

st.plotly_chart(pay_his_chart)

## Other Applications

other_his_chart = px.histogram(df,
                   x = 'Month',
                   y = 'Leads Count',
                   color='Other_Application',
                   barmode='group',
                   title = 'Other Applications Lead Count')

st.plotly_chart(other_his_chart)

## Document Upload

doc_sheet_name = 'Document'

doc_df = pd.read_excel(excel_file,
                       doc_sheet_name,
                       usecols = 'A:D',
                       header = 0)

st.dataframe(doc_df)

## Document Upload Chart
doc_his_chart = px.histogram(doc_df,
                   x = 'Month',
                   y = 'Doc Uploaded',
                   color='Application',
                   barmode='group',
                   title = 'Document Upload')

st.plotly_chart(doc_his_chart)