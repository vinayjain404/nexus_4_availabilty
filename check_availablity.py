import datetime
import pdb
import time
import urllib

from send_mail import send

# Query every five minutes for a start
DEFAULT_DELAY = 5 * 60
NEXUS_4_GOOGLE_URL = "https://play.google.com/store/devices/details?id=nexus_4_8gb&feature=microsite&hl=en"

# TODO (vinayjain) Add a way to dynamically fetch a working proxy from
# http://www.proxynova.com/proxy-server-list/?pxl=e
PROXY_URL = "http://66.132.251.111:80"

def check_availability():
    delay = DEFAULT_DELAY
    while True:
        try:
            log("Querying the page")
            proxies = {'http': PROXY_URL}
            response = urllib.urlopen(NEXUS_4_GOOGLE_URL, proxies=proxies)
            page = response.read()
            if 'sold out' in page.lower():
                log("sold out")
            elif 'add to cart' in page.lower():
                log("available")
                send(NEXUS_4_GOOGLE_URL)
                log("Mail sent")
                delay = 86400
            else:
                log("No clear response: ")
                log(page)
        except:
            log("Exception")
            traceback.print_exc()
        finally:
            time.sleep(delay)

def log(msg):
    """ hackish logging"""
    now = datetime.datetime.now()
    cur_time = now.strftime("%Y-%m-%d %H:%M")
    print "%s: %s" %(cur_time, msg)

if __name__ == "__main__":
	check_availability()
