from .nova.nova_check import nova_checklist
from .neutron.neutron_check import neutron_checklist

def get_nova_check() : 
    print("Nova Check")
    nova=nova_checklist()
def get_keystone_check() : 
    print("Keystone Check")

def get_neutron_check() : 
    print("Neutron Check")
    neutron=neutron_checklist()

    return neutron

def get_cinder_check() : 
    print("Cinder Check")

def get_swift_check() : 
    print("Swift Check")

def check_all_file() :
    check_file = {
        "Nova": [],
        "Neutron": [],
    } 
    print("All File Check")
    get_nova_check()
    get_keystone_check()
    neutron=get_neutron_check()
    get_cinder_check()
    get_swift_check()

    check_file['Neutron'].append(neutron)

    return check_file
