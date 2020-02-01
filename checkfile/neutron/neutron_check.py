import subprocess

def neutron_checklist() :
    result = subprocess.run(["cat","/etc/neutron/neutron.conf"], stdout=subprocess.PIPE)
    neutron_conf = result.stdout.decode("UTF-8")

    if "auth_url" in neutron_conf :
        print("asd")


