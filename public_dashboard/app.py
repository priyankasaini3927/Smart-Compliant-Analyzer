import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze"

st.title("🧠 Citizen Grievance Intelligence Platform 📜")

text = st.text_area("Enter Complaint")

if st.button("Analyze"):

    if text.strip() == "":
        st.warning("Please enter a complaint.")

    else:

        response = requests.post(
            API_URL,
            json={"text": text}
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Analysis Complete")

            st.write(f"Complaint: {result['complaint']}")
            st.write(f"Complaint ID: {result['complaint_id']}")
            st.write(f"Category: {result['category']}")
            st.write(f"Urgency: {result['urgency']}")

        else:
            st.error(f"API Error: {response.status_code}")

response = requests.get(
    "http://127.0.0.1:8000/complaints"
)

complaints = response.json()

st.divider()

st.subheader("🔍 Track Complaint Status")

track_id = st.text_input(
    "Enter Complaint ID"
)

if st.button("Track Complaint"):
    
    response = requests.get(
        f"http://127.0.0.1:8000/complaints/{track_id}"
    )

    result = response.json()

    if "message" not in result:
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "Category",
                result["category"]
            )
        with col2:
            st.metric(
                "Status",
                result["status"]
            )
        st.write(
            f"Complaint ID: {result['complaint_id']}"
        )
    else:
        st.error("Complaint not found")