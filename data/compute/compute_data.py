import requests


def set_request(OS_AUTH_URL, OS_TOKEN,PORT):
    try:
        headers = {'X-Auth_Token': OS_TOKEN}
        res = requests.get(OS_AUTH_URL+":"+PORT, headers=headers)
        return res.json()

    except Exception as ex:
        print(ex)


def create_credentials_token(OS_PROJECT_DOMAIN_ID, OS_USERNAME, OS_PASSWORD, OS_ADMIN_ID, OS_AUTH_URL) :
    print("Create Credentials Token...[]")

    data = '{"auth": {"identity": {"methods": ["password"],"password": {"user": {"id":"' + OS_ADMIN_ID + '","password":"' + OS_PASSWORD + '"}}},"scope": {"project": {"domain": {"id":"' + OS_PROJECT_DOMAIN_ID + '"},"name":"' + OS_USERNAME + '"}}}}'
    try:
        res = requests.post(OS_AUTH_URL+':5000/v3/auth/tokens', data=data)
        token = res.headers['X-Subject-token']

    except Exception as ex:
        print(ex)
    print("Create Credentials Token...[OK]")
    return token

def create_compute_data(OS_AUTH_URL, OS_TOKEN, PORT) :
    compute_res = set_request(OS_AUTH_URL, OS_TOKEN, PORT)

    return [{
      "mode": "data",
      "type": "openstack_compute_instance_v2",
      "name": "basic",
      "provider": "provider.openstack",
      "instances": [{
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
      }for data in compute_res['servers']]
    }]
    

def get_compute_data(OS_PROJECT_DOMAIN_ID, OS_USERNAME, OS_PASSWORD, OS_ADMIN_ID, OS_AUTH_URL) : 
    OS_TOKEN=create_credentials_token(OS_PROJECT_DOMAIN_ID, OS_USERNAME, OS_PASSWORD, OS_ADMIN_ID, OS_AUTH_URL)
    instance_res = create_compute_data(OS_AUTH_URL, OS_TOKEN, "8774/v2.1/servers/detail")

    return instance_res
