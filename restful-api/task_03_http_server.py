#!/usr/bin/python3
"""This modules defines a simple HTTP server."""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Represent a request handler."""

    def do_GET(self):
        """
        Send a simple text.

        do_GET method is called when the server receives a request HTTP GET.
        """

        if self.path == "/":
            # Send a response to the client (200 = OK)
            self.send_response(200)

            # All response's headers are send. The method finalize the headers.
            # The response 's body is ready to be written.
            self.end_headers()

            # Send the text to the client.
            self.wfile.write(b"Hello, this is simple API!")

        # Case : /data is included in the URL
        elif self.path == "/data":
            # Define a dict
            dataset = {"name": "John", "age": "30", "city": "New York"}

            # Conversion dict to json
            json_dataset = json.dumps(dataset)

            # Server's response is OK
            self.send_response(200)

            # Add Content-Type to indicate that the body is JSON type
            self.send_header("content-Type", "application/json")

            # Indicate that the header is finished
            self.end_headers()

            # Send file to the client. (encodage en bytes)
            self.wfile.write(json_dataset.encode(encoding="utf-8"))

        elif self.path == "/info":
            mark = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }

            json_mark = json.dumps(mark)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(json_mark.encode(encoding="utf-8"))

        else:
            # No path corresponds
            self.send_response(404)
            self.end_headers()

            self.wfile.write(b"Endpoint not found")


# Create an HTTP server
httpd = HTTPServer(("", 8000), SimpleHTTPRequestHandler)

# The server is launched indefinitely
httpd.serve_forever()
