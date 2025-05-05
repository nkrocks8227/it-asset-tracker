import streamlit as st
import pandas as pd
import datetime
from pages import dashboard, assets, budget, reports
from pages.assignments_updated import show_assignments_page
from data.asset_data import initialize_session_state
from utils.currency import initialize_currency_settings, CURRENCY_SYMBOLS

# Page configuration
st.set_page_config(
    page_title="IT Asset Tracker",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables if they don't exist
initialize_session_state()
initialize_currency_settings()

def main():
    # Sidebar navigation
    with st.sidebar:
        st.title("IT Asset Tracker")
        
        # Display options
        selected_page = st.radio(
            "Navigation",
            options=["Dashboard", "Assets", "Assignments", "Budget", "Reports"]
        )
        
        st.markdown("---")
        
        # Show some stock photos in the sidebar
        st.subheader("IT Assets Overview")
        
        # Using the provided stock photos
        st.image("https://images.unsplash.com/photo-1498050108023-c5249f4df085", 
                caption="Office Equipment", use_column_width=True)
        
        st.image("https://images.unsplash.com/photo-1580795479225-c50ab8c3348d", 
                caption="IT Hardware Assets", use_column_width=True)
        
        # Add settings section
        st.markdown("---")
        st.subheader("Settings")
        
        # Currency selector
        currency_options = list(CURRENCY_SYMBOLS.keys())
        selected_currency = st.selectbox(
            "Currency",
            options=currency_options,
            index=currency_options.index(st.session_state.currency_code),
            key="currency_selector"
        )
        
        # Update session state when currency is changed
        if selected_currency != st.session_state.currency_code:
            st.session_state.currency_code = selected_currency
            st.rerun()
        
        # Add current date at the bottom of sidebar
        st.markdown("---")
        st.caption(f"Today: {datetime.date.today().strftime('%B %d, %Y')}")

    # Main content based on selected page
    if selected_page == "Dashboard":
        dashboard.show_dashboard()
    elif selected_page == "Assets":
        assets.show_assets_page()
    elif selected_page == "Assignments":
        show_assignments_page()
    elif selected_page == "Budget":
        budget.show_budget_page()
    elif selected_page == "Reports":
        reports.show_reports_page()

if __name__ == "__main__":
    main()
