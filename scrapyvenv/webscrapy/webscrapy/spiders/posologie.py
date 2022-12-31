import scrapy
import sys 
#from [module] import [function or value]


# extraction des posologies apartit de concord.html le resultat sera dans posologie.json


class PosologieSpider(scrapy.Spider):
    name = 'posologie'
    allowed_domains = ['127.0.0.1']
    start_urls = ['http://127.0.0.1:8080/concord.html']
    def parse(self, response):
        print(sys.argv)
        pos = []
        columns = response.xpath('//a/text()').getall()
        yield { "posologie" : columns
         }
