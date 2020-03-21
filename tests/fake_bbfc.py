#!/usr/bin/env python
"""Fake BBFC Server returning pre-baked responses for testing.

Usage:
    ./fake_bbfc.py <port> <data-filename>

Example:
    ./fake_bbfc.py 8000 search_interstellar.html
"""
import sys
from functools import partial
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, filename=None, **kwargs):
        self.file = (Path(__file__).parent / "data" / filename).read_bytes()
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(self.file)


def run(port: int, filename: str):
    address = ("", port)
    httpd = HTTPServer(address, partial(RequestHandler, filename=filename))
    print("ONLINE-ISH")
    httpd.serve_forever()


if __name__ == "__main__":
    port = int(sys.argv[1])
    filename = sys.argv[2]
    run(port, filename)
