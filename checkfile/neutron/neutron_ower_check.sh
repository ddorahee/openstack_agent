#!/bin/sh

stat -L -c "%U %G" /etc/neutron
stat -L -c "%U %G" /etc/neutron/neutron.conf
stat -L -c "%U %G" /etc/neutron/policy.json
stat -L -c "%U %G" /etc/neutron/rootwrap.conf
stat -L -c "%U %G" /etc/neutron/api-paste.ini



 

