import json
import scrapy
from flipkart.items import ListingItem
from scrapy.utils.response import open_in_browser


class ListingSpider(scrapy.Spider):
	name = 'listings'

	# start_urls = ['https://www.flipkart.com/kids-clothing/boys-wear/shorts-34ths/pr?sid=2oq,mpf,u6l,xt9&otracker=categorytree',]
	def start_requests(self):
		with open('categories.json', 'rb') as cat_file:
			data = json.load(cat_file)
			for items in data:
				if not items['url'] is None:
					yield scrapy.Request('https://www.flipkart.com{}'.format(items['url']), callback=self.parse)

	def parse(self, response):
		# open_in_browser(response)
		list_item = ListingItem()
		# visited = []
		container = response.xpath("//div[contains(@class, '_1HmYoV _35HD7C')]")
		list_item['image'] = container.xpath(".//div[@class='_3O0U0u']//div[@class='_3BTv9X']/img/@src").extract_first()
		list_item['name'] = container.xpath(".//div[@class='_3O0U0u']//a[@class='_2cLu-l']/text()").extract_first()
		list_item['url'] = container.xpath(".//div[@class='_3O0U0u']//a[@class='_2cLu-l']/@href").extract_first()
		list_item['ratings'] = container.xpath(".//div[@class='_3O0U0u']//div[contains(@class, 'hGSR34 _2beYZw')]/text()").extract_first()
		extra_data = container.xpath(".//div[@class='_3O0U0u']//div[@class='_1uv9Cb']")
		list_item['price'] = extra_data.xpath(".//div[@class='_1vC4OE']/text()").extract_first()
		list_item['mrp'] = extra_data.xpath(".//div[@class='_3auQ3N']/text()").extract_first()
		list_item['offer'] = extra_data.xpath(".//div[@class='VGWI6T']/span/text()").extract_first()

		next_page = container.xpath(".//a[@class='_3fVaIS']/@href")
		# yield  pagination on hold

		yield list_item