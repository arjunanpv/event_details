from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://allevents.in/new%20delhi/all'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
page_soup.find_all('div',attrs={'class':'meta-right'}) 

event_li_list = page_soup.find_all('li', attrs={"class": "item event-item box-link"})

for event_li in event_li_list:  # to display event name
	anchortag = event_li.find('a')
	anchortag_text = anchortag.text.strip()
	print("Event Name : " + anchortag_text)

	place_span_tag = event_li.find('span',attrs={'class':'up-venue toh'})
	place = place_span_tag.text.strip()
	print ("Venue : " + place)

	start_date_span_tag = event_li.find('span',attrs={'class':'up-time-display'})
	date_text = start_date_span_tag.text.strip()
	print ("Date : " + date_text)

	print("--------------------------------------------")

# print(event_li_list)