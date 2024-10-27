import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Dashboard")
st.header('Leap Uptime Dashboard 2024')
st.subheader('Monthly Volume')

# Add a simple example
#st.write("Welcome to the LEAP Uptime Dashboard for Year 2024")

# Load DataFrame
excel_file = 'Sample.xlsx'
sheet_name = 'Monthly_Volume'

monthly_volume = pd.read_excel(excel_file,
                   sheet_name,
                   usecols = 'A:N',
                   header = 0)

st.dataframe(monthly_volume)

#application = df['Application'].unique().tolist()
#application_selection = st.multiselect('Application:',
#                                        application,
#                                        default=application)

#mask = df['Application'].isin(application_selection)
#number_of_results = df[mask].shape[0]
#st.markdown(f'*Available Results : {number_of_results}*')


## Application Created Chart
app_his_chart = px.histogram(monthly_volume,
                   x = 'Month',
                   y = 'Applications Created',
                   color='Application',
                   barmode='group',
                   title = 'Applications Created')

st.plotly_chart(app_his_chart)

## RNA Completed Chart
rna_his_chart = px.histogram(monthly_volume,
                   x = 'Month',
                   y = 'RNA Completed',
                   color='Application',
                   barmode='group',
                   title = 'RNA Completed')

st.plotly_chart(rna_his_chart)

## Payment Completed Chart
pay_his_chart = px.histogram(monthly_volume,
                   x = 'Month',
                   y = 'Payment Completed',
                   color='Application',
                   barmode='group',
                   title = 'Payment Completed')

st.plotly_chart(pay_his_chart)

## Other Applications

other_his_chart = px.histogram(monthly_volume,
                   x = 'Month',
                   y = 'Leads Count',
                   color='Other_Application',
                   barmode='group',
                   title = 'Other Applications Lead Count')

st.plotly_chart(other_his_chart)

## Document Upload

##doc_sheet_name = 'Document'

## doc_df = pd.read_excel(excel_file,
##                      monthly_volume,
##                       usecols = 'A:D',
##                       header = 0)

##st.dataframe(doc_df)

## Document Upload Chart
doc_his_chart = px.histogram(monthly_volume,
                   x = 'Doc_Month',
                   y = 'Doc Uploaded',
                   color='Doc Application',
                   barmode='group',
                   title = 'Document Upload')

st.plotly_chart(doc_his_chart)

## Daily Volume and Uptime Trend

st.subheader('Current Month Daily Volume and Uptime Trend')

uptime_sheet_name = 'EApp MTD Uptime Trend'

uptime_df = pd.read_excel(excel_file,
                       uptime_sheet_name,
                       usecols = 'A:AC',
                       header = 0)

st.dataframe(uptime_df)

col1, col2 = st.columns(2)

## EApp/MApp Uptime Chart

with col1:
    eapp_uptime_bar_chart = px.bar(uptime_df, x='Date', y='EApp/MApp Daily Volume', title='EApp/MApp')
    eapp_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(eapp_uptime_bar_chart)

with col2:
    eapp_uptime_line_chart = px.line(uptime_df, x='Date', y='EApp/MApp Production UpTime', title='EApp/MApp')
    st.plotly_chart(eapp_uptime_line_chart)


## EApp D2C Uptime Chart

col3, col4 = st.columns(2)

with col3:
    d2c_uptime_bar_chart = px.bar(uptime_df, x='Date', y='EAppD2C Daily Volume', title='EApp D2C')
    
    d2c_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(d2c_uptime_bar_chart)

with col4:
    d2c_uptime_line_chart = px.line(uptime_df, x='Date', y='EAppD2C Production UpTime', title='EApp D2C')
    st.plotly_chart(d2c_uptime_line_chart)


## LMS Uptime Chart

col5, col6 = st.columns(2)

with col5:
    lms_uptime_bar_chart = px.bar(uptime_df, x='Date', y='LMS Daily Volume', title='Lead Flow')
    lms_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(lms_uptime_bar_chart)

with col6:
    lms_uptime_line_chart = px.line(uptime_df, x='Date', y='LMS Production UpTime', title='Lead Flow')
    st.plotly_chart(lms_uptime_line_chart)


## Insta Verify Uptime Chart

col7, col8 = st.columns(2)

with col7:
    insta_uptime_bar_chart = px.bar(uptime_df, x='Date', y='Insta Verify Daily Volume', title='InstaVerify')
    insta_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(insta_uptime_bar_chart)

with col8:
    insta_uptime_line_chart = px.line(uptime_df, x='Date', y='Insta Verify Production UpTime', title='InstaVerify')
    st.plotly_chart(insta_uptime_line_chart)

## Sales Buddy Uptime Chart

col9, col10 = st.columns(2)

with col9:
    sales_buddy_uptime_bar_chart = px.bar(uptime_df, x='Date', y='Sales Buddy Daily Volume', title='Sales Buddy')
    sales_buddy_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(sales_buddy_uptime_bar_chart)

with col10:
    sales_uptime_line_chart = px.line(uptime_df, x='Date', y='Sales Buddy Production UpTime', title='Sales Buddy')
    st.plotly_chart(sales_uptime_line_chart)


## Service Buddy Uptime Chart

col11, col12 = st.columns(2)

with col11:
    service_buddy_uptime_bar_chart = px.bar(uptime_df, x='Date', y='Service Buddy Daily Volume', title='Service Buddy')
    service_buddy_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(service_buddy_uptime_bar_chart)

with col12:
    service_buddy_uptime_line_chart = px.line(uptime_df, x='Date', y='Service Buddy Production UpTime', title='Service Buddy')
    st.plotly_chart(service_buddy_uptime_line_chart)

## LEAP Uptime Chart

col13, col14 = st.columns(2)

with col13:
    leap_uptime_bar_chart = px.bar(uptime_df, x='Date', y='Leap Daily Volume', title='LEAP')
    leap_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(leap_uptime_bar_chart)

with col14:
    leap_uptime_line_chart = px.line(uptime_df, x='Date', y='Leap Production UpTime', title='LEAP')
    st.plotly_chart(leap_uptime_line_chart)


## MTD Application Uptime Trend

st.subheader('Current Month MTD Application Uptime Trend')

mtd_uptime_df = pd.read_excel(excel_file,
                       uptime_sheet_name,
                       usecols = 'AE:AG',
                       header = 0)

st.dataframe(mtd_uptime_df)

# MTD Application Uptime Chart

mtd_uptime_his_chart = px.histogram(mtd_uptime_df,
                       x = 'Application',
                       y = 'Values',
                       color='Production UpTime/ Production DownTime',
                       barmode='group',
                       title = 'MTD Application Uptime')

st.plotly_chart(mtd_uptime_his_chart)

## Daily Channel Wise UpTime

st.subheader('Current Month Daily Channel Wise Uptime Trend')

channel_sheet_name = 'Channel'

channel_uptime_df = pd.read_excel(excel_file,
                       channel_sheet_name,
                       usecols = 'A:C',
                       header = 0)

st.dataframe(channel_uptime_df)

channel_uptime_his_chart = px.histogram(channel_uptime_df,
                           x = 'Channel Name',
                           y = 'Values',
                           color='Production UpTime/ Production DownTime',
                           barmode='group',
                           title = 'Daily Channel Wise UpTime')

st.plotly_chart(channel_uptime_his_chart)