#!/usr/bin/env python

###
#
# This Python script showcases and tests Montastic (https://montastic.com) REST API.
#
# Usage - see help: ./montastic-api-tests.py
#
# Public domain.    
#
##
import requests # pipenv install requests
import sys

dn = 'https://montastic.com'

#
#
# Print a "." w/o a carriage return
def showProgress():
    sys.stdout.write(".") # write w/o \n
    sys.stdout.flush()

if len(sys.argv) < 2: 
    sys.exit("Usage: %s <api-key> [server domain name (e.g.: http://localhost:3000), default: https://montastic.com]" % sys.argv[0])

goodKey = sys.argv[1] # get API key

if len(sys.argv) >= 3: 
    dn = sys.argv[2] # get hostname

print("Using DN: %s" % dn)

#
# Montastic checkpoint endpoint / URL
# 
apiUrl = dn + '/checkpoints'

headers = {'X-API-KEY': goodKey, 'Accept': 'application/json', 'Content-Type': 'application/json'}


#
# 
# get checkpoints OK w/ good key
showProgress()
r = requests.get(apiUrl, headers=headers)
assert r.status_code == 200, "Error getting list. Expected 200, got: %d" % r.status_code
beforeAllCheckpoints=r.json()

#
# 
# get w/ bad key => error 403
headers['X-API-KEY'] = 'badkey'
showProgress()
r = requests.get(apiUrl, headers=headers)
assert r.status_code == 403, "Should get bad key error, got: %d" % r.status_code

headers['X-API-KEY']=goodKey # use good key from now on

#
# 
# create checkpoint OK
showProgress()
data = {'url': 'https://www.daskeyboard.com/'}
r = requests.post(apiUrl, json=data, headers=headers)
assert r.status_code == 201, "Error creating: expected 200, got: %d. Make sure this Montastic plan is not maxed out." % r.status_code
checkpoint = r.json()

# 
# 
# delete newly created checkpoint
showProgress()
url = dn+'/checkpoints/%s' % checkpoint['id']
r = requests.delete(url, headers=headers)
assert r.status_code == 204, "Error deleting: expected 204, got: %d." % r.status_code

#
# 
# create checkpoint with keyword verification
showProgress()
data = {'url': 'https://www.daskeyboard.com/', 'grep_this': 'keyboard', 'grep_presence': 'true'}
r = requests.post(apiUrl, json=data, headers=headers)
assert r.status_code == 201, "Expected 200, got: %d. Make sure this Montastic plan is not maxed out." % r.status_code
checkpoint = r.json()
assert checkpoint['grep_this']=='keyboard', 'Wrong keyword, found: %s' % checkpoint['grep_this']
assert checkpoint['grep_presence'] == True , 'Wrong grep presence, found: %s' % checkpoint['grep_presence']

#
# 
# delete newly created checkpoint
showProgress()
url = dn+'/checkpoints/%s' % checkpoint['id']
r = requests.delete(url, headers=headers)
assert r.status_code == 204, "Error deleting: expected 204, got: %d." % r.status_code


#
# 
# create checkpoint with absence of keyword verification
showProgress()
data = {'url': 'https://www.daskeyboard.com/', 'grep_this': 'logitech', 'grep_presence': False}
r = requests.post(apiUrl, json=data, headers=headers)
assert r.status_code == 201, "Expected 201, got: %d. Make sure this Montastic plan is not maxed out." % r.status_code
checkpoint = r.json()
assert checkpoint['grep_this']=='logitech', 'Wrong keyword, found: %s' % checkpoint['grep_this']
assert checkpoint['grep_presence'] == False , 'Wrong grep presence, found: %s' % checkpoint['grep_presence']

#
# 
# update checkpoint
showProgress()
data = {'name':'my hobby website'}
url = dn+'/checkpoints/%s' % checkpoint['id']
r = requests.patch(url)

#
# 
# delete newly created checkpoint
showProgress()
url = dn+'/checkpoints/%s' % checkpoint['id']
r = requests.delete(url, headers=headers)
assert r.status_code == 204, "Error deleting: expected 204, got: %d." % r.status_code


#
# 
# compare with beforeAllCheckpoints count with new count
showProgress()
r = requests.get(apiUrl, headers=headers)
assert r.status_code == 200, "Expected 200, got: %d" % r.status_code
assert len(beforeAllCheckpoints) == len(r.json())

print("\n==================")
print("==== TESTS OK ====")
print("==================\n")
