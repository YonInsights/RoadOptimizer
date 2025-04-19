import ezdxf
import pandas as pd
import tempfile

def parse_horizontal_alignment(uploaded_file):
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".dxf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        # Read the temp file using readfile
        doc = ezdxf.readfile(tmp_path)
        msp = doc.modelspace()

        alignment_data = []
        for entity in msp:
            if entity.dxftype() == "LINE":
                start = entity.dxf.start
                end = entity.dxf.end
                alignment_data.append({"Easting": start.x, "Northing": start.y})
                alignment_data.append({"Easting": end.x, "Northing": end.y})

        return pd.DataFrame(alignment_data)

    except Exception as e:
        raise ValueError(f"Failed to parse DXF: {e}")
def parse_vertical_profile(uploaded_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".dxf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        doc = ezdxf.readfile(tmp_path)
        msp = doc.modelspace()

        station = []
        elevation = []
        for entity in msp:
            if entity.dxftype() == 'LWPOLYLINE':
                for vertex in entity.get_points():
                    station.append(vertex[0])
                    elevation.append(vertex[1])

        return pd.DataFrame({"Station": station, "Elevation": elevation})

    except Exception as e:
        raise ValueError(f"Error parsing vertical profile: {e}")
