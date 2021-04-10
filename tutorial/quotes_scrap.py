from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup
import datetime
import json
import csv
import urllib
from urllib import parse

my_url = 'https://allevents.in/new%20delhi/all?page='
page_count = 0

while True:
	page_count += 1
	url_to_hit = my_url + str(page_count)
	uClient = uReq(url_to_hit)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	page_soup.find_all('div',attrs={'class':'meta-right'}) 

	event_li_list = page_soup.find_all('li', attrs={"class": "item event-item box-link"})

	date_dict_in_obj = {}
	date_dict = {}
	
	if not event_li_list:
		break

	for event_li in event_li_list:  # to display event name
		anchortag = event_li.find('a')
		anchortag_text = anchortag.text.strip()
		print("\nEvent Name : " + anchortag_text)

		place_span_tag = event_li.find('span',attrs={'class':'up-venue toh'})
		place = place_span_tag.text.strip()
		print ("\nVenue : " + place)

		start_date_span_tag = event_li.find('span',attrs={'class':'up-time-display'})
		if start_date_span_tag:
			date_text = start_date_span_tag.text.strip()
			date_time_obj = datetime.datetime.strptime(date_text, '%a %b %d %Y at %I:%M %p')
			date_dict_in_obj["start_date"] = date_time_obj
			date_dict["start date"] = date_text
			print ("\nDate : " + str(date_dict_in_obj))


		event_url = event_li['data-share-link']
		uClient = uReq(event_url)
		event_page_html = uClient.read()
		uClient.close()
		event_page_soup = soup(event_page_html, "html.parser")

		event_description_tag = event_page_soup.find('div', attrs={"id": "event_description"})
		event_description = ""
		if event_description_tag:
			event_description = event_description_tag.text.strip()
			print("\nEvent Description : \n "+ event_description)

		event_host_div = event_page_soup.find(id="event_host")
		event_host_dict = {}
		if event_host_div:
			event_host_a_tag = event_host_div.find('a')
			event_host_name = event_host_a_tag['title']
			event_host_dict["name"] = event_host_name
			event_host_url = event_host_a_tag['href']
			event_host_dict["url"] = event_host_url
			event_host_img = event_host_a_tag.find('img')
			if event_host_img:
				event_host_img_url = event_host_img['src']
				event_host_dict["img"] = event_host_img_url
		print("\nHost details :" + str(event_host_dict))
		
		print("--------------------------------------------\n--------------------------------------------")
		
		data_json = {"Event name": anchortag_text, "Event Place": place, "Event Date": date_dict, "Event DEscription": event_description, "Host details": event_host_dict}

		
		file = open('eventdetails.json','a')
		file.write(json.dumps(data_json)+'\n')
		file.close()
		
	print("Page No." + str(page_count))

	"""
url = "https://allevents.in/api/index.php/categorization/web/v1/list"


post_params = {
	'category': '"all"',
	'city': '"new delhi"',
	'edate': '1649548800',
	'formats': '0',
	'keywords': '0',
	'page': '5',
	'rows': '15',
	'sdate': '1618012800',
	'tag_type': 'null',
	'venue': '0'
}
post_params = parse.urlencode(post_params).encode()

headers = {
			"authority": "allevents.in",
			"accept": "application/json, text/plain, */*",
			"accept-encoding": "gzip, deflate, br",
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4"
		}
req = Request(url)
req.add_header("authority", "allevents.in")
req.add_header("accept", "application/json, text/plain, */*")
req.add_header("accept-encoding", "gzip, deflate, br")
req.add_header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4")
uClient = uReq(req, post_params)
(page_html, ) = uClient
uClient.close()
page_soup = soup(page_html, "html.parser")
print(page_html)
page_soup.find_all('div',attrs={'class':'meta-right'}) 

"""