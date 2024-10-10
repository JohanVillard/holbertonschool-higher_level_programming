#!/usr/bin/python3
"""This modules defines a simple HTTP server."""

import http.server
import socketserver
import json


class MyHandler(http.server.BaseHTTPRequestHandler):
    """Represent a request handler."""

    def do_GET(self):
        """
        Send a simple text.

        do_GET method is called when the server receives a request HTTP GET.
        """
        if self.path == "/":
            # Send a response to the client (200 = OK)
            self.send_response(200)

            # Add Content-Type to indicate that the body is text type
            self.send_header("Content-Type", "text/plain")

            # All response's headers are send. The method finalize the headers.
            # The response's body is ready to be written.
            self.end_headers()

            # Send the text to the client.
            self.wfile.write(b"Hello, this is a simple API!")

        # Case : /data is included in the URL
        elif self.path == "/data":
            self.send_response(200)

            # Add Content-Type to indicate that the body is JSON type
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            # Define a dict and convert it to json
            dataset = {"name": "John", "age": 30, "city": "New York"}
            json_dataset = json.dumps(dataset)

            # Send file to the client. (encodage en bytes)
            self.wfile.write(json_dataset.encode(encoding="utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.send_message("OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            json_info = json.dumps(info)
            self.wfile.write(json_info.encode(encoding="utf-8"))

        # No path corresponds
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    # Create an HTTP server
    with socketserver.TCPServer(("", 8000), MyHandler) as httpd:
        # The server is launched indefinitely
        httpd.serve_forever()
