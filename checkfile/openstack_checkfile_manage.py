import os
from checkfile.nova.nova_check import nova_checklist
from checkfile.neutron.neutron_check import neutron_checklist
from checkfile.keystone.keystone_check import keystone_checklist
from checkfile.horizon.horizon_check import horizon_checklist


def openstack_check_all_file() :
    path = os.path.dirname(os.path.abspath(__file__))
    check_file = {
        "compute": [],
        "iam" : [],
        "network": [],
        "storage" : [],
        "database" : []
    } 
    print("All File Check")
    check_file['iam'].append(keystone_checklist(path + "/keystone/"))
    print("Complate File Check")
    return check_file
