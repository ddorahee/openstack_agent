import os

class Terraform:
    @staticmethod
    def make_terraform_provider(path, key, OS_TOKEN) :
        if not(os.path.isdir(path)):
            os.makedirs(os.path.join(path))

        try :
            provider = open(path + "provider.tf", 'w')
            content = 'provider "openstack" {\n\t auth_url = "%s" \n\t token = "%s"\n\t \n}' % \
                        (key['OS_AUTH_URL']+"5000", OS_TOKEN)
            provider.write(content)
            provider.close()
            return True
        except Exception as e:
            print(e)
            return False
    @staticmethod
    def terraform_init(path):
        os.system("./terraform init " + path)

    @staticmethod
    def terraform_plan(path):
        os.system("./terraform plan -out " + path + "/tf.plan " + path)

    @staticmethod
    def terraform_apply(path):
        os.system("./terraform apply -state-out " + path + "/tf.tfstate " + path)

    @staticmethod
    def get_tfstate(path):
        tfstate = open(path + "tf.tfstate", 'r')
        data = tfstate.read()
        tfstate.close()
        return data
