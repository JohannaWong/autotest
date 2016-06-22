import urllib
import urllib2
import cookielib
import base64
import re
import json
import hashlib

cj=cookielib.LWPCookieJar()

cookie_support=urllib2.HTTPCookieProcessor(cj)

opener=urllib2.build_opener(cookie_support,urllib2.HTTPHandler)

urllib2.install_opener(opener)

postdata={
	
}


def main():
	username='w2259367'
	pwd='19870918'
	url=''
