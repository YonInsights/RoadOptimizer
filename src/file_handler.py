# src/file_handler.py

import ezdxf
import pandas as pd

def parse_dxf(filepath):
    """
    Extract points from LWPOLYLINE or POLYLINE in a DXF file.
    Returns a DataFrame with coordinates.
    """

    doc = ezdxf.readfile(filepath)
    msp = doc.modelspace()
    coords = []

    for entity in msp:
        if entity.dxftype() == "LWPOLYLINE":
            for point in entity:
                x, y = point[0], point[1]
                coords.append((x, y))
        elif entity.dxftype() == "POLYLINE":
            for vertex in entity.vertices():
                x, y = vertex.dxf.location.x, vertex.dxf.location.y
                coords.append((x, y))

    if not coords:
        raise ValueError("No polyline found in the DXF file.")

    df = pd.DataFrame(coords, columns=["X", "Y"])
    return df

