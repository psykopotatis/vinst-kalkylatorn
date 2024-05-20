import SimpleHTTPServer
import SocketServer

"""
# Start server
python server.py

"""
PORT = 8082

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("SimpleHTTPServer serving at http://localhost:%s" % PORT)
httpd.serve_forever()
