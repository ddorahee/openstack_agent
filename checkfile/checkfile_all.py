from .nova.nova_check import nova_checklist
from .neutron.neutron_check import neutron_checklist

def get_nova_check() :
    print("----------------------") 
    print("Nova Check")
    nova=nova_checklist()
    print("Complete Nova Check")
    print("----------------------\n")

def get_keystone_check() : 
    print("----------------------")
    print("Keystone Check")
    print("Complete Keystone Check")
    print("----------------------\n")

def get_neutron_check() : 
    print("----------------------")
    print("Neutron Check")
    neutron=neutron_checklist()
    print("Complete Neutron Check")
    print("----------------------\n")

    return neutron

def get_cinder_check() : 
    print("----------------------")
    print("Cinder Check")
    print("Complete Cinder Check")
    print("----------------------\n")


def get_swift_check() : 
    print("----------------------")
    print("Swift Check")
    print("Complete Swift Check")
    print("----------------------\n")


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
    print("Complate File Check")
    return check_file
