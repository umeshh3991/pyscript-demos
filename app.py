import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="JIRA Issue Tracker")


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["JIRA Dashboard", "L3 Team", "Business Team", "DEV Team", "L2 Team", "Sprints" ])

excel_file = 'JIRA_Sheet.xlsx'
sheet_name = 'Filtered_JIRA_Sheet'
sheet_name_1 = "Priority Tasks"

JIRA_volume = pd.read_excel(excel_file,
                            sheet_name= sheet_name,
                            usecols = None,
                            header = 0
                            )

JIRA_priority_task_volume = pd.read_excel(excel_file,
                                          sheet_name= sheet_name_1,
                                          usecols = None,
                                          header = 0
                                         )

with tab1:

    st.header('Dashboard')
    
    # Load DataFrame

    #st.dataframe(JIRA_volume)
    
    jira_vol_counts = JIRA_volume['Status'].value_counts().reset_index()
    jira_vol_counts.columns = ['Status', 'Count']
    
    jira_vol_pie_chart = px.pie(
                                jira_vol_counts, 
                                names='Status',
                                values='Count',
                                title='Jira Issues Pie Chart'
                                )
    
    st.plotly_chart(jira_vol_pie_chart)
    

#L3 Team Tab

with tab2:
    
    tab7, tab8 = st.tabs(["Priority Tasks", "Other Pending Issues" ])
    
    with tab7:
        if 'Assignee' in JIRA_priority_task_volume.columns:
            L3_team_priority_issues = JIRA_priority_task_volume[(JIRA_priority_task_volume['Assignee'] == 'Hitesh Mishra') 
                                                                | (JIRA_priority_task_volume['Assignee'] == 'Virendra Minanath Arekar')]
            
        else:
            print('The column does not exist in excel file')
            
        L3_team_priority_assignee_filter = st.multiselect(
            "Select Assignee(s):",
            options=L3_team_priority_issues["Assignee"].unique(),
            default=L3_team_priority_issues["Assignee"].unique(),
            key="unique_key_1"
        )
        
        # Apply the filter
        L3_team_priority_filtered_df = L3_team_priority_issues[L3_team_priority_issues["Assignee"].isin(L3_team_priority_assignee_filter)]
        L3_team_priority_sorted_df = L3_team_priority_filtered_df.sort_values(by=['Priority Number'], ascending=[True])
        
        # Display the filtered DataFrame
        st.dataframe(L3_team_priority_sorted_df)
        
        number_of_results = L3_team_priority_filtered_df.shape[0]
        st.markdown(f'***Total Priority Issues: {number_of_results}***')
        
        L3_priority_issues_count = L3_team_priority_filtered_df['Status'].value_counts().reset_index()
        L3_priority_issues_count.columns = ['Status', 'Count']
        
        L3_priority_issues_pie_chart = px.pie(
                                            L3_priority_issues_count, 
                                            names='Status',
                                            values='Count',
                                            title='L3 Priority Issues Pie Chart'
                                          )
        
        st.plotly_chart(L3_priority_issues_pie_chart)
    
    with tab8:
        #st.dataframe(JIRA_volume)
        
        if 'Assignee' in JIRA_volume.columns:
            L3_team_issues = JIRA_volume[(JIRA_volume['Assignee'] == 'Hitesh Mishra') 
                                         | (JIRA_volume['Assignee'] == 'Virendra Minanath Arekar')]
            
            L3_team_open_issues = L3_team_issues[(L3_team_issues['Status'] == 'Open')]
            #st.dataframe(L3_team_issues)
            
        else:
            print('The column does not exist in excel file')
                                              
        L3_team_assignee_filter = st.multiselect(
            "Select Assignee(s):",
            options=L3_team_open_issues["Assignee"].unique(),
            default=L3_team_open_issues["Assignee"].unique(),
            key="unique_key_2"
        )
    
        # Apply the filter
        L3_team_filtered_df = L3_team_open_issues[L3_team_open_issues["Assignee"].isin(L3_team_assignee_filter)]
        L3_selected_columns = ["Issue Type", "Issue key", "Summary", "Reporter", "Severity", "Applications Affected", "Created"]
        L3_team_col_filtered_df = L3_team_filtered_df.loc[:, L3_selected_columns]
        L3_team_sorted_df = L3_team_col_filtered_df.sort_values(by=['Severity','Applications Affected', 'Created'], ascending=[True,False, True])
    
        # Display the filtered DataFrame
        st.dataframe(L3_team_sorted_df)
        
        number_of_results = L3_team_filtered_df.shape[0]
        st.markdown(f'***Total Open Issues: {number_of_results}***')
        
        L3_open_issues_count = L3_team_filtered_df['Severity'].value_counts().reset_index()
        L3_open_issues_count.columns = ['Severity', 'Count']
        
        L3_open_issues_pie_chart = px.pie(
                                            L3_open_issues_count, 
                                            names='Severity',
                                            values='Count',
                                            title='L3 Open Issues Pie Chart'
                                          )
        
        st.plotly_chart(L3_open_issues_pie_chart)
    
with tab3:
    
    tab9, tab10 = st.tabs(["Priority Tasks", "Other Pending Issues" ])
    
    with tab9:
        if 'Assignee' in JIRA_priority_task_volume.columns:
            buis_team_priority_issues = JIRA_priority_task_volume[(JIRA_priority_task_volume['Assignee'] == 'Sarthak Singh') 
                                                                | (JIRA_priority_task_volume['Assignee'] == 'Parth Thakkar')
                                                                | (JIRA_priority_task_volume['Assignee'] == 'KIRAN BHAAVAN MEHTA')
                                                                | (JIRA_priority_task_volume['Assignee'] == 'MaheshGundekar')
                                                                | (JIRA_priority_task_volume['Assignee'] == 'Abhay Kamath')]
            
        else:
            print('The column does not exist in excel file')
            
        buis_team_priority_assignee_filter = st.multiselect(
            "Select Assignee(s):",
            options=buis_team_priority_issues["Assignee"].unique(),
            default=buis_team_priority_issues["Assignee"].unique(),
            key="unique_key_3"
        )
        
        # Apply the filter
        buis_team_priority_filtered_df = buis_team_priority_issues[buis_team_priority_issues["Assignee"].isin(buis_team_priority_assignee_filter)]
        buis_team_priority_filtered_df = buis_team_priority_filtered_df.sort_values(by=['Priority Number'], ascending=[True])
        
        # Display the filtered DataFrame
        st.dataframe(buis_team_priority_filtered_df)
        
        number_of_results = buis_team_priority_filtered_df.shape[0]
        st.markdown(f'***Total Priority Issues: {number_of_results}***')
        
        buis_priority_issues_count = buis_team_priority_filtered_df['Status'].value_counts().reset_index()
        buis_priority_issues_count.columns = ['Status', 'Count']
        
        buis_priority_issues_pie_chart = px.pie(
                                            buis_priority_issues_count, 
                                            names='Status',
                                            values='Count',
                                            title='Business Team Priority Issues Pie Chart'
                                          )
        
        st.plotly_chart(buis_priority_issues_pie_chart)
    
    with tab10:
        #st.dataframe(JIRA_volume)
        
        if 'Assignee' in JIRA_volume.columns:
            buis_team_issues = JIRA_volume[(JIRA_volume['Assignee'] == 'Sarthak Singh') 
                                          | (JIRA_volume['Assignee'] == 'Parth Thakkar')
                                          | (JIRA_volume['Assignee'] == 'KIRAN BHAAVAN MEHTA')
                                          | (JIRA_volume['Assignee'] == 'MaheshGundekar')]
            
            buis_team_open_issues = buis_team_issues[(buis_team_issues['Status'] == 'Open')]
            #st.dataframe(buis_team_issues)
            
        else:
            print('The column does not exist in excel file')
                                              
        buis_team_assignee_filter = st.multiselect(
            "Select Assignee(s):",
            options=buis_team_open_issues["Assignee"].unique(),
            default=buis_team_open_issues["Assignee"].unique(),
            key="unique_key_4"
        )
    
        # Apply the filter
        buis_team_filtered_df = buis_team_open_issues[buis_team_open_issues["Assignee"].isin(buis_team_assignee_filter)]
        buis_selected_columns = ["Issue Type", "Issue key", "Summary", "Reporter", "Severity", "Applications Affected", "Created"]
        buis_team_col_filtered_df = buis_team_filtered_df.loc[:, buis_selected_columns]
        buis_team_sorted_df = buis_team_col_filtered_df.sort_values(by=['Severity','Applications Affected', 'Created'], ascending=[True, False, True])
    
        # Display the filtered DataFrame
        st.dataframe(buis_team_sorted_df)
        
        number_of_results = buis_team_filtered_df.shape[0]
        st.markdown(f'***Total Open Issues: {number_of_results}***')
        
        buis_open_issues_count = buis_team_filtered_df['Severity'].value_counts().reset_index()
        buis_open_issues_count.columns = ['Severity', 'Count']
        
        buis_open_issues_pie_chart = px.pie(
                                            buis_open_issues_count, 
                                            names='Severity',
                                            values='Count',
                                            title='Business Team Open Issues Pie Chart'
                                          )
        
        st.plotly_chart(buis_open_issues_pie_chart)
        
with tab4:
    
    tab11, tab12 = st.tabs(["Priority Tasks", "Other Pending Issues" ])
    
    with tab11:
        if 'Assignee' in JIRA_priority_task_volume.columns:
            dev_team_priority_issues = JIRA_priority_task_volume[(JIRA_priority_task_volume['Assignee'] == 'Atrik Shah') 
                                                                | (JIRA_priority_task_volume['Assignee'] == 'Sachin Pasi')
                                                                | (JIRA_priority_task_volume['Assignee'] == 'Aishwarya Anand')]
            
        else:
            print('The column does not exist in excel file')
            
        dev_team_priority_assignee_filter = st.multiselect(
            "Select Assignee(s):",
            options=dev_team_priority_issues["Assignee"].unique(),
            default=dev_team_priority_issues["Assignee"].unique(),
            key="unique_key_5"
        )
        
        # Apply the filter
        dev_team_priority_filtered_df = dev_team_priority_issues[dev_team_priority_issues["Assignee"].isin(dev_team_priority_assignee_filter)]
        dev_team_priority_filtered_df = dev_team_priority_filtered_df.sort_values(by=['Priority Number'], ascending=[True])
        
        # Display the filtered DataFrame
        st.dataframe(dev_team_priority_filtered_df)
        
        number_of_results = dev_team_priority_filtered_df.shape[0]
        st.markdown(f'***Total Priority Issues: {number_of_results}***')
        
        dev_priority_issues_count = dev_team_priority_filtered_df['Status'].value_counts().reset_index()
        dev_priority_issues_count.columns = ['Status', 'Count']
        
        dev_priority_issues_pie_chart = px.pie(
                                            dev_priority_issues_count, 
                                            names='Status',
                                            values='Count',
                                            title='Business Team Priority Issues Pie Chart'
                                          )
        
        st.plotly_chart(dev_priority_issues_pie_chart)
    
    with tab12:
        #st.dataframe(JIRA_volume)
        
        if 'Assignee' in JIRA_volume.columns:
            dev_team_issues = JIRA_volume[(JIRA_volume['Assignee'] == 'Atrik Shah') 
                                          | (JIRA_volume['Assignee'] == 'Sachin Pasi')
                                          | (JIRA_volume['Assignee'] == 'Aishwarya Anand')]
            
            dev_team_open_issues = dev_team_issues[(dev_team_issues['Status'] == 'Open')]
            #st.dataframe(dev_team_issues)
            
        else:
            print('The column does not exist in excel file')
                                              
        dev_team_assignee_filter = st.multiselect(
            "Select Assignee(s):",
            options=dev_team_open_issues["Assignee"].unique(),
            default=dev_team_open_issues["Assignee"].unique(),
            key="unique_key_6"
        )
    
        # Apply the filter
        dev_team_filtered_df = dev_team_open_issues[dev_team_open_issues["Assignee"].isin(dev_team_assignee_filter)]
        dev_selected_columns = ["Issue Type", "Issue key", "Summary", "Reporter", "Severity", "Applications Affected", "Created"]
        dev_team_col_filtered_df = dev_team_filtered_df.loc[:, dev_selected_columns]
        dev_team_sorted_df = dev_team_col_filtered_df.sort_values(by=['Severity','Applications Affected', 'Created'], ascending=[True, False, True])
    
        # Display the filtered DataFrame
        st.dataframe(dev_team_sorted_df)
        
        number_of_results = dev_team_filtered_df.shape[0]
        st.markdown(f'***Total Open Issues: {number_of_results}***')
        
        dev_open_issues_count = dev_team_filtered_df['Severity'].value_counts().reset_index()
        dev_open_issues_count.columns = ['Severity', 'Count']
        
        dev_open_issues_pie_chart = px.pie(
                                            dev_open_issues_count, 
                                            names='Severity',
                                            values='Count',
                                            title='Development Team Open Issues Pie Chart'
                                          )
        
        st.plotly_chart(dev_open_issues_pie_chart)
        
with tab5:
    
    tab13, tab14 = st.tabs(["Priority Tasks", "Other Pending Issues" ])
    
    with tab13:
        if 'Assignee' in JIRA_priority_task_volume.columns:
            L2_team_priority_issues = JIRA_priority_task_volume[(JIRA_priority_task_volume['Assignee'] == 'Mithila Ajit Sawant') 
                                                                | (JIRA_priority_task_volume['Assignee'] == 'Rakesh Yadav')
                                                                | (JIRA_priority_task_volume['Assignee'] == 'Umesh Gupta')
                                                                | (JIRA_priority_task_volume['Assignee'] == 'sushant joshi')
                                                                | (JIRA_priority_task_volume['Assignee'] == 'Vikas Yadav')
                                                                | (JIRA_priority_task_volume['Assignee'] == 'Sagar Rathod')
                                                                | (JIRA_priority_task_volume['Assignee'] == 'Rahul.Rajbhar2')]
            
        else:
            print('The column does not exist in excel file')
            
        L2_team_priority_assignee_filter = st.multiselect(
            "Select Assignee(s):",
            options=L2_team_priority_issues["Assignee"].unique(),
            default=L2_team_priority_issues["Assignee"].unique(),
            key="unique_key_7"
        )
        
        # Apply the filter
        L2_team_priority_filtered_df = L2_team_priority_issues[L2_team_priority_issues["Assignee"].isin(L2_team_priority_assignee_filter)]
        L2_team_priority_filtered_df = L2_team_priority_filtered_df.sort_values(by=['Priority Number'], ascending=[True])
        
        # Display the filtered DataFrame
        st.dataframe(L2_team_priority_filtered_df)
        
        number_of_results = L2_team_priority_filtered_df.shape[0]
        st.markdown(f'***Total Priority Issues: {number_of_results}***')
        
        L2_priority_issues_count = L2_team_priority_filtered_df['Status'].value_counts().reset_index()
        L2_priority_issues_count.columns = ['Status', 'Count']
        
        L2_priority_issues_pie_chart = px.pie(
                                            L2_priority_issues_count, 
                                            names='Status',
                                            values='Count',
                                            title='L2 Team Priority Issues Pie Chart'
                                          )
        
        st.plotly_chart(L2_priority_issues_pie_chart)
    
    with tab14:
        #st.dataframe(JIRA_volume)
        
        if 'Assignee' in JIRA_volume.columns:
            L2_team_issues = JIRA_volume[(JIRA_volume['Assignee'] == 'Mithila Ajit Sawant')
                                         | (JIRA_volume['Assignee'] == 'Rakesh Yadav')
                                         | (JIRA_volume['Assignee'] == 'Umesh Gupta')
                                         | (JIRA_volume['Assignee'] == 'sushant joshi')
                                         | (JIRA_volume['Assignee'] == 'Vikas Yadav')
                                         | (JIRA_volume['Assignee'] == 'Sagar Rathod')
                                         | (JIRA_volume['Assignee'] == 'Rahul.Rajbhar2')]

            
            L2_team_open_issues = L2_team_issues[(L2_team_issues['Status'] == 'Open')]
            #st.dataframe(L2_team_issues)
            
        else:
            print('The column does not exist in excel file')
                                              
        L2_team_assignee_filter = st.multiselect(
            "Select Assignee(s):",
            options=L2_team_open_issues["Assignee"].unique(),
            default=L2_team_open_issues["Assignee"].unique(),
            key="unique_key_8"
        )
    
        # Apply the filter
        L2_team_filtered_df = L2_team_open_issues[L2_team_open_issues["Assignee"].isin(L2_team_assignee_filter)]
        L2_selected_columns = ["Issue Type", "Issue key", "Summary", "Reporter", "Severity", "Applications Affected", "Created"]
        L2_team_col_filtered_df = L2_team_filtered_df.loc[:, L2_selected_columns]
        L2_team_sorted_df = L2_team_col_filtered_df.sort_values(by=['Severity','Applications Affected', 'Created'], ascending=[True, False, True])
    
        # Display the filtered DataFrame
        st.dataframe(L2_team_sorted_df)
        
        number_of_results = L2_team_filtered_df.shape[0]
        st.markdown(f'***Total Open Issues: {number_of_results}***')
        
        L2_open_issues_count = L2_team_filtered_df['Severity'].value_counts().reset_index()
        L2_open_issues_count.columns = ['Severity', 'Count']
        
        L2_open_issues_pie_chart = px.pie(
                                            L2_open_issues_count, 
                                            names='Severity',
                                            values='Count',
                                            title='L2 Team Open Issues Pie Chart'
                                          )
        
        st.plotly_chart(L2_open_issues_pie_chart)     