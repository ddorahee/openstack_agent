import http.server
import socketserver
import re
import time
import ast
import checkfile.checkfile_all as checkfile_all
import data.data_all as data_all


PORT = 35358

class CustomHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        if None != re.search('/openstack/*', self.path):
            list = self.path.split('/')
            resource = str(list[2])
            id = str(list[3])
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            body = ast.literal_eval(post_body.decode('utf-8'))
 
            if resource == "data" : 
                openstack_data = data_all.data_all(body)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(str(openstack_data).encode())

            elif resource == "checklist" :
                openstack_checklist = checkfile_all.check_all_file() 
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(str(openstack_checklist).encode())

httpd = socketserver.ThreadingTCPServer(('', PORT), CustomHandler)

print("Unicloudus Agent Start port " + str(PORT))
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()

