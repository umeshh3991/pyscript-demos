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

## EApp MTD Uptime Trend 

uptime_sheet_name = 'EApp MTD Uptime Trend'

uptime_df = pd.read_excel(excel_file,
                       uptime_sheet_name,
                       usecols = 'A:AC',
                       header = 0)

st.dataframe(uptime_df)

## EApp/MApp Uptime Chart

eapp_uptime_bar_chart = px.bar(uptime_df, x='Date', y='EApp/MApp Daily Volume', title='EApp/MApp Uptime & Volume Trend')
eapp_uptime_bar_chart.update_xaxes(tickangle=90)

st.plotly_chart(eapp_uptime_bar_chart)


## EApp D2C Uptime Chart

d2c_uptime_bar_chart = px.bar(uptime_df, x='Date', y='EAppD2C Daily Volume', title='EApp D2C Uptime & Volume Trend')
d2c_uptime_bar_chart.update_xaxes(tickangle=90)

st.plotly_chart(d2c_uptime_bar_chart)


## LMS Uptime Chart

lms_uptime_bar_chart = px.bar(uptime_df, x='Date', y='LMS Daily Volume', title='Lead Flow Uptime & Volume Trend')
lms_uptime_bar_chart.update_xaxes(tickangle=90)

st.plotly_chart(lms_uptime_bar_chart)


## Insta Verify Uptime Chart

insta_uptime_bar_chart = px.bar(uptime_df, x='Date', y='Insta Verify Daily Volume', title='InstaVerify Uptime & Volume Trend ')
insta_uptime_bar_chart.update_xaxes(tickangle=90)

st.plotly_chart(insta_uptime_bar_chart)



## Sales Buddy Uptime Chart

sales_buddy_uptime_bar_chart = px.bar(uptime_df, x='Date', y='Sales Buddy Daily Volume', title='Sales Buddy Uptime & Volume Trend')
sales_buddy_uptime_bar_chart.update_xaxes(tickangle=90)

st.plotly_chart(sales_buddy_uptime_bar_chart)


## Service Buddy Uptime Chart

service_buddy_uptime_bar_chart = px.bar(uptime_df, x='Date', y='Service Buddy Daily Volume', title='Service Buddy Uptime & Volume Trend')
service_buddy_uptime_bar_chart.update_xaxes(tickangle=90)

st.plotly_chart(service_buddy_uptime_bar_chart)



## LEAP Uptime Chart

leap_uptime_bar_chart = px.bar(uptime_df, x='Date', y='Leap Daily Volume', title='Leap Uptime & Volume Trend')
leap_uptime_bar_chart.update_xaxes(tickangle=90)

st.plotly_chart(leap_uptime_bar_chart)