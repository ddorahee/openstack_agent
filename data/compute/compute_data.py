import requests


def set_request(key, OS_TOKEN,PORT):
    try:
        headers = {'X-Auth_Token': OS_TOKEN}
        res = requests.get(key['OS_AUTH_URL']+":"+PORT, headers=headers)
        return res.json()

    except Exception as ex:
        print(ex)


def create_compute_data(key, OS_TOKEN, PORT) :
    compute_datas = set_request(key, OS_TOKEN, PORT)
    return {
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
      }for data in compute_datas['servers']]
    }
    
def get_compute_data(key, OS_TOKEN) :
    instance_res = create_compute_data(key, OS_TOKEN, "8774/v2.1/servers/detail")

    return instance_res
