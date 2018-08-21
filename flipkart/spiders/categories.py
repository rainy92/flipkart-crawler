import scrapy
import json


class CategoriesSpider(scrapy.Spider):
    name = 'categories'
    allowed_domains = ['www.flipkart.com']
    start_urls = ['https://www.flipkart.com/lc/getData?dataSourceId=websiteNavigationMenuDS_1.0&t=25577905']

    def parse(self, response):
        categories = json.loads(response.body)
        for key in categories['navData']:
        	if 'tabs' in categories['navData'].get(key).keys():
        		for elems in categories['navData'].get(key).get('tabs')[0]['columns']:
        			for i in range(len(elems)):
        				title = elems[i]['title'].encode('utf-8')
        				url = elems[i]['url'].encode('utf-8')

				        yield{
				        	'title': title,
				        	'url': url,
				        }