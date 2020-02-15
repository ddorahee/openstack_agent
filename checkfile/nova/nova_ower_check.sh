#!/bin/sh

stat -L -c "%U %G" /etc/nova
stat -L -c "%U %G" /etc/nova/nova.conf
stat -L -c "%U %G" /etc/nova/api-paste.ini
stat -L -c "%U %G" /etc/nova/policy.json
stat -L -c "%U %G" /etc/nova/rootwrap.conf


 

