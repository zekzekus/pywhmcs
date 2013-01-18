# -*- coding: utf-8 -*-

import logging as log
import requests
import hashlib


def invoke(url, username, password, action, format, parameters):
    content_type = "application/%s" % format
    headers = {'content-type': content_type}

    payload = {
        'username': username,
        'password': hashlib.md5(password).hexdigest(),
        'responsetype': format,
        'action': action}
    payload.update(parameters)
    log.debug("PAYLOAD: %s" % payload)

    r = requests.post(url, data=payload)
    print "%s" % r.text
    return (r.status_code, r.text)
