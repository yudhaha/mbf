#!/usr/bin/python3
# coding=utf-8

#######################################################
# File           : run.py                             #
# Author         : DulLah                             #
# Github         : https://github.com/dz-id           #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/DulLah                #
# Python version : 3.8+                               #
#######################################################
#         RECODE? OKE CANTUMKAN NAMA PEMBUAT          #
#######################################################

import shutil, platform

py_version = platform.python_version()

if py_version < '3.7':
   

cache = ['src/__pycache__', 'src/data/__pycache__']

for path in cache:
    try:
        shutil.rmtree(path)
    except:
        pass

__import__('src.app')
