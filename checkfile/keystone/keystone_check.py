import subprocess

def keystone_ower_check(keystone_ower) :
    keystone_ower = keystone_ower.split("\n")
 
    if "keystone keystone" in keystone_ower[0] :
        print("keystone keystone ower")
    else :
        print("root ower")

    if "keystone keystone" in keystone_ower[1] :
        print("keystone_conf keystone ower")
    else : 
        print("root ower")

    if "keystone keystone" in keystone_ower[2] :
        print("keystone-paste.ini keystone ower")
    else :
        print("root ower")

    if "keystone keystone" in keystone_ower[3] :
        print("policy.json keystone ower")
    else :
        print("root ower")

    if "keystone keystone" in keystone_ower[4] :
        print("logging.conf keystone ower")
    else :
        print("root ower")

def keystone_checklist() :
    result = subprocess.run(["./keystone_ower_check.sh"], stdout=subprocess.PIPE)
    keystone_ower = result.stdout.decode("UTF-8")

#    keystone_ower_check(keystone_ower)

#keystone_checklist()
 
