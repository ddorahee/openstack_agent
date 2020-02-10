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

def openstack_compute_terraform(path):
    Terraform.terraform_init(path)
    Terraform.terraform_plan(path)
    Terraform.terraform_apply(path)

def make_compute_terraform(path):
    tf = open(path + "tf.tfstate", 'w')
    data = '{ \n\t "version": 4, \n\t "terraform_version": "0.12.18",\n\t "serial": 4, \n\t "lineage": "c26695ac-9e77-5e65-36c9-1fd92a2a7592", \n\t "outputs": {}, \n\t "resources": []\n}'
    tf.write(data)
    tf.close()

def create_compute_data(key, OS_TOKEN, PORT) :
    compute_datas = set_request(key, OS_TOKEN, PORT)

    return compute_datas
    
def get_compute_data(path, key, OS_TOKEN) :
    make_compute_terraform(path)
    openstack_compute_terraform(path)
    instance_res = create_compute_data(key, OS_TOKEN, "8774/v2.1/servers/detail")

    terraform_data = Terraform.get_tfstate(path)
    terraform_data = json.loads(terraform_data)

    for data in instance_res['servers'] : 
        data =  {
           "mode": "data",
           "type": "openstack_compute_instance_v2",
           "name": "basic",
           "provider": "provider.openstack",
           "instances" : [{
              "status" : data['status'],
                  "attributes" : {
                      "id" : data['id'],
                      "name" : data['name'],
                      "network" : data['addresses'],
                      "key_pair" : data['key_name'],
                      "availability_zone" : data['OS-EXT-AZ:availability_zone'],
                      "security_groups" : data['security_groups'],
                      "block_device" : [],
                      "flavor_id" : data['flavor'],
                      "created" : data['created'],
                      }
            }]
        } 
        terraform_data['resources'].append(data)
    return terraform_data
