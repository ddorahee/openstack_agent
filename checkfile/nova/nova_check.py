import os 
import subprocess


def nova_ower_check(nova_ower) : 
    nova_ower = nova_ower.split("\n")
    if "root nova" in keystone_ower[0] :
        print("nova folder root nova ower")
    else :
        print("None")

    if "root nova" in keystone_ower[1] :
        print("nova conf root nova ower")
    else :
        print("None")

    if "root nova" in keystone_ower[2] :
        print("api-paste root nova ower")
    else :
        print("None")

    if "root nova" in keystone_ower[3] :
        print("policy root nova ower")
    else :
        print("None")

    if "root nova" in keystone_ower[4] :
        print("rootwrap root nova ower")
    else :
        print("None")

def nova_right_check(nova_right) : 
    nova_right = nova_right.split("\n")

    if "etc" in nova_right[0] :
        if "drwxr-x---" in nova_right[0]:
            print("keystone folder True")
        else :
            print("keystone folder False")

def nova_conf_check():
    conf = open("/etc/nova/nova.conf", 'r')
    lines = conf.readlines()
    cnt = []
    check = ""
    conf.close()
    for line in lines:
        check_new_line = line.replace('\n', '#').replace(' ', '#')
        if check_new_line[0] == '#':
            continue
        elif '[API]' in line.upper():
            check = 1
        elif '[keystone_authtoken]' in line:
            check = 2 
        elif '[glance]' in line :
            check = 3

        elif check == 1 :
            line = line.replace(' ', "").lower()
            if 'auth_strategy' in line :
                print("auth_strategy nice")
            elif 'auth_strategy' not in line :
                print("auth_strategy no nice")
            check = "" 
 
        elif check == 2 :
            line = line.replace(' ', "").lower()
            if 'auth_url=http://' in line :
                print("http No Nice")
            elif 'auth_url=https://' in line : 
                print("https Nice")
            if 'insecure=false' in line : 
                print("insecure nice")
            elif 'insecure=false' not in line :
                print("insecure No nice")
            check = ""

        elif check == 3 :
            line = line.replace(' ', "").lower()
            if 'api_insecure=false' in line :
                print("api_insecure Nice")
            elif 'api_insecure=false' not in line :
                print("api_insecure no nice")
            if 'api_servers=https'  in line :
                print("api_servers nice")
            elif 'api_servers=https' not in line : 
                print("api_servers no")
            check = ""




def nova_checklist(path) :
#    result = subprocess.run([path + "./nova_ower_check.sh"], stdout=subprocess.PIPE)
#    result2 = subprocess.run([path + "./nova_right_check.sh"], stdout=subprocess.PIPE)
#    nova_ower = result.stdout.decode("UTF-8")
#    nova_ower_check(nova_ower) 

#    nova_right = result.stdout.decode("UTF-8")
#    nova_right_check(nova_right)
    nova_conf_check()

nova_checklist("a")


