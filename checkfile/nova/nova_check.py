import os 


def nova_checklist() : 
    f = open("/etc/nova/nova.conf", "r")
    lines=f.readline()
    for line in lines :
        if line == "" :
            pass
