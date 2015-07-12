import urllib2

url = 'http://www.acme.com/products/3322'
response = urllib2.urlopen(url).read()
