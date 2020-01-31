def neutron_checklist() :
    f = open("/etc/neutron/neutron.conf", "r")
    lines=f.readline()
    for line in lines :
        if line == "" :
            pass
 
