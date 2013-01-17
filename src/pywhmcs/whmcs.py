# -*- coding: utf-8 -*-

import logging as log
import requests
import hashlib
import simplejson as json


def invoke(url, username, password, action, parameters):
    headers = {'content-type': 'application/json'}

    payload = {
        'username': username,
        'password': hashlib.md5(password).hexdigest(),
        'responsetype': 'json',
        'action': action}
    payload.update(parameters)
    log.debug("PAYLOAD: %s" % payload)

    r = requests.post(url, data=payload)
    print "%s" % json.dumps(r.json(), sort_keys = False, indent = 4)
    return (r.status_code, r.text)
