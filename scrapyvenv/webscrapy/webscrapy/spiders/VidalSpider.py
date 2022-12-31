import scrapy
import sys
from ..items import WebscrapyItemV  

# 1st Step : extraction des liens 
# scrap http://127.0.0.1:port/vidal to get list of links in order to scrap with another spider 

class VidalSpider(scrapy.Spider):
        name = 'vidal'
        start_urls = ['http://127.0.0.1:'+sys.argv[2]+'/vidal']
        custom_settings = {      
            'FEED_FORMAT': 'json',
            'FEED_URI': 'vidal.json'
        }
    # quand le spider est cree la fonction sera executee
        def parse(self, response):
                items = WebscrapyItemV()   
                columns = response.css('a').xpath('@href')
                for col in range(5,len(columns)):
                                # extraire et faire la concatenation avec http://127.0.0.1:port/vidal/
                            items["title"] = 'http://127.0.0.1:'+sys.argv[2]+'/vidal/'+columns[col].get()
                            yield items
                            # yield va envoyer chaque item reconnu vers pipelines.py pour autre traitement(dans ce cas le traitement de stockage dans vidal.json)

            
