#!/usr/bin/env python
from django.utils.crypto import get_random_string

"""
Django SECRET_KEY generator.
"""
chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
print(get_random_string(50, chars))
