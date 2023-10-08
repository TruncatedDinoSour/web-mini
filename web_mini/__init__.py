#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""web-mini -- the web minifier for a mini web"""

from typing import Tuple

from . import css, html

__version__: str = "1.0.0"
__all__: Tuple[str, ...] = "__version__", "html", "css"
