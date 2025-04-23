import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CareerScope: Career Intelligence", layout="wide")

# ---- Mock Data ----

# Salary by Role & Industry
salary_data = pd.DataFrame({
    "Role": ["Data Scientist", "Software Engineer", "Product Manager", "Marketing Executive", "Mechanical Engineer"],
    "Industry": ["IT", "IT", "Tech", "Media", "Manufacturing"],
    "Average Salary (INR LPA)": [12.5, 9.0, 15.0, 6.5, 5.8]
})

# Course ROI
roi_data = pd.DataFrame({
    "Course": ["B.Tech CS", "MBA", "Data Science Bootcamp", "Digital Marketing Cert.", "Diploma in Mech. Engg."],
    "Duration (Months)": [48, 24, 6, 3, 36],
    "Fees (INR Lakh)": [6.0, 10.0, 1.5, 0.6, 2.5],
    "Avg Placement Salary (INR LPA)": [8.5, 12.0, 10.0, 5.0, 4.5]
})

# Job Demand by Skill
job_demand = pd.DataFrame({
    "Skill": ["Python", "Digital Marketing", "Excel", "SQL", "AI/ML", "Java", "Public Speaking"],
    "Monthly Job Postings": [9500, 6700, 5800, 6200, 4100, 5400, 3000]
})

# Hiring by Location
location_data = pd.DataFrame({
    "City": ["Bangalore", "Delhi", "Mumbai", "Hyderabad", "Pune", "Chennai", "Kolkata"],
    "Open Positions": [28000, 21000, 19000, 16000, 15000, 13000, 8000]
})

# ---- App Interface ----
st.title("📊 CareerScope – India's Career Intelligence Dashboard")
st.markdown("### For students & job seekers aged 16–30")

tabs = st.tabs(["💼 Salary Insights", "🎓 Course ROI", "📈 Skill Demand", "📍 Hiring by City"])

# Tab 1: Salary Insights
with tabs[0]:
    st.subheader("💼 Average Salary by Role and Industry")
    fig1 = px.bar(salary_data, x="Role", y="Average Salary (INR LPA)", color="Industry",
                  text="Average Salary (INR LPA)", height=500)
    st.plotly_chart(fig1, use_container_width=True)

# Tab 2: Course ROI
with tabs[1]:
    st.subheader("🎓 Course ROI – Fees vs Salary")
    fig2 = px.scatter(roi_data, x="Fees (INR Lakh)", y="Avg Placement Salary (INR LPA)",
                      size="Duration (Months)", color="Course", size_max=60,
                      hover_name="Course", height=500)
    st.plotly_chart(fig2, use_container_width=True)

# Tab 3: Skill Demand
with tabs[2]:
    st.subheader("📈 Job Demand by Skill")
    fig3 = px.bar(job_demand, x="Skill", y="Monthly Job Postings", color="Skill",
                  text="Monthly Job Postings", height=500)
    st.plotly_chart(fig3, use_container_width=True)

# Tab 4: Location-Based Hiring
with tabs[3]:
    st.subheader("📍 Hiring Demand by City")
    fig4 = px.pie(location_data, names="City", values="Open Positions", height=500)
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.caption("Built with ❤️ by Archit | Education Journalist | CareerScope Beta v0.1")
