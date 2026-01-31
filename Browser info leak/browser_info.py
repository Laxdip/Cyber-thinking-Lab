# Browser Information Leak Tool
# Shows what information a browser exposes by default

from http.server import BaseHTTPRequestHandler, HTTPServer

class InfoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"<h2>Browser Information Leak</h2>")
        self.wfile.write(b"<p>The following data is automatically shared:</p>")
        self.wfile.write(b"<ul>")

        for header, value in self.headers.items():
            line = f"<li><b>{header}</b>: {value}</li>"
            self.wfile.write(line.encode())

        self.wfile.write(b"</ul>")
        self.wfile.write(b"<p><b>Note:</b> This data can be used for tracking and fingerprinting.</p>")

def run_server():
    server_address = ("localhost", 8000)
    httpd = HTTPServer(server_address, InfoHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()