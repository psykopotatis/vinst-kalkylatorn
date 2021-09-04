import SimpleHTTPServer
import SocketServer

"""
# Start server
python server.py

"""
PORT = 8081

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "SimpleHTTPServer serving at port", PORT
httpd.serve_forever()
