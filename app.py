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
                   usecols = 'A:G',
                   header = 0)

#st.dataframe(monthly_volume)

month = monthly_volume['Month_Num'].unique().tolist()

selected_option = st.slider(
                  "Month: ",
                  min_value=min(month),
                  max_value=max(month),
                  value=(min(month),max(month))
)

mask = (monthly_volume['Month_Num'].between(*selected_option))
#number_of_results = monthly_volume[mask].shape[0]
#st.markdown(f'*Available Results: {number_of_results}*')

monthly_volume_grouped = monthly_volume[mask].groupby(by=['Month','Application','Applications Created','RNA Completed','Payment Completed','Doc Uploaded']).count()[['Month_Num']]
monthly_volume_grouped = monthly_volume_grouped.rename(columns = {'Month': 'Applications Created'})
monthly_volume_grouped = monthly_volume_grouped.reset_index()   

app_his_chart = px.histogram(monthly_volume_grouped,
                             x = 'Month',
                             y = 'Applications Created',
                             color='Application',
                             color_discrete_sequence=['aquamarine','teal','lightgreen'],
                             barmode='group',
                             title='Applications Created',
                             text_auto=True
                             )

app_his_chart.update_traces(texttemplate='%{y:,.0f}',textfont_size=12, textangle=0, textposition="outside")

app_his_chart.update_layout(yaxis_title="Applications Created")
app_his_chart.update_xaxes(categoryorder='array', categoryarray= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

st.plotly_chart(app_his_chart)

## RNA Completed Chart
rna_his_chart = px.histogram(monthly_volume_grouped,
                   x = 'Month',
                   y = 'RNA Completed',
                   color='Application',
                   color_discrete_sequence=['aquamarine','teal','lightgreen'],
                   barmode='group',
                   title = 'RNA Completed',
                   text_auto=True
                   )

rna_his_chart.update_traces(texttemplate='%{y:,.0f}',textfont_size=12, textangle=0, textposition="outside")

rna_his_chart.update_layout(yaxis_title="RNA Completed")
rna_his_chart.update_xaxes(categoryorder='array', categoryarray= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

st.plotly_chart(rna_his_chart)

## Payment Completed Chart
pay_his_chart = px.histogram(monthly_volume_grouped,
                   x = 'Month',
                   y = 'Payment Completed',
                   color='Application',
                   color_discrete_sequence=['aquamarine','teal','lightgreen'],
                   barmode='group',
                   title = 'Payment Completed',
                   text_auto=True
                   )

pay_his_chart.update_traces(texttemplate='%{y:,.0f}',textfont_size=12, textangle=0, textposition="outside")

pay_his_chart.update_layout(yaxis_title="Payment Completed")
pay_his_chart.update_xaxes(categoryorder='array', categoryarray= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

st.plotly_chart(pay_his_chart)

## Document Upload Chart
doc_his_chart = px.histogram(monthly_volume_grouped,
                   x = 'Month',
                   y = 'Doc Uploaded',
                   color='Application',
                   color_discrete_sequence=['aquamarine','teal','lightgreen'],
                   barmode='group',
                   title = 'Document Upload',
                   text_auto=True
                   )

doc_his_chart.update_traces(texttemplate='%{y:,.0f}',textfont_size=12, textangle=0, textposition="outside")

doc_his_chart.update_layout(yaxis_title="Document Uploaded")
doc_his_chart.update_xaxes(categoryorder='array', categoryarray= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

st.plotly_chart(doc_his_chart)

## Other Applications

sheet_name_1 = 'Other_App_Monthly_Volume'

other_app_monthly_volume = pd.read_excel(excel_file,
                                     sheet_name_1,
                                     usecols = 'A:D',
                                     header = 0)


other_app_month = other_app_monthly_volume['Other_App_Month_Num'].unique().tolist()

other_app_selected_option = st.slider(
                                      "Month: ",
                                      min_value=min(other_app_month),
                                      max_value=max(other_app_month),
                                      value=(min(other_app_month),max(other_app_month)),
                                      key= 'unique_key_2',
)

other_app_mask = (other_app_monthly_volume['Other_App_Month_Num'].between(*other_app_selected_option))

other_app_monthly_volume['Other_Application'] = other_app_monthly_volume['Other_Application'].replace({
    'LEAD': 'LEAD CRM',
    'InstaVerify': 'PIVC Done',
    'Sales Buddy': 'Sales Buddy Illustration'
})


other_app_monthly_volume_grouped = other_app_monthly_volume[other_app_mask].groupby(by=['Other App Month','Other_Application','Leads Count']).count()[['Other_App_Month_Num']]
other_app_monthly_volume_grouped = other_app_monthly_volume_grouped.rename(columns = {'Other App Month': 'Leads Count'})
other_app_monthly_volume_grouped = other_app_monthly_volume_grouped.reset_index()

other_his_chart = px.histogram(other_app_monthly_volume_grouped,
                   x = 'Other App Month',
                   y = 'Leads Count',
                   color='Other_Application',
                   color_discrete_sequence=['khaki','gold','deepskyblue'],
                   barmode='group',
                   title = 'Other Applications Details',
                   text_auto=True
                   )

other_his_chart.update_traces(texttemplate='%{y:,.0f}',textfont_size=10, textangle=0, textposition="outside")

other_his_chart.update_layout(yaxis_title="Values")
other_his_chart.update_layout(xaxis_title="Month")
other_his_chart.update_xaxes(categoryorder='array', categoryarray= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

st.plotly_chart(other_his_chart)

## Daily Volume and Uptime Trend

st.subheader('Daily Volume and Uptime Trend')

uptime_sheet_name = 'EApp MTD Uptime Trend'

uptime_df = pd.read_excel(excel_file,
                       uptime_sheet_name,
                       usecols = 'A:AH',
                       header = 0)

#st.dataframe(uptime_df)

month_uptime = uptime_df['Month'].unique().tolist()

selected_month = st.selectbox(
                  "Select a Month: ",
                  month_uptime,
                  index=len(month_uptime) - 1
)

filtered_data = uptime_df[uptime_df['Month'] == selected_month]

## LEAP Uptime Chart

col13, col14 = st.columns(2)

with col13:
    leap_uptime_bar_chart = px.bar(filtered_data, x='Date', y='Leap Daily Volume', title=f'LEAP Daily Volume for {selected_month}', text_auto=True)
    leap_uptime_bar_chart.update_traces(texttemplate='%{y:,.0f}',textfont_size=12, textangle=0, textposition="outside")
    leap_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(leap_uptime_bar_chart)

with col14:
    leap_uptime_line_chart = px.line(filtered_data, x='Date', y='Leap Production UpTime', title=f'LEAP Uptime Graph for {selected_month}')
    st.plotly_chart(leap_uptime_line_chart)

## EApp/MApp Uptime Chart

col1, col2 = st.columns(2)

with col1:
    eapp_uptime_bar_chart = px.bar(filtered_data, x='Date', y='EApp/MApp Daily Volume', title=f'EApp/MApp Daily Volume for {selected_month}', text_auto=True)
    eapp_uptime_bar_chart.update_traces(texttemplate='%{y:,.0f}',textfont_size=12, textangle=0, textposition="outside")
    eapp_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(eapp_uptime_bar_chart)

with col2:
    eapp_uptime_line_chart = px.line(filtered_data, x='Date', y='EApp/MApp Production UpTime', title=f'EApp/MApp Uptime Graph for {selected_month}')
    st.plotly_chart(eapp_uptime_line_chart)


## EApp D2C Uptime Chart

col3, col4 = st.columns(2)

with col3:
    d2c_uptime_bar_chart = px.bar(filtered_data, x='Date', y='EAppD2C Daily Volume', title=f'EApp D2C Daily Volume for {selected_month}', text_auto=True)
    d2c_uptime_bar_chart.update_traces(texttemplate='%{y:,.0f}',textfont_size=12, textangle=0, textposition="outside")
    d2c_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(d2c_uptime_bar_chart)

with col4:
    d2c_uptime_line_chart = px.line(filtered_data, x='Date', y='EAppD2C Production UpTime', title=f'EApp D2C Uptime Graph for {selected_month}')
    st.plotly_chart(d2c_uptime_line_chart)


## LMS Uptime Chart

col5, col6 = st.columns(2)

with col5:
    lms_uptime_bar_chart = px.bar(filtered_data, x='Date', y='LMS Daily Volume', title=f'Lead Flow Daily Volume for {selected_month}', text_auto=True)
    lms_uptime_bar_chart.update_traces(texttemplate='%{y:,.0f}',textfont_size=12, textangle=0, textposition="outside")
    lms_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(lms_uptime_bar_chart)

with col6:
    lms_uptime_line_chart = px.line(filtered_data, x='Date', y='LMS Production UpTime', title=f'Lead Flow Uptime Graph for {selected_month}')
    st.plotly_chart(lms_uptime_line_chart)


## Insta Verify Uptime Chart

col7, col8 = st.columns(2)

with col7:
    insta_uptime_bar_chart = px.bar(filtered_data, x='Date', y='Insta Verify Daily Volume', title=f'InstaVerify Daily Volume for {selected_month}', text_auto=True)
    insta_uptime_bar_chart.update_traces(texttemplate='%{y:,.0f}',textfont_size=12, textangle=0, textposition="outside")
    insta_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(insta_uptime_bar_chart)

with col8:
    insta_uptime_line_chart = px.line(filtered_data, x='Date', y='Insta Verify Production UpTime', title=f'InstaVerify Uptime Graph for {selected_month}')
    st.plotly_chart(insta_uptime_line_chart)

## Sales Buddy Uptime Chart

col9, col10 = st.columns(2)

with col9:
    sales_buddy_uptime_bar_chart = px.bar(filtered_data, x='Date', y='Sales Buddy Daily Volume', title=f'Sales Buddy Daily Volume for {selected_month}', text_auto=True)
    sales_buddy_uptime_bar_chart.update_traces(texttemplate='%{y:,.0f}',textfont_size=12, textangle=0, textposition="outside")
    sales_buddy_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(sales_buddy_uptime_bar_chart)

with col10:
    sales_uptime_line_chart = px.line(filtered_data, x='Date', y='Sales Buddy Production UpTime', title=f'Sales Buddy Uptime Graph for {selected_month}')
    st.plotly_chart(sales_uptime_line_chart)


## Service Buddy Uptime Chart

col11, col12 = st.columns(2)

with col11:
    service_buddy_uptime_bar_chart = px.bar(filtered_data, x='Date', y='Service Buddy Daily Volume', title=f'Service Buddy Daily Volume for {selected_month}', text_auto=True)
    service_buddy_uptime_bar_chart.update_traces(texttemplate='%{y:,.0f}',textfont_size=12, textangle=0, textposition="outside")
    service_buddy_uptime_bar_chart.update_xaxes(tickangle=90)

    st.plotly_chart(service_buddy_uptime_bar_chart)

with col12:
    service_buddy_uptime_line_chart = px.line(filtered_data, x='Date', y='Service Buddy Production UpTime', title=f'Service Buddy Uptime Graph for {selected_month}')
    st.plotly_chart(service_buddy_uptime_line_chart)

## MTD Application Uptime Trend

st.subheader('MTD Application Uptime Trend')

#st.dataframe(mtd_uptime_df)

# MTD Application Uptime Chart

mtd_uptime_his_chart = px.histogram(filtered_data,
                       x = 'Application',
                       y = 'Values',
                       color='Production UpTime/ Production DownTime',
                       facet_col='Month',
                       color_discrete_sequence=['green','red'],
                       barmode='group',
                       title = f'MTD Application Uptime for {selected_month}',
                       text_auto=True
                       )

mtd_uptime_his_chart.update_traces(texttemplate='%{y:,.0f}',textfont_size=12, textangle=0, textposition="outside")

mtd_uptime_his_chart.update_layout(yaxis_title="Production Uptime and Downtime")

st.plotly_chart(mtd_uptime_his_chart)