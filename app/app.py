from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):

    def _send_response(self, code, body=b""):
        self.send_response(code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            self._send_response(200, b"ok\n")
            return

        if self.path == "/":
            self._send_response(200, b"Hello from app container\n")
            return

        self._send_response(404)

    def do_HEAD(self):
        if self.path in ["/", "/health"]:
            self._send_response(200)
            return

        self._send_response(404)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 3000), Handler)
    server.serve_forever()
