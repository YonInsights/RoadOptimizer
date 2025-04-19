import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Road Alignment Optimization",
    layout="wide",
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Go to",
    ["Upload Data", "Horizontal Optimization", "Vertical Optimization", "Both"]
)

# Load the selected page
if page == "Upload Data":
    from pages.Upload_Data import main
    main()
elif page == "Horizontal Optimization":
    from pages.Horizontal_Optimization import main
    main()
elif page == "Vertical Optimization":
    from pages.Vertical_Optimization import main
    main()
elif page == "Both":
    from pages.Both_Optimization import main
    main()