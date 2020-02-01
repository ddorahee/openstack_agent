import subprocess

def neutron_checklist() :
    result = subprocess.run(["cat","/etc/neutron/neutron.conf"], stdout=subprocess.PIPE)
    neutron_conf = result.stdout.decode("UTF-8")

    if "auth_url = http:" in neutron_conf :
         neutron_point = "False"

    data = {
        "6.3.1.1" : {
            "Point" : neutron_point,
            "Data" : []
         },
    }
    return data

