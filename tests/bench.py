#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""benchmark"""

import timeit
from warnings import filterwarnings as filter_warnings

import web_mini


def main() -> int:
    """entry / main function"""

    num: int = 2 ** 16

    with open("index.html", "r") as html:
        print(
            "html",
            timeit.timeit(lambda: web_mini.html.minify_html(html.read()), number=num),
        )

    with open("styles.css", "r") as css:
        print(
            "css",
            timeit.timeit(lambda: web_mini.css.minify_css(css.read()), number=num),
        )

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    raise SystemExit(main())
