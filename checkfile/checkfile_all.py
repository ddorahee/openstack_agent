from .nova.nova_check import nova_checklist

def get_nova_check() : 
    print("Nova Check")
    a=nova_checklist()
    print(a)
def get_keystone_check() : 
    print("Keystone Check")

def get_neutron_check() : 
    print("Neutron Check")

def get_cinder_check() : 
    print("Cinder Check")

def get_swift_check() : 
    print("Swift Check")

def check_all_file() : 
    print("All File Check")
    get_nova_check()
    get_keystone_check()
    get_neutron_check()
    get_cinder_check()
    get_swift_check()
