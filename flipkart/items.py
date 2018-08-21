# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ListingItem(scrapy.Item):
	image = scrapy.Field()
	name = scrapy.Field()
	url = scrapy.Field()
	ratings = scrapy.Field()
	price = scrapy.Field()
	mrp = scrapy.Field()
	offer = scrapy.Field()


class PdpItem(scrapy.Item):
	images = scrapy.Field()
	title = scrapy.Field()
	price = scrapy.Field()
	mrp = scrapy.Field()
	offer = scrapy.Field()
	bank_offers = scrapy.Field()
	services = scrapy.Field()
	available_sizes = scrapy.Field()
	available_sizes_url = scrapy.Field()
	seller_name = scrapy.Field()
	seller_ratings = scrapy.Field()
	description = scrapy.Field()
	no_of_items = scrapy.Field()
	sales_package = scrapy.Field()
	brand = scrapy.Field()
	style_code = scrapy.Field()
	brand_color = scrapy.Field()
	size = scrapy.Field()
	ideal_for = scrapy.Field()
	product_type = scrapy.Field()
	fabric = scrapy.Field()
	primary_color = scrapy.Field()
	pattern = scrapy.Field()
	suitable_for = scrapy.Field()
	secondary_color = scrapy.Field()
	reversible = scrapy.Field()
	group_id = scrapy.Field()
	fit = scrapy.Field()
	pockets = scrapy.Field()
	fabric_details = scrapy.Field()
	stars = scrapy.Field()
	ratings_count = scrapy.Field()
	reviews_count = scrapy.Field()
	no_of_5_stars = scrapy.Field()
	no_of_4_stars = scrapy.Field()
	no_of_3_stars = scrapy.Field()
	no_of_2_stars = scrapy.Field()
	no_of_1_stars = scrapy.Field()