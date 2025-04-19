import streamlit as st
from src.file_handler import parse_vertical_profile
from src.optimization import optimize_vertical_profile

def main():
    st.title("Vertical Profile Optimization")

    # Vertical Profile Upload
    st.subheader("Existing Vertical Profile")
    vertical_file = st.file_uploader("Upload Existing Vertical Profile (DXF)", type=["dxf"])
    if vertical_file:
        try:
            vertical_data = parse_vertical_profile(vertical_file)
            st.success("Vertical Profile Uploaded Successfully!")
            
            # Display uploaded profile in yellow bold line
            st.markdown(
                "<p style='color: yellow; font-weight: bold;'>Uploaded Vertical Profile:</p>",
                unsafe_allow_html=True,
            )
            st.write(vertical_data)

            # Optimization Button
            if st.button("Optimize Vertical Profile"):
                optimized_vertical = optimize_vertical_profile(vertical_data)
                
                # Display optimized profile in red bold line
                st.markdown(
                    "<p style='color: red; font-weight: bold;'>Optimized Vertical Profile:</p>",
                    unsafe_allow_html=True,
                )
                st.write(optimized_vertical)

        except Exception as e:
            st.error(f"Error parsing vertical profile: {e}")
