# This file is to test if the server is working
from http.server import BaseHTTPRequestHandler, HTTPServer


class PingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # If the request path is "/ping", respond with "pong"
        if self.path == "/ping":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"message": "pong"}') # Expected output: {"message": "pong"}
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not Found"}') # Expected output: {"error": "Not Found"}

# Define server details
HOST = "localhost"
PORT = 8001

if __name__ == "__main__":
    # Start the server on localhost:8001
    server = HTTPServer((HOST, PORT), PingHandler)
    print(f"Server running on http://{HOST}:{PORT}")
    try:
        server.serve_forever()  # Runs until you press CTRL+C
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()
        print("Server stopped.")
