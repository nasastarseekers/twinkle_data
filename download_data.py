import requests
import pandas as pd
# from __future__ import print_function, division
from PyAstronomy import pyasl
import bs4
import matplotlib.pyplot as plt


response = requests.get('https://brite.camk.edu.pl/pub/index.html')
web_info = response.text
soup = bs4.BeautifulSoup(web_info,'lxml')
print(soup)


'02-Cen-I-2014_DR2/HD120307_02-Cen-I-2014_BAb_setup4_APa2s5_DR2.dat',
'02-Cen-I-2014_DR2/HD120324_02-Cen-I-2014_BAb_setup4_APa2s5_DR2.dat',
'02-Cen-I-2014_DR2/HD121263_02-Cen-I-2014_BAb_setup4_APa2s5_DR2.dat',
'02-Cen-I-2014_DR2/HD120307_02-Cen-I-2014_BAb_setup4_APa2s5_DR2.dat',
'02-Cen-I-2014_DR2/HD121743_02-Cen-I-2014_BAb_setup4_APa2s5_DR2.dat',
'02-Cen-I-2014_DR2/HD121790_02-Cen-I-2014_BAb_setup4_APa2s5_DR2.dat',
'02-Cen-I-2014_DR2/HD122451_02-Cen-I-2014_BAb_setup4_APa2s5_DR2.dat',
'02-Cen-I-2014_DR2/HD122980_02-Cen-I-2014_BAb_setup4_APa2s5_DR2.dat',
'02-Cen-I-2014_DR2/HD125238_02-Cen-I-2014_BAb_setup4_APa2s5_DR2.dat',
'02-Cen-I-2014_DR2/HD125823_02-Cen-I-2014_BAb_setup4_APa2s5_DR2.dat'

