import streamlit as st
import requests
import plotly.express as px
import pandas as pd
import random
import string

def show_dashboard():
    st.title("🚀 Smart Complaint Analyzer")
    st.subheader("Admin Dashboard")

    response = requests.get(
        "http://127.0.0.1:8000/stats"
    )

    stats = response.json()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Complaints", stats["Total"])

    with col2:
        st.metric("Pending", stats["Pending"])

    with col3:
        st.metric("Resolved", stats["Resolved"])

    with col4:
        st.metric("Rejected", stats["Rejected"])
    
    
    category_data = {
        "Health": stats["Health"],
        "Safety": stats["Safety"],
        "Transport": stats["Transport"],
        "Roads": stats["Roads"],
        "Water": stats["Water"],
        "Electricity": stats["Electricity"],
        "Other": stats["Other"]
    }

    category_fig = px.pie(
        names=list(category_data.keys()),
        values=list(category_data.values()),
        title="Complaints by Category",
        hole=0.4
    )
    category_fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        pull=[0.03] * len(category_data)
    )

    complaints_response = requests.get(
        "http://127.0.0.1:8000/complaints"
    )
    complaints = complaints_response.json()

    df = pd.DataFrame(complaints)

    st.subheader("All Complaints")



    category_filter = st.selectbox(
        "Select Category",
        [
        "All",
        "Health",
        "Safety",
        "Transport",
        "Roads",
        "Water",
        "Electricity",
        "Other"
        ]
    )
    status_filter = st.selectbox(
        "Select Status",
        ["All", "Pending", "In Progress", "Resolved", "Rejected"]
    )

    filtered_df = df.copy()

    if category_filter != "All":
        filtered_df = filtered_df[
            filtered_df["category"] == category_filter
        ]

    if status_filter != "All":
        filtered_df = filtered_df[
            filtered_df["status"] == status_filter
        ]

    search_id = st.text_input(
        "Search Complaint ID"
    )
    if search_id:
        filtered_df = filtered_df[
            filtered_df["complaint_id"]
            .astype(str)
            .str.contains(
                search_id,
                case=False,
                na=False
            )
        ]

    columns_to_show = [
        "complaint_id",
        "complaint",
        "category",
        "urgency",
        "status"
    ]

    st.dataframe(
        filtered_df[columns_to_show],
        use_container_width=True
    )

    status_data = {
        "Pending": stats["Pending"],
        "In Progress": stats["In Progress"],
        "Resolved": stats["Resolved"],
        "Rejected": stats["Rejected"]
    }

    status_fig = px.pie(
        names=list(status_data.keys()),
        values=list(status_data.values()),
        title="Complaints by Status",
        hole=0.4
    )
    status_fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        pull=[0.03] * len(status_data)
    )

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            category_fig,
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            status_fig,
            use_container_width=True
        )

    high_priority_response = requests.get(
        "http://127.0.0.1:8000/high-priority"
    )

    high_priority_complaints = high_priority_response.json()

    high_priority_df = pd.DataFrame(
        high_priority_complaints
    )

    st.subheader("🚨 High Priority Complaints")

    priority_columns = [
        "complaint_id",
        "complaint",
        "category",
        "urgency",
        "status"
    ]

    st.metric(
        "High Priority",
        len(high_priority_df)
    )

    if len(high_priority_df) == 0:
        st.success(
           "No High Priority Complaints 🎉"
        )
    else:
        st.dataframe(
            high_priority_df[priority_columns],
            use_container_width=True
        )

    st.subheader("🖋 Update Complaint Status")
    complaint_options = {
        f"{row['complaint_id']} - {row['category']}":
        row['complaint_id']
        for _, row in df.iterrows()
    }

    selected_display = st.selectbox(
        "Select Complaint",
        list(complaint_options.keys())
    )
    selected_complaint = complaint_options[selected_display]

    new_status = st.selectbox(
        "New Status",
        [
            "Pending",
            "In Progress",
            "Resolved",
            "Rejected"
        ]
    )

    if st.button("Update Status"):
        
        response = requests.put(
            f"http://127.0.0.1:8000/complaints/{selected_complaint}",
            json={
                "status": new_status
            }
        )

        st.success(
            response.json()["message"]
        )
        st.rerun()


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:

    st.title("🔐 Admin Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if "captcha" not in st.session_state:
    
        st.session_state["captcha"] = ''.join(
            random.choices(
                string.ascii_uppercase + 
                string.ascii_lowercase + 
                string.digits,
                k=6
            )
        )

    captcha = st.session_state["captcha"]

    st.write(f"Captcha: {captcha}")

    user_captcha = st.text_input(
        "Enter Captcha"
    )
    
    if st.button("Login"):

        if (
            username == "admin"
            and password == "admin123"
            and user_captcha == captcha
        ):

            st.session_state["logged_in"] = True
            st.sidebar.success("Logged in as Admin")
            st.rerun()

        else:
            st.error("Invalid Credentials")

else:
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()

    show_dashboard()