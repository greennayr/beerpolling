from BeautifulSoup import BeautifulSoup
import urllib2
from datetime import datetime
import requests


beer_list=[
'crayon box',
'coconut milk ',
'grove stand',
'green rest',
'hammer pants',
'king citra',
'orchard street',
'galaxy juice',
'broken clouds',
'super saint thomas'
]
tempfile=open('/Users/Documents/temp_beer_time.txt','r+') 

previous_date=tempfile.read()
tempfile.close()
previousTime = datetime.strptime(previous_date, "%Y-%m-%d %H:%M:%S.%f") 
url=urllib2.urlopen("https://www.beermenus.com/places/")
soup=BeautifulSoup(url)

for div in soup.findAll('span'):
    if "Updated:" in str(div.contents):
    	# print str(div.contents[0]).split(': ')[1]
    	datetime_object = datetime.strptime(str(div.contents[0]).split(': ')[1], '%m/%d/%Y')
# print datetime_object
tempfile=open('/Users/Documents/temp_beer_time.txt','r+') 
tempfile.write(str(datetime_object))
tempfile.close()
matching_beers=[]
if datetime_object>previousTime:
	current_beer=[]
	for div in soup.findAll('div', attrs={'class':'pure-u-2-3'}):
	    current_beer.append(div.find('a').contents[0])


	for beer in beer_list:
		for curr_beer in current_beer:
			if curr_beer.upper() == beer.upper():
				matching_beers.append(curr_beer)

if len(matching_beers)>0:


	base_url="https://maker.ifttt.com/trigger/BeerUpdate/with/key/"

	payload = {'value1': matching_beers}
	response = requests.post(base_url, data=payload)
	print(response.text) #TEXT/HTML
	print(response.status_code, response.reason) #HTTP





# print out1