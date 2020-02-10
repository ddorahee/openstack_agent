import subprocess 

def horizon_right_check(horizon_right) :
    horizon_right = horizon_right.split("\n")
    if "/etc/openstack-dashboard/local_settings" in horizon_right[0] :
        if "-rw-r--r--" in horizon_right[0] : 
             print("localseggintgright")
        else : 
             print("right False")

def horizon_conf_check(horizon_conf) :
    if "#DISALLOW_IFRAME_EMBED=TRUE" in horizon_conf :
        print("1none")
    elif "DISALLOW_IFRAME_EMBED=TRUE" in horizon_conf :
        print("1")
    else :
        print("a")

    if "#CSRF_COOKIE_SECURE=TRUE" in horizon_conf:
        print("2none")
    elif "CSRF_COOKE_SECURE=TRUE" in horizon_conf :
        print("2")
    else :
        print("b")

    if "#SESSION_COOKIE_SECURE=TRUE" in horizon_conf :
        print("3none")
    elif "SESSION_COOKIE_SECURE=TRUE" in horizon_conf :
        print("3")
    else :
        print("c")

    if "#SESSION_COOKIE_HTTPONLY=TRUE" in horizon_conf :
        print("4none")
    elif "SESSION_COOKIE_HTTPONLY=TRUE" in horizon_conf :
        print("4")
    else :
        print("d")

    if "#PASSWORD_AUTOCOMPLET=OFF" in horizon_conf :
        print("5none")
    elif "PASSWORD_AUTOCOMPLET=OFF" in horizon_conf :
        print("5")
    else :
        print("e")

    if "#DISABLE_PASSWORD_REVEAL=TRUE" in horizon_conf :
        print("6none")
    elif "DISABLE_PASSWORD_REVEAL=TRUE" in horizon_conf :
        print("6")
    else :
        print("f")

    if "#ENFORCE_PASSWORD_CHECK=TRUE" in horizon_conf :
        print("7none")
    if "ENFORCE_PASSWORD_CHECK=TRUE" in horizon_conf :
        print("7")
    else :
        print("g")

    if "#SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO','HTTPS')" in horizon_conf :
        print("8none")
    elif "SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO','HTTPS')" in horizon_conf :
        print("8")
    else :
        print("h")

def horizon_checklist() :
    result = subprocess.run(["./checkfile/horizon/horizon_conf_check.sh"], stdout=subprocess.PIPE)
    result2 = subprocess.run(["./checkfile/horizon/horizon_right_check.sh"], stdout=subprocess.PIPE)
    horizon_conf = result.stdout.decode("UTF-8")
    horizon_right = result2.stdout.decode("UTF-8")
    horizon_conf = horizon_conf.upper().replace(" ", "")

    horizon_right_check(horizon_right)
    horizon_conf_check(horizon_conf)

