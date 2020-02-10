import os

class Terraform:
    @staticmethod
    def make_terraform_provider(path, key, OS_TOKEN) :
        if not os.path.isdir (path):
            os.makedirs (os.path.join (path))

        try :
            f = open(path + "openstack_provider.tf", 'w')
            code = 'provider "openstack" {\n\t'
            code += 'auth_url='+'"'+key['OS_AUTH_URL']+':5000"\n\t'
            code += "token="+'"'+OS_TOKEN+'"\n}'
            f.write(code)
            f.close()
        except Exception as e:
            print(e)
            return False

        @staticmethod
        def terraform_init(path):
            os.system ("./data/terraform_openstack/terraform init ./data/terraform_openstack/" + path)

        @staticmethod
        def terraform_plan(path):
           os.system ("./data/terraform_openstack/terraform plan -out " + path + "/tf.plan " + path)

        @staticmethod
        def terraform_apply(path):
            os.system ("./data/terraform_openstack/terraform apply -state-out " + path + "/tf.tfstate " + path)

        @staticmethod
        def get_tfstate(path):
            tfstate = open (path + "tf.tfstate", 'r')
            data = tfstate.read ()
            tfstate.close ()
            return data