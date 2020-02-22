import requests
import json
from data.terraform_openstack.openstack_terraform import Terraform


def set_request(key, OS_TOKEN,PORT):
    try:
        headers = {'X-Auth_Token': OS_TOKEN}
        res = requests.get(key['OS_AUTH_URL']+":"+PORT, headers=headers)
        return res.json()

    except Exception as ex:
        print(ex)


def make_network_terraform(path, network_list) : 
    tf = open(path + "network.tf", 'w')
    content = ''
    for network in network_list:
        content += 'data "openstack_networking_network_v2" "%s" {\n\t' \
                   'name = "%s"\n}\n' % (network, network)
    tf.write(content)
    tf.close() 
    pass

def openstack_network_terraform(path, network_list):
    make_network_terraform(path, network_list)
    Terraform.terraform_init(path)
    Terraform.terraform_plan(path)
    Terraform.terraform_apply(path)

def create_network_data(key, OS_TOKEN, PORT) :
    network_datas = set_request(key, OS_TOKEN, PORT)

    return network_datas
    
def openstack_network_data(path, key, OS_TOKEN) :
    network_list = []
    network_res = create_network_data(key, OS_TOKEN, "9696/v2.0/networks")
    for data in network_res['networks'] : 
        network_list.append(data['name'])


    openstack_network_terraform(path, network_list)

    terraform_data = Terraform.get_tfstate(path)
    terraform_data = json.loads(terraform_data)

    return terraform_data
