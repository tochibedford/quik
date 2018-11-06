import os
import urllib.request
import re



def facebook_search(search):
	
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

	return(result)


def twitter_search(search):
	terms = search.replace(" ","%20")
	print(terms)
	url = "https://www.twitter.com/search?q="+terms+"&src=typd" 
	print(url)
	result_unproc_2 = urllib.request.urlopen(url).read()
	result_unproc = str(result_unproc_2.decode('utf-8'))

	regex = re.compile('<p .+ js-tweet-text .+>.+</p>')
	regex2 = re.compile('<p>\d</p>')
	result = regex.findall(result_unproc)
	result2 = regex2.findall(result_unproc)

	# for i in range(1,6):
	# 	remo = "<span>"+str(i)+"</span>"
	# 	result.remove(remo)

	return(result)

searchi = input("search for someone:" )
searchi = str.casefold(searchi)


print(twitter_search(searchi))