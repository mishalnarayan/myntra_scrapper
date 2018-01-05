 # -*- coding: utf-8 -*-

import os
import sys
import threading
import urllib,urllib2,cookielib
import smtplib
import ftplib
import datetime,time
import bs4
import re
import csv
import numpy
from PIL import Image
import random
from bs4 import BeautifulSoup as soup
import pandas as pd

site = "https://www.myntra.com/amp/men-kurtas?rows=500&p=1" #make sure rows = 500 and p = 1 ex - https://www.myntra.com/amp/men-tshirts?rows=500&p=1
        #https://www.myntra.com/amp/nehru-jackets?rows=500&p=1,https://www.myntra.com/amp/helmet?rows=500&p=1

hdr1 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
hdr2 = {'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
hdr3 = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
hdr4 = {'User-Agent': 'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
hdr5 = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
hdr = random.choice([hdr1,hdr2,hdr3,hdr4,hdr5])
req = urllib2.Request(site, headers=hdr)


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

response = opener.open(req)
content = response.read()
response.close()


page_soup = soup(content,"html.parser")
xyz  = page_soup.findAll("div",{"class" : "productInfo"})
pqr  = page_soup.findAll("div",{"class" : "product"})

y = len(xyz)
print y

a = 2

filename = "record.csv"
f = open(filename,"w")
headers = "Product_name,Brand,Current_price,Original_price\n"
f.write(headers)

filename2 = "file2.csv"
opening = open(filename2,"w")
headers1 = "Product_link\n"
opening.write(headers1)

while y != 0 :
    for abc in xyz :
        product_name = abc.findAll("h4",{"class" : "name-product"})
        product_name = product_name[0].text.strip()
        product_name = str(product_name.encode('utf-8', 'replace'))
        
        brand = abc.findAll("div",{"class" : "name"})
        brand = brand[0].text
        brand = str(brand.encode('utf-8', 'replace'))

        current_price = abc.findAll("span",{"class" : "price-discounted"})
        current_price = current_price[0].text
        current_price = str(current_price.encode('utf-8', 'replace')) #solves shitty unicode problem DONOT REMOVE
        current_price = current_price[3:] #Removes first three character from converted

        original_price = str(abc.findAll("span",{"class" : "price"}))
        original_price = str([int(s) for s in original_price.split() if s.isdigit()])
        original_price = original_price.translate(None, '[]') #extracts brackets and places none
        #checks for string being non empty else is return if empty or secuence of white space
        if original_price and not original_price.isspace(): 
            pass
        else :
            original_price = current_price

##        percent_off = str(abc.findAll("span",{"class" : "price-discount"}))
##        percent_off = percent_off.translate(None, '[]') #extracts brackets and places none
##        #checks for string being non empty else is return if empty or secuence of white space
##        if percent_off and not percent_off.isspace() :
##            percent_off = str(int(''.join(ele for ele in percent_off if ele.isdigit() or ele == '.')))
##        else :
##            percent_off = "NO DISCOUNT"
        print product_name
        print brand
        print current_price
        print original_price
        data1 = product_name + "," + brand + "," + current_price + "," + original_price + "\n"
        f.write(data1)
##        print percent_off
    for ac in pqr:
      product_link = str(ac.a["href"])
      myntra_homepage = "https://www.myntra.com"
      product_link = myntra_homepage + product_link
                                                            #sir dard tha bc link nikalna
     # product_image = ac.findAll("amp-img")[0].get('src')        #commented out this line cause want to add product image feature later but it works

      data3 = product_link + "\n"
      opening.write(data3)

    if a == 100 :
      site = str(site[0:-2]) + str(a)
    elif a> 100:
      site = str(site[0:-3]) + str(a)
    elif a <= 10 :
      site = str(site[0:-1]) + str(a) #code will crash if the no of product listed at myntra in a specific category exceeds 500000
    elif 10 < a <=99 :
      site = str(site[0:-2]) + str(a)

    a = int(a)
    a = a+1
    #print a
    #print site

    hdr = random.choice([hdr1,hdr2,hdr3,hdr4,hdr5])
    req = urllib2.Request(site, headers=hdr)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    response = opener.open(req)
    content = response.read()
    response.close()
    
    print site
    page_soup = soup(content,"html.parser")
    xyz  = page_soup.findAll("div",{"class" : "productInfo"})
    pqr  = page_soup.findAll("div",{"class" : "product"})
    y = len(xyz)
    print y


try:
    ap = csv.reader(f, delimiter='\t')
finally:
    f.close()                                 #just closing csv file so that it can be joined in next step

try:
    qv = csv.reader(opening, delimiter='\t')
finally:
    opening.close()


df1 = pd.read_csv("record.csv")
df2 = pd.read_csv("file2.csv")

merged = df1.join(df2)
timestr = time.strftime("%Y%m%d-%H%M%S")
merged.to_csv(timestr + ".csv", index=False)

os.remove("record.csv")
os.remove("file2.csv")
#lmnop = random.randint(0,1)
#time.sleep(lmnop)


   
