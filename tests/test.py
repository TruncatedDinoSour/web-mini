#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test web_mini"""

import http.server
import os
import time
import typing
from warnings import filterwarnings as filter_warnings

import web_mini


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        file_path: str = self.translate_path(self.path)  # type: ignore

        if os.path.isdir(file_path):  # type: ignore
            file_path = f"{file_path}/index.html"

        try:
            with open(file_path, "rb") as fp:  # type: ignore
                self.send_response(200)  # type: ignore
                self.end_headers()  # type: ignore

                content: typing.Union[bytes, str]

                if file_path.endswith("html") or file_path.endswith("css"):
                    content = fp.read().decode()
                else:
                    content = fp.read()

                t: float = time.time()

                if file_path.endswith("html"):
                    print("html minification")
                    content = web_mini.html.minify_html(content)
                elif file_path.endswith("css"):
                    print("css minification")
                    content = web_mini.css.minify_css(content)

                if type(content) is str:
                    print(content)

                print(time.time() - t, "s")
                self.wfile.write(content.encode() if type(content) is str else content)  # type: ignore
        except Exception as e:
            self.send_response(404)  # type: ignore
            self.end_headers()  # type: ignore
            self.wfile.write(f"{e.__class__.__name__} : {e}".encode())  # type: ignore


def main() -> int:
    """entry / main function"""

    httpd: typing.Any = http.server.HTTPServer(("127.0.0.1", 8080), RequestHandler)
    httpd.RequestHandlerClass.directory = "."

    try:
        print(
            f"server running on http://{httpd.server_address[0]}:{httpd.server_address[1]}/ ^C to close it"
        )
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print("server shut down")

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    raise SystemExit(main())
