import requests
import os
from data.compute.compute_data import get_compute_data
from data.terraform_openstack.openstack_terraform import Terraform

def create_credentials_token(key) :
    print("Create Credentials Token")

    data = '{"auth": {"identity": {"methods": ["password"],"password": {"user": {"id":"' + key['OS_ADMIN_ID'] + '","password":"' + key['OS_PASSWORD'] + '"}}},"scope": {"project": {"domain": {"id":"' + key['OS_PROJECT_DOMAIN_ID'] + '"},"name":"' + key['OS_USERNAME'] + '"}}}}'
    try:
        res = requests.post(key['OS_AUTH_URL']+':5000/v3/auth/tokens', data=data)
        token = res.headers['X-Subject-token']

    except Exception as ex:
        print(ex)
    print("Complate Credentials Token")
    return token



def openstack_data_all(key) :
    path = os.path.dirname(os.path.abspath('.')) + "./data/terraform_openstack/"
    print("GET Openstack All data")
    OS_TOKEN = create_credentials_token(key)
    print("Create terraform openstack provider")
    Terraform.make_terraform_provider(path+"compute/",key['OS_AUTH_URL'],OS_TOKEN)
    Terraform.make_terraform_provider (path + "network/", key['OS_AUTH_URL'], OS_TOKEN)
    Terraform.make_terraform_provider (path + "database/", key['OS_AUTH_URL'], OS_TOKEN)
    Terraform.make_terraform_provider (path + "storage/", key['OS_AUTH_URL'], OS_TOKEN)

    print("Complete terraform openstack provider")
    print("Get Compute Data")
    compute = get_compute_data(path + "compute/",key, OS_TOKEN)
    print("Complete Compute Data")
    
    return compute

