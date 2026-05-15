"""
filter_points.py — keep only PA points that fall inside an Australian state polygon.
Reads:
  data/aus-states.geojson  (FeatureCollection of state MultiPolygons)
  data/protected-areas-points.csv
Writes (in place):
  data/protected-areas-points.csv
"""

import csv
import json


def point_in_ring(x: float, y: float, ring: list[list[float]]) -> bool:
    """Ray-casting test. ring = list of [lng, lat] pairs, closed (first == last)."""
    inside = False
    n = len(ring)
    j = n - 1
    for i in range(n):
        xi, yi = ring[i][0], ring[i][1]
        xj, yj = ring[j][0], ring[j][1]
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi)
        if intersect:
            inside = not inside
        j = i
    return inside


def point_in_polygon(x: float, y: float, polygon: list[list[list[float]]]) -> bool:
    """polygon = [outer_ring, hole_ring1, hole_ring2, ...].  Inside iff inside outer and outside all holes."""
    if not polygon:
        return False
    if not point_in_ring(x, y, polygon[0]):
        return False
    for hole in polygon[1:]:
        if point_in_ring(x, y, hole):
            return False
    return True


def point_in_geometry(x: float, y: float, geom: dict) -> bool:
    t = geom["type"]
    if t == "Polygon":
        return point_in_polygon(x, y, geom["coordinates"])
    if t == "MultiPolygon":
        return any(point_in_polygon(x, y, p) for p in geom["coordinates"])
    return False


def main() -> None:
    with open("data/aus-states.geojson", encoding="utf-8") as f:
        gj = json.load(f)
    geometries = [feat["geometry"] for feat in gj["features"]]

    with open("data/protected-areas-points.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    print(f"Total input points: {len(rows)}")

    kept = []
    for r in rows:
        try:
            lng = float(r["longitude"])
            lat = float(r["latitude"])
        except (KeyError, ValueError):
            continue
        if any(point_in_geometry(lng, lat, g) for g in geometries):
            kept.append(r)

    print(f"Kept (on land): {len(kept)}  ({len(rows) - len(kept)} dropped)")

    with open("data/protected-areas-points.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(kept)


if __name__ == "__main__":
    main()
