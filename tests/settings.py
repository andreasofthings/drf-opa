#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 et sw=4 sts=4

SECRET_KEY = 'fake-key'
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "test.db"
    }
}
INSTALLED_APPS = [
    "drf-opa",
    "rest_framework",
    "tests",
]
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.OpenPolicyPermission',
    ]
}
