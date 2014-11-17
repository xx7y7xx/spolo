#!/bin/python

import urllib2
import re

def gettxt():
    """all page txt"""
    try:
        username = "ci"
        password = "sp12345678"
        top_level_url = "http://glue.spolo.org"
        url = "http://glue.spolo.org/trac/glue/wiki/xuanran001-3.0/www?format=txt"

        # create a password manager
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

        # Add the username and password.
        # If we knew the realm, we could use it instead of None.
        password_mgr.add_password(None, top_level_url, username, password)

        handler = urllib2.HTTPBasicAuthHandler(password_mgr)

        # create "opener" (OpenerDirector instance)
        opener = urllib2.build_opener(handler)

        # use the opener to fetch a URL
        response = opener.open(url)

    except urllib2.HTTPError as e:
        msg = "URL : %s\n" % url
        msg += 'Server return code : %s' % e.code
        print(msg)
    #except e:
    #    print(('Unexpected exception thrown:', e))

    raw_data = response.read().decode('utf-8')
    #print raw_data

    # get all web page path
    ret = []
    for line in raw_data.splitlines():
        # page prefix is `-`
        m = re.search(r"`(.*)`", line)
        if m:
            name = m.group(1)
            print name
            ret.append(name)

    return ret


def main():
    print "main"
    gettxt()

if __name__ == "__main__":
    main()
