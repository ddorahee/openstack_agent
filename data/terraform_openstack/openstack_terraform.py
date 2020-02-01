import os
import subprocess

def make_terraform_provider(OS_TOKEN, OS_AUTH_URL) :
    f = open(".openstack_provider.tf", 'w')
    code = 'provider "openstack" {\n\t'
    code += 'auth_url='+'"'+OS_AUTH_URL+':5000"\n\t'
    code += "token="+'"'+OS_TOKEN+'"\n}'
    f.write(code)
    f.close()
    result = subprocess.check_output ('./data/terraform_openstack/terraform init ./data/terraform_openstack/' , shell=True)
    result = result.decode("UTF-8")

def create_network_provider() : 
    f = open(".openstack_network.tf", 'w')

