import subprocess

def keystone_checklist() :
    result = subprocess.run(["./keystone_ower.sh"], stdout=subprocess.PIPE)
    keystone_ower = result.stdout.decode("UTF-8")

    
    if "root" in keystone_ower : 
       print("None")
keystone_checklist()
