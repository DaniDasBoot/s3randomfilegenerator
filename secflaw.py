def secure_cookie_noncompliant():
    from http.cookies import SimpleCookie
    cookie = SimpleCookie()
    cookie['sample'] = "sample_value"
    # Noncompliant: the cookie is insecure.
    cookie['sample']['secure'] = 0
    print(cookie)
