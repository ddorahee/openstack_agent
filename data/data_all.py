from .compute.compute_data import get_compute_data

def make_credentials_info(api_dict) :
    OS_PROJECT_DOMAIN_ID = api_dict['OS_PROJECT_DOMAIN_ID']
    OS_USERNAME = api_dict['OS_USERNAME']
    OS_PASSWORD = api_dict['OS_PASSWORD']
    OS_ADMIN_ID = api_dict['OS_ADMIN_ID']
    OS_AUTH_URL = api_dict['OS_AUTH_URL']

    return OS_PROJECT_DOMAIN_ID, OS_USERNAME, OS_PASSWORD, OS_ADMIN_ID, OS_AUTH_URL

def data_all(api_dict) : 
    OS_PROJECT_DOMAIN_ID, OS_USERNAME, OS_PASSWORD, OS_ADMIN_ID, OS_AUTH_URL = make_credentials_info(api_dict)
    print("GET Openstack All data")
    print("Get Compute Data")
    compute = get_compute_data(OS_PROJECT_DOMAIN_ID, OS_USERNAME, OS_PASSWORD, OS_ADMIN_ID, OS_AUTH_URL)
    print("Complete Compute Data")
    
    return compute

