import os
def make_terraform_provider(OS_TOKEN, OS_AUTH_URL) :
    f = open(".openstack_provider.tf", 'w')
    code = 'provider "openstack" {\n\t'
    code += 'auth_url='+'"'+OS_AUTH_URL+':5000"\n\t'
    code += "token="+'"'+OS_TOKEN+'"\n}'
    f.write(code)
    f.close()
    os.system("./terraform init")

