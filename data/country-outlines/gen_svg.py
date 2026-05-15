"""
Generate inline SVG path data for 4 country outlines, area-proportional.
Reads data/country-outlines/{AUS,DEU,FRA,ESP}.geojson and prints HTML SVG block.
"""

import json

# Real terrestrial protected area (Australia) vs country total areas (km²).
# Source: CAPAD 2024 for AUS; CIA Factbook for European totals.
AREAS = {"AUS": 1_690_000, "DEU": 357_022, "FRA": 551_695, "ESP": 505_990}

# Layout coords inside viewBox 0..500 x 0..300.
# Australia anchored top-left; Europe trio packed on the right.
ANCHORS = {
    "AUS": {"x": 25, "y": 50, "target_w": 210},  # width 210
    "DEU": {"x": 265, "y": 55, "target_w": 95},
    "FRA": {"x": 370, "y": 30, "target_w": 130},
    "ESP": {"x": 330, "y": 180, "target_w": 130},
}

COLORS = {"AUS": "#3f4a2a", "DEU": "#c66b3d", "FRA": "#c66b3d", "ESP": "#c66b3d"}

LABELS = {
    "AUS": {"big": "1.69M", "small": "km² protected", "caption": "Australia · 22% of land", "big_size": 30, "label_dy": 10},
    "DEU": {"big": "357K", "small": "Germany", "caption": "km²", "big_size": 15, "label_dy": -2},
    "FRA": {"big": "551K", "small": "France", "caption": "km²", "big_size": 17, "label_dy": -2},
    "ESP": {"big": "506K", "small": "Spain", "caption": "km²", "big_size": 17, "label_dy": -2},
}


def rings(geom):
    if geom["type"] == "Polygon":
        return [geom["coordinates"][0]]
    if geom["type"] == "MultiPolygon":
        return [poly[0] for poly in geom["coordinates"]]
    return []


def ring_area(ring):
    return abs(sum(ring[i][0] * ring[i + 1][1] - ring[i + 1][0] * ring[i][1]
                   for i in range(len(ring) - 1))) / 2


def to_path(code, geom, target_w):
    polys = rings(geom)
    sizes = [ring_area(r) for r in polys]
    biggest = max(sizes) if sizes else 1
    kept = [p for p, s in zip(polys, sizes) if s >= biggest * 0.01]

    xs = [pt[0] for r in kept for pt in r]
    ys = [pt[1] for r in kept for pt in r]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    span_x = maxx - minx
    span_y = maxy - miny

    # Scale so the bbox area is area-proportional to Australia.
    # AU bbox = target_w * (target_w * aspect_y/aspect_x).
    # Use simple rule: scale = target_w / span_x  (width-driven).
    scale = target_w / span_x
    bbox_h = span_y * scale

    cmds = []
    for ring in kept:
        for i, (lng, lat) in enumerate(ring):
            x = (lng - minx) * scale
            y = (maxy - lat) * scale  # flip y
            cmds.append(("M" if i == 0 else "L") + f"{x:.2f},{y:.2f}")
        cmds.append("Z")
    return " ".join(cmds), target_w, bbox_h


def main():
    print('<svg viewBox="0 0 500 300" preserveAspectRatio="xMidYMid meet"\n'
          '     style="width:100%;flex:1;min-height:280px;display:block;">')
    for code in ["AUS", "DEU", "FRA", "ESP"]:
        with open(f"data/country-outlines/{code}.geojson") as f:
            gj = json.load(f)
        geom = gj["features"][0]["geometry"]
        a = ANCHORS[code]
        path_d, w, h = to_path(code, geom, a["target_w"])
        color = COLORS[code]
        lab = LABELS[code]
        cx = w / 2
        cy = h / 2
        print(f'  <!-- {code} bbox={w:.0f}x{h:.0f} -->')
        print(f'  <g transform="translate({a["x"]},{a["y"]})">')
        print(f'    <path d="{path_d}"')
        print(f'          fill="{color}" stroke="#1a1a1a" stroke-width="0.8" stroke-linejoin="round"/>')
        # big number
        print(f'    <text x="{cx:.1f}" y="{cy + lab["label_dy"]:.1f}" text-anchor="middle"'
              f' font-family="Fraunces" font-size="{lab["big_size"]}" font-weight="700" fill="#f5efe6">{lab["big"]}</text>')
        # small label below big number
        sm_dy = lab["big_size"] * 0.65
        print(f'    <text x="{cx:.1f}" y="{cy + lab["label_dy"] + sm_dy:.1f}" text-anchor="middle"'
              f' font-family="Public Sans" font-size="9" fill="#f5efe6">{lab["small"]}</text>')
        # caption
        if code == "AUS":
            print(f'    <text x="{cx:.1f}" y="{cy + lab["label_dy"] + sm_dy + 14:.1f}" text-anchor="middle"'
                  f' font-family="Public Sans" font-size="8" font-style="italic" fill="#d8cdb7">{lab["caption"]}</text>')
        else:
            print(f'    <text x="{cx:.1f}" y="{cy + lab["label_dy"] + sm_dy + 11:.1f}" text-anchor="middle"'
                  f' font-family="Public Sans" font-size="7" fill="#f5efe6" opacity="0.78">{lab["caption"]}</text>')
        print(f'  </g>')
    # ≈ sign between Australia and Europe
    print('  <text x="248" y="155" text-anchor="middle"'
          ' font-family="Fraunces" font-size="34" font-weight="400" fill="#8a8278">≈</text>')
    # caption below
    print('  <text x="250" y="287" text-anchor="middle"'
          ' font-family="Public Sans" font-size="11" fill="#4a4641">'
          'Australia protects more land than Germany, France and Spain '
          '<tspan font-weight="700">combined.</tspan></text>')
    print('</svg>')


if __name__ == "__main__":
    main()
