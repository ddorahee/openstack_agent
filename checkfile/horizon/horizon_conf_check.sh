#!/bin/sh

grep 'DISALLOW_IFRAME_EMBED' /etc/openstack-dashboard/local_settings
grep 'CSRF_COOKIE_SECURE' /etc/openstack-dashboard/local_settings
grep 'SESSION_COOKIE_SECURE' /etc/openstack-dashboard/local_settings
grep 'SESSION_COOKIE_HTTPONLY' /etc/openstack-dashboard/local_settings
grep 'PASSWORD_AUTOCOMPLET' /etc/openstack-dashboard/local_settings
grep 'DISABLE_PASSWORD_REVEAL' /etc/openstack-dashboard/local_settings
grep 'ENFORCE_PASSWORD_CHECK' /etc/openstack-dashboard/local_settings
grep 'SECURE_PROXY_SSL_HEADER' /etc/openstack-dashboard/local_settings


