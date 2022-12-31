import scrapy
import sys 
#from [module] import [function or value]
from ...links import links
from ..items import WebscrapyItemM  


# 2nd Step : extraction des medicaments le resultat sera dans medic.json
class MedicSpider(scrapy.Spider):
        name = 'medic'
        allowed_domains = ['127.0.0.1']
        custom_settings = {      
            'FEED_FORMAT': 'json',
            'FEED_URI': 'medic.json'
        }
        start_urls = links() #array of links
        def parse(self, response):
            items = WebscrapyItemM()   
            columns = response.xpath('//ul[@class="substances list_index has_children"]/li/a/text()').getall()
            items["medicament"] = columns
            yield items   
            print(items) 
