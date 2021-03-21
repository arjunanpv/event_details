import scrapy


class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	
	def start_requests(self):
		urls = [
            'http://allevents.in/new_delhi/all',
		]
		headers = {
			"authority": "allevents.in",
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"accept-encoding": "gzip, deflate, br",
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54"
		}
		for url in urls:
			yield scrapy.Request(url=url, headers=headers, callback=self.parse)
			
	def parse(self, response):
		for quote in response.css('li.item'):
			yield {
				'event_name': quote.xpath('div.title::text').get()
            }
			
         

		