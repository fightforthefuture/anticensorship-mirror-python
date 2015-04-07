# handle imports
import os, time
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, jsonify, Response
from access_control_decorator import crossdomain
import maxminddb

# defines
MOTHERSHIP_URL = os.environ.get('MOTHERSHIP_URL',
                    'https://anticensorship.herokuapp.com')

# create flask application
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    JSON_AS_ASCII=False
))
app.config.from_object('config.Config')

def fix_ip(ip_address):
    """Fixes an ugly, broken IP address string that came from Heroku"""

    if "," in ip_address:
        ips = ip_address.split(", ")
        ip_address = ips[0]

    return ip_address

@app.route('/', methods=['GET', 'POST'])
@crossdomain(origin='*')
def mirror():
    """Get the encrypted anti-censorship data from Mothership"""

    import urllib

    v = request.values.get
    ip = fix_ip(request.headers.get('x-forwarded-for', request.remote_addr))

    reader = maxminddb.open_database('GeoLite2-City.mmdb')
    result = reader.get(ip)
    reader.close()

    if v("_ac_force_locale") or (result and result.get('country')):

        locale = v("_ac_force_locale") if v("_ac_force_locale") else \
                 result.get("country").get('iso_code')

        link = "%s/%s?api_key=%s&domain=%s&user_key=%s" % (MOTHERSHIP_URL,
               locale, os.environ.get('API_KEY'), os.environ.get('DOMAIN'),
               v("key"))

        f = urllib.urlopen(link)
        encrypted_data = f.read()
        return encrypted_data

    return ""

@app.route('/report', methods=['POST'])
@crossdomain(origin='*')
def report():
    """Report something sketchy back to Mothership"""

    import urllib
    import requests

    v = request.values.get
    ip = fix_ip(request.headers.get('x-forwarded-for', request.remote_addr))

    reader = maxminddb.open_database('GeoLite2-City.mmdb')
    result = reader.get(ip)
    reader.close()

    payload = {
        'ip': ip,
        'host': v('host'),
        'response': v('response')
    }
    if result and result.get('country'):
        payload['locale'] = result.get("country").get('iso_code')

    r = requests.post(MOTHERSHIP_URL + "/report", data=payload)
    print r.text

    return "kthx"

@app.route('/helo', methods=['GET'])
@crossdomain(origin='*')
def ping():
    """Returns a ping response to Mothership server"""

    import hashlib

    challenge       = request.values.get('challenge', ''),
    gen_response    = "%s%s" % (os.environ.get('API_KEY'), challenge[0])
    response        = hashlib.sha1(gen_response).hexdigest()
    return response

if __name__ == '__main__':
    if app.config['DEBUG'] == True:
        print 'Debug mode active'
        app.run('0.0.0.0', 9001)
    else:
        app.run()