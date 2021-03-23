from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
	my_url = 'https://allevents.in/new%20delhi/all'
		uClient = uReq(my_url)
			page_html = uClient.read()
			uClient.close()
	page_soup = soup(page_html, "html.parser")
	page_soup.find_all('div',attrs={'class':'meta-right'}) 
		divlist = page_soup.find_all('div',attrs={'class':'meta-right'})
		divlist[0].find('a')
		anchortag = divlist[0].find('a')
		anchortag.text
		anchortag.text.strip()
for div in divlist:  
	anchortag = div.find('a')
	anchortag_text = anchortag.text.strip()
	print(anchortag_text)
for div in divlist:  
    place_span_tag = div.find('span',attrs={'class':'up-venue toh'})
    place = place_span_tag.text.strip()
    print (place)
for div in divlist:  
	start_date_span_tag = div.find('span',attrs={'class':'up-time-display'})
    date_text = start_date_span_tag.text
    print (date_text)
