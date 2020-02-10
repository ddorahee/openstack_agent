#!/bin/sh

stat -L -c "%U %G" /etc/keystone
stat -L -c "%U %G" /etc/keystone/keystone.conf 
stat -L -c "%U %G" /etc/keystone/keystone-paste.ini
stat -L -c "%U %G" /etc/keystone/policy.json
stat -L -c "%U %G" /etc/keystone/logging.conf
stat -L -c "%U %G" /etc/keystone/ssl/certs/signing_cert.pem
stat -L -c "%U %G" /etc/keystone/ssl/private/signing_key.pem
stat -L -c "%U %G" /etc/keystone/ssl/certs/ca.pem
 

