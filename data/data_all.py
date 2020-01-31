import requests
import os
from .compute.compute_data import get_compute_data
from .terraform_openstack.openstack_terraform import make_terraform_provider

def make_credentials_info(api_dict) :
    OS_PROJECT_DOMAIN_ID = api_dict['OS_PROJECT_DOMAIN_ID']
    OS_USERNAME = api_dict['OS_USERNAME']
    OS_PASSWORD = api_dict['OS_PASSWORD']
    OS_ADMIN_ID = api_dict['OS_ADMIN_ID']
    OS_AUTH_URL = api_dict['OS_AUTH_URL']

    return OS_PROJECT_DOMAIN_ID, OS_USERNAME, OS_PASSWORD, OS_ADMIN_ID, OS_AUTH_URL

def create_credentials_token(OS_PROJECT_DOMAIN_ID, OS_USERNAME, OS_PASSWORD, OS_ADMIN_ID, OS_AUTH_URL) :
    print("Create Credentials Token")

    data = '{"auth": {"identity": {"methods": ["password"],"password": {"user": {"id":"' + OS_ADMIN_ID + '","password":"' + OS_PASSWORD + '"}}},"scope": {"project": {"domain": {"id":"' + OS_PROJECT_DOMAIN_ID + '"},"name":"' + OS_USERNAME + '"}}}}'
    try:
        res = requests.post(OS_AUTH_URL+':5000/v3/auth/tokens', data=data)
        token = res.headers['X-Subject-token']

    except Exception as ex:
        print(ex)
    print("Complate Credentials Token")
    return token



def data_all(api_dict) : 
    OS_PROJECT_DOMAIN_ID, OS_USERNAME, OS_PASSWORD, OS_ADMIN_ID, OS_AUTH_URL = make_credentials_info(api_dict)
    print("GET Openstack All data")
    OS_TOKEN = create_credentials_token(OS_PROJECT_DOMAIN_ID, OS_USERNAME, OS_PASSWORD, OS_ADMIN_ID, OS_AUTH_URL)
    print("Create terraform openstack provider")
    make_terraform_provider(OS_TOKEN, OS_AUTH_URL)
    print("Complete terraform openstack provider")
    print("Get Compute Data")
    
    compute = get_compute_data(OS_PROJECT_DOMAIN_ID, OS_USERNAME, OS_PASSWORD, OS_ADMIN_ID, OS_AUTH_URL, OS_TOKEN)
    print("Complete Compute Data")
    
    return compute

