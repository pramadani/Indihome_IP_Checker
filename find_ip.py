import urequests # type: ignore

def get_public_ip():
    response = urequests.get('http://api.ipify.org')
    ip = response.text
    response.close()
    return ip