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

def nova_right_check(nova_right)
    nova_right = nova_right.split("\n")

    if "etc" in nova_right[0] :
        if "drwxr-x---" in nova_right[0]:
            print("keystone folder True")
        else :
            print("keystone folder False")

  

def nova_checklist() : 
    result = subprocess.run(["./nova_ower_check.sh"], stdout=subprocess.PIPE)
    result2 = subprocess.run(["./nova_right_check.sh"], stdout=subprocess.PIPE)
    nova_ower = result.stdout.decode("UTF-8")
    nova_ower_check(nova_ower) 

    nova_right = result.stdout.decode("UTF-8")
    nova_right_check(nova_right)


nova_checklist()
