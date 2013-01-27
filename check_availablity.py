import pdb
import urllib

NEXUS_4_GOOGLE_URL = "https://play.google.com/store/devices/details?id=nexus_4_8gb&feature=microsite&hl=en"
# TODO (vinayjain) Add a way to dynamically fetch a working proxy from
# http://www.proxynova.com/proxy-server-list/?pxl=e
PROXY_URL = "http://66.132.251.111:80"

def check_availability():
    proxies = {'http': PROXY_URL}
    response = urllib.urlopen(NEXUS_4_GOOGLE_URL, proxies=proxies)
    page = response.read()
    if 'sold out' in page.lower():
        print "sold out"
    elif 'add to cart' in page.lower():
        print "available"
        send_email()
    else:
        print "no clear response"
        print page
def send_email():
   # TODO (vinayjain) Send mail via a mail server setup
   pass

if __name__ == "__main__":
	check_availability()
