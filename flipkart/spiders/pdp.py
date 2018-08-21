import scrapy
from flipkart.items import PdpItem


class PdpSpider(scrapy.Spider):
	name = 'pdp'

	start_urls = ['https://www.flipkart.com/ad-av-short-boys-solid-cotton-linen-blend-nylon-blend/p/itmf3w2s2m2zwzwu?pid=SRTEEFTKSVGTUFQH',]
	# def start_requests(self):
	# 	pass

	def parse(self, response):
		pdp_item = PdpItem()
		container = response.xpath("//div[@class='_2Cl4hZ']")
		images_container = response.xpath("//div[@class='keS6DZ']")
		header = container.xpath(".//div[@class='_29OxBi']")
		pdp_item['images'] = images_container.xpath(".//ul[@class='LzhdeS']//li//div[@class='_2_AcLJ']/@style").extract()
		pdp_item['title'] = header.xpath(".//h1[@class='_9E25nV']/span/text()").extract_first()
		# ratings = header.xpath(".//div[contains(@class, 'hGSR34 _2beYZw')]").extract_first()
		# reviews = header.xpath(".//span[@class='_38sUEc']/span/span/text()").extract()
		pdp_item['price'] = header.xpath(".//div[@class='_3iZgFn']//div[contains(@class, '_1vC4OE _3qQ9m1')]/text()").extract_first()
		pdp_item['mrp'] = header.xpath(".//div[@class='_3iZgFn']//div[contains(@class, '_3auQ3N _1POkHg')]/text()").extract()
		pdp_item['offer'] = header.xpath(".//div[@class='_3iZgFn']//div[contains(@class, 'VGWI6T _1iCvwn')]/span/text()").extract_first()
		pdp_item['available_sizes'] = container.xpath(".//div[@class='rPoo01']//ul[@class='eaKBCI']/li[contains(@id, 'swatch-')]/a/text()").extract()
		pdp_item['available_sizes_url'] = container.xpath(".//div[@class='rPoo01']//ul[@class='eaKBCI']/li[contains(@id, 'swatch-')]/a/@href").extract()
		pdp_item['seller_name'] = container.xpath(".//div[@id='sellerName']/span/span/text()").extract_first()
		pdp_item['seller_ratings'] = container.xpath(".//div[@id='sellerName']/span/div[contains(@class, 'hGSR34 _2beYZw YddkNl')]/text()").extract_first()
		pdp_item['description'] = container.xpath(".//div[@class='_1PPw05']//div[contains(@class, 'bzeytq _3cTEY2')]/text()").extract_first()
		specifications = container.xpath(".//div[@class='MocXoX']")
		pdp_item['no_of_items'] = specifications.xpath(".//div[@class='_2RngUh'][1]//li[1]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['sales_package'] = specifications.xpath(".//div[@class='_2RngUh'][1]//li[2]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['brand'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[1]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['style_code'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[2]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['brand_color'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[3]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['size'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[4]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['ideal_for'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[5]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['product_type'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[6]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['fabric'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[7]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['primary_color'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[8]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['pattern'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[9]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['suitable_for'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[10]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['secondary_color'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[11]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['reversible'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[12]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['group_id'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[13]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['fit'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[14]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['pockets'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[15]//li[@class='_3YhLQA']/text()").extract_first()
		pdp_item['fabric_details'] = specifications.xpath(".//div[@class='_2RngUh'][2]//li[16]//li[@class='_3YhLQA']/text()").extract_first()
		ratings_reviews = container.xpath(".//div[contains(@class, 'ebepc- _2eB0mV')]")
		pdp_item['stars'] = ratings_reviews.xpath(".//div[@class='_1i0wk8']/text()").extract_first()
		pdp_item['ratings_count'] = ratings_reviews.xpath(".//div[contains(@class, '_2yc1Qo')][2]//span/text()").extract_first()
		pdp_item['reviews_count'] = ratings_reviews.xpath(".//div[contains(@class, '_2yc1Qo')][3]//span/text()").extract_first()
		pdp_item['no_of_5_stars'] = ratings_reviews.xpath(".//li[contains(@class, '_58ZIbs _1V6lUx')][1]//div[@class='CamDho']/text()").extract_first()
		pdp_item['no_of_4_stars'] = ratings_reviews.xpath(".//li[contains(@class, '_58ZIbs _1V6lUx')][2]//div[@class='CamDho']/text()").extract_first()
		pdp_item['no_of_3_stars'] = ratings_reviews.xpath(".//li[contains(@class, '_58ZIbs _1V6lUx')][3]//div[@class='CamDho']/text()").extract_first()
		pdp_item['no_of_2_stars'] = ratings_reviews.xpath(".//li[contains(@class, '_58ZIbs _1V6lUx')][4]//div[@class='CamDho']/text()").extract_first()
		pdp_item['no_of_1_stars'] = ratings_reviews.xpath(".//li[contains(@class, '_58ZIbs _1V6lUx')][5]//div[@class='CamDho']/text()").extract_first()

		yield pdp_item