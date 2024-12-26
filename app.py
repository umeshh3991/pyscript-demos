import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="JIRA Issue Tracker")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["JIRA Dashboard", "L3 Team", "Business Team", "DEV Team", "L2 Team", "Sprints" ])

excel_file = 'JIRA_Sheet.xlsx'
sheet_name = 'JIRA_Sheet'
JIRA_volume = pd.read_excel(excel_file,
                            sheet_name,
                            usecols = 'A:R',
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
    
    #st.dataframe(JIRA_volume)
    
    if 'Assignee' in JIRA_volume.columns:
        L3_team_issues = JIRA_volume[(JIRA_volume['Assignee'] == 'Hitesh Mishra') | (JIRA_volume['Assignee'] == 'Virendra Minanath Arekar')]
        L3_team_open_issues = L3_team_issues[(L3_team_issues['Status'] == 'Open')]
        #st.dataframe(L3_team_issues)
        
    else:
        print('The column does not exist in excel file')
        
        
    L3_team_assignee_filter = st.multiselect(
                                            "Select Assignee(s):", options=L3_team_open_issues["Assignee"].unique(), default=L3_team_open_issues["Assignee"].unique()
                                            )

    # Apply the filter
    L3_team_filtered_df = L3_team_open_issues[L3_team_open_issues["Assignee"].isin(L3_team_assignee_filter)]

    # Display the filtered DataFrame
    st.dataframe(L3_team_filtered_df)
    
    mask = (L3_team_filtered_df['Assignee'].between(*L3_team_assignee_filter))
    number_of_results = L3_team_filtered_df[mask].shape[0]
    st.markdown(f'***Available Results: {number_of_results}***')
    
    L3_open_issues_count = L3_team_filtered_df['Custom field (Severity).1'].value_counts().reset_index()
    L3_open_issues_count.columns = ['Custom field (Severity).1', 'Count']
    
    L3_open_issues_pie_chart = px.pie(
                                        L3_open_issues_count, 
                                        names='Custom field (Severity).1',
                                        values='Count',
                                        title='L3 Open Issues Pie Chart'
                                      )
    
    st.plotly_chart(L3_open_issues_pie_chart)
    

     