# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 03:06:21 2021

@author: Rogue
"""

import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib ## http.cookiejar in python3

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://id.arduino.cc/auth/login/")

br.select_form(nr=0)
br.form['username'] = 'username'
br.form['password'] = 'password.'
br.submit()

