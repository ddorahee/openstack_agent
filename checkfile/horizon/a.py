def horizon_checkfile() :
    f = open("/etc/openstack-dashboard/local_settings", 'r')
    lines = f.readlines()
    

    for line in lines :
        if "#DISALLOW_IFRAME_EMBED" in line : 
            print("1 False")
        elif "DISALLOW_IFRAME_EMBED" in line : 
            if "DISALLOW_IFRAME_EMBED = TRUE" in line.upper() :
                print("1 True")

        elif "#CSRF_COOKIE_SECURE" in line : 
            print("2 False")
        elif "CSRF_COOKIE_SECURE" in line :
            if "CSRF_COOKIE_SECURE = TRUE" in line.upper() :
                print("2 True")

        elif "#SESSION_COOKIE_SECURE" in line :
            print("3 Flase")
        elif "SESSION_COOKIE_SECURE" in line :
            if "SESSION_COOKIE_SECURE = TRUE" in line.upper() :
                print("3 True")
        
        elif "#SESSION_COOKIE_HTTPONLY" in line :
            print("4 Flase")
        elif "SESSION_COOKIE_HTTPONLY" in line :
            if "SESSION_COOKIE_HTTPONLY = TRUE" in line.upper() :
                print("4 True")

        elif "#ENFORCE_PASSWORD_CHECK" in line :
            print("5 Flase")
        elif "ENFORCE_PASSWORD_CHECK" in line :
            if "ENFORCE_PASSWORD_CHECK = TRUE" in line.upper() : 
                print("5 True")

        elif "#SECURE_PROXY_SSL_HEADER" in line :
            print("6 Flase")
        elif "SECURE_PROXY_SSL_HEADER" in line :
            if "SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')" in line.upper() :
                print("6 True")



horizon_checkfile()
