import http.server
import socketserver
import re
import ast
from checkfile.openstack_checkfile_manage import openstack_check_all_file
from data.openstack_data_manage import openstack_data_all


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
                openstack_data = openstack_data_all(body)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(str(openstack_data).encode())

            elif resource == "checklist" :
                openstack_checklist = openstack_check_all_file()
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

