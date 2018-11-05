import os
import urllib.request
import re



search = str.casefold("harram David")
terms = search.replace(" ","-")
print(terms)
url = "https://www.facebook.com/public/"+terms 
print(url)
result_unproc = str(urllib.request.urlopen(url).read())

regex = re.compile('<span>[\w+\s]+</span>')
regex2 = re.compile('<span>\d</span>')
result = regex.findall(result_unproc)
result2 = regex2.findall(result_unproc)

for i in range(1,6):
	remo = "<span>"+str(i)+"</span>"
	result.remove(remo)

print(result)
