import http.server
import socketserver
import re
import ast
import os
import time
from datetime import datetime
from checkfile.openstack_checkfile_manage import openstack_check_all_file
from data.openstack_data_manage import openstack_data_all


PORT = 35358

class CustomHandler(http.server.SimpleHTTPRequestHandler):

    def get_now_time_string(self):
        date_time = datetime.fromtimestamp(time.time())
        return date_time.strftime("%Y-%m-%d_%H:%M:%S")

    def do_POST(self):
        if None != re.search('/openstack/*', self.path):
            list = self.path.split('/')
            resource = str(list[2])
            id = str(list[3])
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            body = ast.literal_eval(post_body.decode('utf-8'))
            time = self.get_now_time_string()
            path = os.path.dirname(os.path.abspath(__file__)) + "/log"


 
            if resource == "data" : 
                if not(os.path.isdir(path + "/" + time.split("_")[0])) :
                    os.makedirs(os.path.join(path + "/" + time.split("_")[0]))
                    print("mkdir" + path + "/" + time.split("_")[0])
                if not(os.path.isdir(path + "/" + time.split("_")[0] + "/data")) :
                    os.makedirs(os.path.join(path + "/" + time.split("_")[0] + "/data"))
                    print("mkdir" + path + "/" + time.split("_")[0] + "/data")

                openstack_data = openstack_data_all(body)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(str(openstack_data).encode())

            elif resource == "checklist" :
                openstack_checklist = openstack_check_all_file()
                checklist = {
                   'cloud_name': body['cloud_name'],
                   'vendor': body['vendor'],
                   'time': time,
                   'checklist': openstack_checklist
                }
                if not(os.path.isdir(path + "/" + time.split("_")[0])) : 
                    os.makedirs(os.path.join(path + "/" + time.split("_")[0]))
                    print("mkdir" + path + "/" + time.split("_")[0])
                if not(os.path.isdir(path + "/" + time.split("_")[0] + "/checklist")) :
                    os.makedirs(os.path.join(path + "/" + time.split("_")[0] + "/checklist"))
                    print("mkdir" + path + "/" + time.split("_")[0] + "/checklist")
                
                checklist_file = open(path + '/' + time.split("_")[0] + '/checklist/' + time.split("_")[1] + '.chk', 'w')
                checklist_file.write(str(checklist))
                checklist_file.close()
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

