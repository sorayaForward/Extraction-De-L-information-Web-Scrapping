import sys
from webscrapy.webscrapy.spiders import VidalSpider,MedicSpider
from scrapy.crawler import CrawlerProcess
from webscrapy.cration_dic import creat_dict
from webscrapy.intervallPortHandler import display,info1Generator
import os
import scrapy


def main():
    if(len(sys.argv) == 3):# path + intervall + port
        try:
            int(sys.argv[2])    
        except:
            print('Please, Print a valid port of type integer')
        else :  
                if "vidal.json" and "medic.json" in os.listdir('.'):# to avoid appending results each time
                    os.remove('vidal.json')
                    os.remove('medic.json')
                process = CrawlerProcess({
                'FEED_FORMAT': 'json',
                })
                process.crawl(VidalSpider.VidalSpider)#lancer le premier spider qui va retourner les liens ( a - z )
                process.crawl(MedicSpider.MedicSpider)#lancer le 2eme spider qui va retourner les medicaments
                process.start()
                m = creat_dict()# creation du dictionnaire subst.dic
                display(m)# afficher les medicaments + creation de info1
                info1Generator(m)
    else:
        print('Missing arguments please respect the format (py extraire.py intervall port)')       


main()

