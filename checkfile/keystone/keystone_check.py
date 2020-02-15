import subprocess
import os 

def keystone_right_check(keystone_right) : 
    keystone_right = keystone_right.split("\n")
    if "keystone" in keystone_right[0] : 
        if "drwxr-x---" in keystone_right[0]:
            print("keystone folder True")
        else :
            print("keystone folder False")

    if "keystone.conf" in keystone_right[1]:
        if "-rw-r----" in keystone_right[1]: 
            print("keystone_conf True")
        else : 
            print("keystone_conf False")
    if "keystone-paste.ini" in keystone_right[2] : 
        if "-rw-r----" in keystone_right[2] : 
            print("keystone-paste True")
        else : 
            print("keystone-paste False")
    if "policy.json" in keystone_right[3] : 
        if "-rw-r----" in keystone_right[3] : 
            print("policy.json True")
        else : 
            print("policy.json False")
    if "logging.conf" in keystone_right[4] : 
        if "-rw-r----" in keystone_right[4] : 
            print("logging.conf True")
        else : 
            print("logging.conf False")

    try :
        if keystone_right[5] is None or keystone_right[5] == "" :
            print("File None")
        elif "signing_cert.pem" in keystone_right[5] : 
            if "-rw-r----" in keystone_right[5] : 
                print("signing_cert.pem True")
            else :
                print("signing_cert.pem False") 
    except : 
        print("File None")

    try :
        if keystone_right[6] is None or keystone_right[6] == "" :
            print("File None")
        elif "ca.pem" in keystone_right[6] :
            if "-rw-r----" in keystone_right[6] :
                print("ca.pem True")
            else :
                print("ca.pem False")
    except :
        print("File None")


    try :
        if keystone_right[7] is None or keystone_right[7] == "" :
            print("File None")
        elif "signing_key.pem" in keystone_right[7] :
            if "-rw-r----" in keystone_right[7] :
                print("signing_key.pem True")
            else :
                print("signing_key.pem False")
    except :
        print("File None")



def keystone_ower_check(keystone_ower) :
    keystone_ower = keystone_ower.split("\n")
 
    if "keystone keystone" in keystone_ower[0] :
        print("keystone/ keystone ower")
    else :
        print("keystone/ root ower")

    if "keystone keystone" in keystone_ower[1] :
        print("keystone_conf keystone ower")
    else : 
        print("keystone_conf root ower")

    if "keystone keystone" in keystone_ower[2] :
        print("keystone-paste.ini keystone ower")
    else :
        print("keystone-paste.ini root ower")

    if "keystone keystone" in keystone_ower[3] :
        print("policy.json keystone ower")
    else :
        print("policy.json root ower")
    
    if "keystone keystone" in keystone_ower[4] :
        print("logging.conf keystone ower")
    else :
        print("loggig.conf root ower")

    try : 
        if keystone_ower[5] is None or keystone_ower[5] == "" : 
            print("File None")
        elif "keystone keystone" in keystone_ower[5] : 
            print("signing_cert.pem keystone ower")
        else : 
            print("signing_cert.pem root ower")
    except : 
        print("File None")

    try : 
        if keystone_ower[6] is None or keystone_ower[6] == "" :
            print("File None")
        elif "keystone keystone" in keystone_ower[6] :
            print("signing_key.pem keystone ower")
        else :
            print("signing_key.pem root ower")
    except :
        print("File None")

    try : 
        if keystone_ower[7] is None or keystone_ower[7] == "" :
            print("File None")
        elif "keystone keystone" in keystone_ower[7] :
            print("ca.pem keystone ower")
        else :
           print("ca.pem root ower")
    except : 
        print("File None")

def keystone_conf_check():
    max_request = {
        "status" : {},
        "data" : {}
    }
    admin_token = {
        "status" : {},
        "data" : {}
    }
    provider = {
        "status" : {},
        "data" : {}
    }
    conf = open("/etc/keystone/keystone.conf", 'r')
    lines = conf.readlines()
    cnt = []
    check = ""
    conf.close()
    for line in lines:
        check_new_line = line.replace('\n', '#').replace(' ', '#')
        if check_new_line[0] == '#':
            continue
        elif '[DEFAULT]' in line:
            check = 3
        elif '[oslo_middleware]' in line :
            check = 2
        elif '[token]' in line :
            check = 1

        elif check == 1 :
            line = line.replace(' ', "").lower()
            if 'provider=fernet' in line :
                provider['status'] = 0
                provider['data'] = line.split("\n")[0]
            elif 'provider=fernet' not in line :
                provider['status']=2
                provider['data'] = line.split("\n")[0]
            if 'hash_algorithm=sha256' in line :
                print("hash_algorithm")
            elif 'hash_algorithm=sha256' not in line :
                print("hash_algorithm None setting")
            check = ""

        elif check == 2 :
            line = line.replace(' ', "")
            if 'max_request_body_size=114688' in line :
                max_request['status']=0
                max_request['data'] = line.split("\n")[0]
            elif 'max_request_body_size' not in line :
                max_request['status']=2
                max_request['data'] = "None"
            check = ""

        elif check == 3 :
            line = line.replace(' ', "")
            if 'admin_token=<None>' in line :
                admin_token['status'] = 0
                admin_token['data'] = line.split("\n")[0]
            elif 'admin_token=<None>' not in line :
                admin_token['status']=2
                admin_token['data'] = "None"

            check = ""
        else :
            pass

    data = {
         "2.1.4.9" : max_request,
         "2.1.4.13" : admin_token,
         "2.1.4.15" : provider
    }
    return data
def keystone_checklist(path) :

    path = os.path.dirname(os.path.abspath(__file__))
#    result = subprocess.run([path + "/keystone_ower_check.sh"], stdout=subprocess.PIPE)
#    result2 = subprocess.run([path + "/keystone_right_check.sh"], stdout=subprocess.PIPE)
#    keystone_ower = result.stdout.decode("UTF-8")
#    keystone_right = result2.stdout.decode("UTF-8")

#    keystone_right_check(keystone_right)
#    keystone_ower_check(keystone_ower)
    keystone_checklist = keystone_conf_check()
    return keystone_checklist

 
