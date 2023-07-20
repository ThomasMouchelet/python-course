import http.server
import socketserver

PORT = 8001
address = ("", PORT)

handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(address, handler)

print("serving at port", PORT)

httpd.serve_forever()