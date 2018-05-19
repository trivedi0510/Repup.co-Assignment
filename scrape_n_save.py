import requests
import os
from bs4 import BeautifulSoup
import pandas as pd

end_points = {'Delhi':'/delhi-city/', 
			'Hyderabad': '/hyderabad-city/',
			'Chennai':'/chennai-city/',
			'Mumbai':'/mumbai-city/'}

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

url = 'https://blogs.timesofindia.indiatimes.com/city'

for key, value in end_points.items():
	# print(key, value)
	city_url = url + value
	source_code = requests.get(city_url, headers=headers, timeout=15)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,"html.parser")
	h2s = soup.findAll('h2', {'class':'media-heading'})
	city = [key]*len(h2s)
	h2s = [h2.text for h2 in h2s]
	mapped = zip(city, h2s)

	df = pd.DataFrame(list(mapped))

	print(df.head(2))

	with open('data.csv', 'a') as f:
		df.to_csv(f, header=False, index=False)

	#data = {'City':key, 'News':h2s}
	#print(key, h2s[0].text)