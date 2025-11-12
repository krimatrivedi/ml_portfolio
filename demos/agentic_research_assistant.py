# krima_agentic_assistant.py
import streamlit as st
from datetime import datetime, timedelta

def run_demo():
    st.set_page_config(page_title="Agentic Scheduler", layout="wide")
    st.title("🤖 Krima's Agentic Scheduler")

    st.markdown("""
    This assistant helps recruiters plan interviews and joining schedules based on Krima's preferences.  
    It ensures proper notice, preferred time slots, and logical joining timelines.
    """)

    # Fixed details
    notice_period_months = 2
    st.info("📅 Krima's notice period is fixed: 2 months.")

    # Recruiter inputs
    interview_date = st.date_input("Select proposed interview date:", min_value=datetime.now().date())
    pref_time = st.radio("Choose preferred interview slot:", [
        "Morning: 9:00 AM – 11:30 AM",
        "Evening: 4:45 PM – 7:00 PM"
    ])
    notice_days = st.slider("Minimum days of prior notice you plan to give:", 1, 7, 2)
    select_days = st.number_input("Days your team might take after the interview to finalize selection:", min_value=0, max_value=60, value=5)

    if st.button("Generate Smart Schedule Plan"):
        today = datetime.now().date()

        # Calculate when recruiter should inform Krima
        notify_by = interview_date - timedelta(days=notice_days)

        # Calculate joining date (based on fixed notice period)
        joining_date = today + timedelta(days=(notice_period_months * 30+select_days))

        st.subheader("Smart Interview & Joining Plan")

        st.write(f"**Interview Date:** {interview_date.strftime('%B %d, %Y')}")
        st.write(f"**Selected Slot:** {pref_time}")

        st.markdown("---")
        st.write(f"**Recruiter should contact Krima by:** {notify_by.strftime('%B %d, %Y')} (at least {notice_days} day(s) prior)")
        st.write(f"**Expected Earliest Joining Date:** {joining_date.strftime('%B %d, %Y')}")

        st.markdown("---")
        st.markdown("""
        *Tip for recruiters:*  
        Please send interview invites at least the selected number of days before the interview date.  
        Official communication can be sent to Krima’s contact details available on her portfolio site or resume.
        """)

        st.success("Smart scheduling plan generated successfully!")