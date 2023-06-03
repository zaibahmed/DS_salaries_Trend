import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st


st.set_page_config(layout='wide')


#path = r'C:\Users\TOSHIBA\Downloads\ds_salaries.csv'
data = pd.read_csv(ds_salaries.csv)

col1, col2,col3 = st.columns([4,1,1])

with col1:
    st.title('Data Scientist Salary Trend Dashboard')
    

yearly_top_salaries = data.groupby('work_year').apply(lambda x: x.loc[x['salary_in_usd'].idxmax()])
kpi1 = yearly_top_salaries['salary_in_usd'].max()
kpi2 = yearly_top_salaries['salary_in_usd'].mean()


with col2:
    st.info("Max-Salary [In USD]")
    st.write(kpi1)

with col3:
    st.info("Avg-Salary [In USD]")
    st.write(kpi2)



job_titles = data['job_title'].unique()
selected_job_title = st.selectbox("Select Job Title", job_titles)
subset = data[data['job_title'] == selected_job_title]



col1,col2,col3=st.columns(3)


with col1:
    median_salary_by_experience = subset.groupby('experience_level')['salary_in_usd'].median()
    sorted_exprience_level = median_salary_by_experience.index.sort_values()
    colors = ['blue', 'green', 'red', 'orange', 'purple']
    plt.figure(figsize=(10, 8.5),facecolor='lightgray')
    plt.bar(sorted_exprience_level,median_salary_by_experience , color = colors)
    plt.xlabel('Experience Level', fontsize=20)
    plt.ylabel('Median Salary (in USD)', fontsize=20)
    plt.title('Salary variation by Experience Level ', fontsize=20)
    plt.xticks(rotation=45, fontsize=20)
    plt.yticks(fontsize=20)
    st.pyplot(plt)    


with col2:
    employment_type_counts = subset['employment_type'].value_counts()
    plt.figure(figsize=(10, 8.05),facecolor='lightgray')
    outer_colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
    inner_colors = ['white']
    wedges, text, autotext = plt.pie(employment_type_counts, labels=None, autopct='%1.1f%%', startangle=90, pctdistance=0.85, colors=outer_colors, wedgeprops=dict(edgecolor='white'))
    plt.setp(autotext, size=15, weight='bold')
    plt.setp(text, size=15)
    plt.title('Distribution of Employment Types', fontsize=18)
    center_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    plt.legend(wedges, employment_type_counts.index, loc='best', title='Employment Type', fontsize=12)
    plt.axis('equal')
    st.pyplot(plt)


with col3:
    subset['Region'] = subset['company_location'].str.extract(r'([A-Za-z\s]+)')
    location_counts = subset['Region'].value_counts()
    top_10_locations = location_counts.head(10) 
    plt.figure(figsize=(10,7.9),facecolor='lightgray')
    plt.bar(top_10_locations.index, top_10_locations)
    plt.xlabel('Region',fontsize=20)
    plt.ylabel('Count',fontsize=20)
    plt.title('Top 10 Geographical Distribution of Company Locations',fontsize=20)
    plt.xticks(rotation=45,fontsize=20)
    plt.yticks(fontsize=20)
    st.pyplot(plt)


col1,col2=st.columns([1, 2.5])

with col1:
    Highest_paid_salary = data.groupby('job_title')['salary_in_usd'].max()
    Highest_paid_salary_sorted_desc = Highest_paid_salary.sort_values(ascending=False)
    st.markdown("#### Maximum Salary A/C Job Title")
    st.write(Highest_paid_salary_sorted_desc.head(5))


with col2:
    salary_by_job_title = data.groupby('job_title')['salary_in_usd'].mean()
    top_job_title = salary_by_job_title.sort_values(ascending=True).head(10)
    colors = plt.cm.Set3(np.linspace(0, 1, len(top_job_title)))
    plt.figure(figsize=(8,3),facecolor='lightgray')
    plt.barh(top_job_title.index, top_job_title, color = colors)
    plt.xlabel('Average Salary')
    plt.ylabel('Job Title')
    plt.title('Top job titles with highest Salaries')
    st.pyplot(plt)

















