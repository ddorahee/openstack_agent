import subprocess

def neutron_right_check(neutron_right) : 
    if "neutron" in neutron_right[0] :
        if "drwxr-x--" in neutron_right[0] :
            print("logging.conf True")
        else :
            print("logging.conf False")

    if "rootwrap.conf" in neutron_right[1] :
        if "-rw-r----" in neutorn_right[1] :
            print("logging.conf True")
        else :
            print("logging.conf False")

    if "policy.json" in neutron_right[2] :
        if "-rw-r----" in neutron_right[2] :
            print("logging.conf True")
        else :
            print("logging.conf False")

    if "neutron.conf" in neutron_right[3] :
        if "-rw-r----" in neutron_right[3] :
            print("logging.conf True")
        else :
            print("logging.conf False")
    try : 
        if "api-paste.ini" in neutron_right[4] :
            if "-rw-r----" in neutron_right[4] :
                print("logging.conf True")
            else :
                print("logging.conf False")
    except Exception as e :
        print("No File")


def neutron_ower_check(neutron_ower) : 
    neutron_ower = neutron_ower.split("\n")
    if "root neutron" in keystone_ower[0] :
        print("nova folder root nova ower")
    else :
        print("None")

    if "root neutron" in neutron_ower[1] :
        print("nova conf root nova ower")
    else :
        print("None")


    if "root neutron" in neutron_ower[2] :
        print("nova conf root nova ower")
    else :
        print("None")

    if "root neutron" in neutron_ower[3] :
        print("nova conf root nova ower")
    else :
        print("None")
    try : 
        if "root neutron" in neutron_ower[4] :
            print("nova conf root nova ower")
        else :
            print("None")
    except Exception as e:
        print("None File")

def neutron_conf_check(neutron_conf):
    neutron_conf = neutron_conf.split("\n")
    neutron_conf.remove('')
    for conf in neutron_conf : 
        new_conf = conf.replace("#","##").replace(' ', '').lower()
        if new_conf[1] == "##" : 
            continue
        elif "auth_strategy=keystone" == new_conf :
            print("a")

        elif "use_ssl=true" == new_conf : 
            print("b")

        
 

def neutron_checklist(path) :
#    result = subprocess.run([path + "./neutron_ower_check.sh"], stdout=subprocess.PIPE)
#    result2 = subprocess.run([path + "./neutron_right_check.sh"], stdout=subprocess.PIPE)
    result3 = subprocess.run([path + "./neutron_conf_check.sh"], stdout=subprocess.PIPE)
#    neutron_ower = result.stdout.decode("UTF-8")
#    neutron_ower_check(neutron_ower)

    neutron_conf = result3.stdout.decode("UTF-8")
    neutron_conf_check(neutron_conf)

#    neutron_right = result2.stdout.decode("UTF-8")
#    neutron_right_check(neutron_right)


