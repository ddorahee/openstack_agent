from checkfile.nova.nova_check import nova_checklist
from checkfile.neutron.neutron_check import neutron_checklist
from checkfile.keystone.keystone_check import keystone_checklist
from checkfile.horizon.horizon_check import horizon_checklist


def openstack_check_all_file() :
    check_file = {
        "Nova": [],
        "Neutron": [],
    } 
    print("All File Check")
    horizon_checklist()
    check_file['Neutron'].append(neutron_checklist)
    print("Complate File Check")
    return check_file
