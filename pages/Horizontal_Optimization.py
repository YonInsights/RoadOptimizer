import streamlit as st
from src.file_handler import parse_horizontal_alignment
from src.optimization import optimize_horizontal_alignment

def main():
    st.title("Horizontal Alignment Optimization")

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

            # Optimization Button
            if st.button("Optimize Horizontal Alignment"):
                optimized_horizontal = optimize_horizontal_alignment(horizontal_data)
                
                # Display optimized alignment in red bold line
                st.markdown(
                    "<p style='color: red; font-weight: bold;'>Optimized Horizontal Alignment:</p>",
                    unsafe_allow_html=True,
                )
                st.write(optimized_horizontal)

        except Exception as e:
            st.error(f"Error parsing horizontal alignment: {e}")