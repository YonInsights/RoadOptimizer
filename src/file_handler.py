import ezdxf
import pandas as pd
from io import BytesIO

def parse_horizontal_alignment(file):
    """
    Parse horizontal alignment from DXF file.
    Extracts Northing and Easting coordinates from LWPOLYLINE entities.
    """
    try:
        # Read the uploaded file content into memory
        file_content = file.getvalue()
        file_like = BytesIO(file_content)

        # Use ezdxf.read() to parse the file content
        doc = ezdxf.read(file_like)
        msp = doc.modelspace()

        northing = []
        easting = []
        for entity in msp:
            if entity.dxftype() == 'LWPOLYLINE':  # Check for polyline entities
                for vertex in entity.get_points():
                    easting.append(vertex[0])  # X-coordinate
                    northing.append(vertex[1])  # Y-coordinate

        # Create a DataFrame
        data = pd.DataFrame({
            "Easting": easting,
            "Northing": northing
        })
        return data

    except Exception as e:
        raise ValueError(f"Error parsing horizontal alignment: {e}")

def parse_vertical_profile(file):
    """
    Parse vertical profile from DXF file.
    Extracts Station and Elevation from LWPOLYLINE entities.
    """
    try:
        # Read the uploaded file content into memory
        file_content = file.getvalue()
        file_like = BytesIO(file_content)

        # Use ezdxf.read() to parse the file content
        doc = ezdxf.read(file_like)
        msp = doc.modelspace()

        station = []
        elevation = []
        for entity in msp:
            if entity.dxftype() == 'LWPOLYLINE':  # Check for polyline entities
                for vertex in entity.get_points():
                    station.append(vertex[0])  # Assume X-axis is Station
                    elevation.append(vertex[1])  # Assume Y-axis is Elevation

        # Create a DataFrame
        data = pd.DataFrame({
            "Station": station,
            "Elevation": elevation
        })
        return data

    except Exception as e:
        raise ValueError(f"Error parsing vertical profile: {e}")