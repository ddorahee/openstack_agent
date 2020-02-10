import subprocess

def horizon_checkfile() :
    result = subprocess.run(["./horizon_check.sh"], stdout=subprocess.PIPE)
    horizon_conf = result.stdout.decode("UTF-8")
    horizon_conf = horizon_conf.upper().replace(" ", "") 
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



horizon_checkfile()


