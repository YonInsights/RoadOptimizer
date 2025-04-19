import streamlit as st
from src.file_handler import parse_horizontal_alignment, parse_vertical_profile
from src.optimization import (
    optimize_horizontal_alignment,
    optimize_vertical_profile,
    optimize_both_alignments,
)
from src.design_standards import get_standard
import matplotlib.pyplot as plt

def main():
    st.title("Road Alignment Optimization")

    # Navigation Options
    st.subheader("Optimization Type")
    optimization_type = st.radio(
        "Select Optimization Type",
        ["Horizontal Alignment", "Vertical Profile", "Both"],
        horizontal=True,
    )

    # Horizontal Alignment Upload
    if optimization_type in ["Horizontal Alignment", "Both"]:
        st.subheader("Proposed Horizontal Alignment")
        horizontal_file = st.file_uploader("Upload Proposed Horizontal Alignment (DXF)", type=["dxf"])
        if horizontal_file:
            try:
                horizontal_data = parse_horizontal_alignment(horizontal_file)
                st.success("Horizontal Alignment Uploaded Successfully!")
                st.session_state["horizontal_data"] = horizontal_data

                # Display uploaded alignment in a table
                st.markdown(
                    "<p style='color: yellow; font-weight: bold;'>Uploaded Horizontal Alignment:</p>",
                    unsafe_allow_html=True,
                )
                st.write(horizontal_data.head(5))  # Show first 5 rows

                # Plot uploaded alignment
                fig, ax = plt.subplots()
                ax.plot(horizontal_data["Easting"], horizontal_data["Northing"], color="yellow", linewidth=2)
                ax.set_title("Uploaded Horizontal Alignment")
                ax.set_xlabel("Easting")
                ax.set_ylabel("Northing")
                st.pyplot(fig)

            except Exception as e:
                st.error(f"Error parsing horizontal alignment: {e}")

    # Vertical Profile Upload
    if optimization_type in ["Vertical Profile", "Both"]:
        st.subheader("Existing Vertical Profile")
        vertical_file = st.file_uploader("Upload Existing Vertical Profile (DXF)", type=["dxf"])
        if vertical_file:
            try:
                vertical_data = parse_vertical_profile(vertical_file)
                st.success("Vertical Profile Uploaded Successfully!")
                st.session_state["vertical_data"] = vertical_data

                # Display uploaded profile in a table
                st.markdown(
                    "<p style='color: yellow; font-weight: bold;'>Uploaded Vertical Profile:</p>",
                    unsafe_allow_html=True,
                )
                st.write(vertical_data.head(5))  # Show first 5 rows

                # Plot uploaded vertical profile
                fig, ax = plt.subplots()
                ax.plot(vertical_data["Station"], vertical_data["Elevation"], color="yellow", linewidth=2)
                ax.set_title("Uploaded Vertical Profile")
                ax.set_xlabel("Station")
                ax.set_ylabel("Elevation")
                st.pyplot(fig)

            except Exception as e:
                st.error(f"Error parsing vertical profile: {e}")

    # Design Inputs
    st.subheader("Design Inputs")
    st.write("**Note:** You can input multiple sections with different terrain types, design speeds, and road types.")

    num_sections = st.number_input("Number of Sections", min_value=1, max_value=10, value=1)
    sections = []

    for i in range(num_sections):
        st.write(f"**Section {i + 1}**")
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # Design Class Input
            design_classes = ["DC1", "DC2", "DC3", "DC4", "DC5", "DC6", "DC7", "DC8"]
            design_class = st.selectbox(f"ERA Design Class (Section {i + 1})", design_classes)

        with col2:
            # Terrain Type Input
            terrain_types = ["Flat", "Rolling", "Mountainous", "Escarpment"]
            terrain_type = st.selectbox(f"Terrain Type (Section {i + 1})", terrain_types)

        with col3:
            # Road Type Input
            road_types = ["Rural", "Kebele", "Woreda", "Zone", "Urban"]
            road_type = st.selectbox(f"Road Type (Section {i + 1})", road_types)

        with col4:
            # Design Speed Input
            design_speed = st.number_input(f"Design Speed (km/h) (Section {i + 1})", min_value=10, max_value=160, value=80)

        with col5:
            # Station Interval Input (formatted as "0+000 - 3+150")
            station_start = st.number_input(f"Start Station (m) (Section {i + 1})", min_value=0, max_value=10000, value=i * 3150)
            station_end = st.number_input(f"End Station (m) (Section {i + 1})", min_value=station_start + 1, max_value=10000, value=station_start + 3150)
            formatted_station_interval = f"{int(station_start // 1000)}+{int(station_start % 1000):03d} - {int(station_end // 1000)}+{int(station_end % 1000):03d}"

        # Validate inputs against ERA standards
        try:
            # Retrieve minimum radius for validation
            min_radius = get_standard("minimum_radius", design_class, terrain_type)

            # Add section data to list
            sections.append({
                "design_class": design_class,
                "terrain_type": terrain_type,
                "road_type": road_type,
                "design_speed": design_speed,
                "station_interval": formatted_station_interval,
                "min_radius": min_radius,
            })

        except ValueError as e:
            st.error(f"Error in Section {i + 1}: {e}")

    # Display validation results
    if sections:
        st.subheader("Validation Results")
        for i, section in enumerate(sections):
            st.write(f"**Section {i + 1}**")
            st.write(f"- Design Class: {section['design_class']}")
            st.write(f"- Terrain Type: {section['terrain_type']}")
            st.write(f"- Road Type: {section['road_type']}")
            st.write(f"- Design Speed: {section['design_speed']} km/h")
            st.write(f"- Station Interval: {section['station_interval']}")
            st.write(f"- Minimum Radius: {section['min_radius']} m")

    # Optimization Button
    if st.button("Optimize"):
        if not sections:
            st.error("No valid sections found. Please enter at least one section.")
        else:
            st.success("Optimization started!")

            # Retrieve parsed data
            horizontal_data = st.session_state.get("horizontal_data", None)
            vertical_data = st.session_state.get("vertical_data", None)

            try:
                if optimization_type == "Horizontal Alignment":
                    if horizontal_data is None:
                        st.error("Please upload a horizontal alignment file.")
                    else:
                        optimized_horizontal = optimize_horizontal_alignment(horizontal_data, sections)
                        st.markdown(
                            "<p style='color: red; font-weight: bold;'>Optimized Horizontal Alignment:</p>",
                            unsafe_allow_html=True,
                        )
                        st.write(optimized_horizontal)

                elif optimization_type == "Vertical Profile":
                    if vertical_data is None:
                        st.error("Please upload a vertical profile file.")
                    else:
                        optimized_vertical = optimize_vertical_profile(vertical_data, sections)
                        st.markdown(
                            "<p style='color: red; font-weight: bold;'>Optimized Vertical Profile:</p>",
                            unsafe_allow_html=True,
                        )
                        st.write(optimized_vertical)

                elif optimization_type == "Both":
                    if horizontal_data is None or vertical_data is None:
                        st.error("Please upload both horizontal alignment and vertical profile files.")
                    else:
                        optimized_data = optimize_both_alignments(horizontal_data, vertical_data, sections)
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

    # Store sections in session state
    st.session_state["sections"] = sections