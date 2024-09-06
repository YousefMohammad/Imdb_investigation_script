# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 16:42:15 2023

@author: LENOVO
"""

import scrapy

from scrapy.item import Item, Field

from scrapy.loader import ItemLoader

generes = {
    "Action": 1766,
    "Advanture" : 1269,
    "Animation": 334,
    "Biography": 441,
    "Comedy": 2227,
    "Crime": 1308,
    "Documentary": 82,
    "Darama": 3392,
    "Family":609,
    "Fantasy": 853,
    "Film-Noir":32,
    "History": 267,
    "Horror": 838,
    "Music": 202,
    "Musical": 184,
    "Mystery": 895,
    "Romance": 1280,
    "Sci-Fi": 875,
    "Short": 17,
    "Sport": 201,
    "Thriller": 2143,
    "War": 282,
    "Western": 114
}

class Movie(Item):
    name = Field()
    year = Field()
    certificate = Field()
    runtime = Field()
    genre = Field()
    rate = Field()
    metascore = Field()
    director = Field()
    stars = Field()
    votes = Field()
    gross = Field()

class IMDb_Movies(scrapy.Spider):
    name = "imdb_movies"
    def start_requests(self):
        start_urls = []
        for i in generes.keys():
            for j in range(1,generes[i],50):
                start_urls.append("https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres={}&sort=user_rating,desc&start={:0>2}&ref_=adv_nxt".format(i.lower(),j))
    
        for url in start_urls:
            yield scrapy.Request(url = url, callback=self.parse)
        
    def parse(self,response):
        loader = ItemLoader(item=Movie(),response=response)
        loader.add_xpath("name","//div[@class='lister-list']/div[@class='lister-item mode-advanced']/div[@class='lister-item-content']/h3[@class='lister-item-header']/a")
