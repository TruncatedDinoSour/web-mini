#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""constants"""

from typing import Dict, Final, Set

REPLACABLE_CLRS: Final[Dict[str, str]] = {
    "blanchedalmond": "#ffebcd",
    "burlywood": "#deb887",
    "chartreuse": "#7fff00",
    "chocolate": "#d2691e",
    "cornsilk": "#fff8dc",
    "darkcyan": "#008b8b",
    "darkgoldenrod": "#b8860b",
    "darkgray": "#a9a9a9",
    "darkgreen": "#006400",
    "darkgrey": "#a9a9a9",
    "darkkhaki": "#bdb76b",
    "darkmagenta": "#8b008b",
    "darkolivegreen": "#556b2f",
    "darkorange": "#ff8c00",
    "darkorchid": "#9932cc",
    "darksalmon": "#e9967a",
    "darkseagreen": "#8fbc8f",
    "darkslategray": "#2f4f4f",
    "darkslategrey": "#2f4f4f",
    "darkturquoise": "#00ced1",
    "darkviolet": "#9400d3",
    "deeppink": "#ff1493",
    "firebrick": "#b22222",
    "forestgreen": "#228b22",
    "gainsboro": "#dcdcdc",
    "goldenrod": "#daa520",
    "honeydew": "#f0fff0",
    "indianred": "#cd5c5c",
    "lavender": "#e6e6fa",
    "lavenderblush": "#fff0f5",
    "lawngreen": "#7cfc00",
    "lemonchiffon": "#fffacd",
    "lightcoral": "#f08080",
    "lightcyan": "#e0ffff",
    "lightgray": "#d3d3d3",
    "lightgreen": "#90ee90",
    "lightgrey": "#d3d3d3",
    "lightpink": "#ffb6c1",
    "lightsalmon": "#ffa07a",
    "lightseagreen": "#20b2aa",
    "lightslategray": "#789",
    "lightslategrey": "#789",
    "limegreen": "#32cd32",
    "magenta": "#f0f",
    "mediumorchid": "#ba55d3",
    "mediumpurple": "#9370db",
    "mediumseagreen": "#3cb371",
    "mediumspringgreen": "#00fa9a",
    "mediumturquoise": "#48d1cc",
    "mediumvioletred": "#c71585",
    "mintcream": "#f5fffa",
    "mistyrose": "#ffe4e1",
    "moccasin": "#ffe4b5",
    "olivedrab": "#6b8e23",
    "orangered": "#ff4500",
    "palegoldenrod": "#eee8aa",
    "palegreen": "#98fb98",
    "paleturquoise": "#afeeee",
    "palevioletred": "#db7093",
    "papayawhip": "#ffefd5",
    "peachpuff": "#ffdab9",
    "rosybrown": "#bc8f8f",
    "saddlebrown": "#8b4513",
    "sandybrown": "#f4a460",
    "seagreen": "#2e8b57",
    "seashell": "#fff5ee",
    "slategray": "#708090",
    "slategrey": "#708090",
    "springgreen": "#00ff7f",
    "turquoise": "#40e0d0",
}

UNNEEDED_HTML_TAGS: Final[Set[str]] = {
    "<html>",
    "</colgroup>",
    "</img>",
    "<head>",
    "</dd>",
    "</tr>",
    "</area>",
    "</base>",
    "</head>",
    "</li>",
    "</tbody>",
    "</param>",
    "<tbody>",
    "</link>",
    "</br>",
    "</basefont>",
    "</option>",
    "</hr>",
    "</td>",
    "</input>",
    "</th>",
    "</html>",
    "</dt>",
    "</col>",
    "</thead>",
    "</meta>",
    "</body>",
    "<body>",
    "</tfoot>",
    "</isindex>",
}
