import streamlit as st
from src.file_handler import parse_horizontal_alignment, parse_vertical_profile
from src.optimization import optimize_both_alignments

def main():
    st.title("Combined Horizontal and Vertical Optimization")

    # Horizontal Alignment Upload
    st.subheader("Proposed Horizontal Alignment")
    horizontal_file = st.file_uploader("Upload Proposed Horizontal Alignment (DXF)", type=["dxf"])
    if horizontal_file:
        try:
            horizontal_data = parse_horizontal_alignment(horizontal_file)
            st.success("Horizontal Alignment Uploaded Successfully!")
            
            # Display uploaded alignment in yellow bold line
            st.markdown(
                "<p style='color: yellow; font-weight: bold;'>Uploaded Horizontal Alignment:</p>",
                unsafe_allow_html=True,
            )
            st.write(horizontal_data)
        except Exception as e:
            st.error(f"Error parsing horizontal alignment: {e}")

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
        except Exception as e:
            st.error(f"Error parsing vertical profile: {e}")

    # Optimization Button
    if st.button("Optimize Both Alignments"):
        if not horizontal_file or not vertical_file:
            st.error("Please upload both horizontal alignment and vertical profile files.")
        else:
            try:
                horizontal_data = parse_horizontal_alignment(horizontal_file)
                vertical_data = parse_vertical_profile(vertical_file)
                optimized_data = optimize_both_alignments(horizontal_data, vertical_data)
                
                # Display optimized alignments in red bold line
                st.markdown(
                    "<p style='color: red; font-weight: bold;'>Optimized Horizontal Alignment:</p>",
                    unsafe_allow_html=True,
                )
                st.write(optimized_data["horizontal"])

                st.markdown(
                    "<p style='color: red; font-weight: bold;'>Optimized Vertical Profile:</p>",
                    unsafe_allow_html=True,
                )
                st.write(optimized_data["vertical"])

            except Exception as e:
                st.error(f"Error during optimization: {e}")