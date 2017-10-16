# coding=utf-8
from scrapy import Spider
from yangscrapy.items import DailyMoiveItem


class DailyMovie(Spider):
    name = "dailymovie"
    start_urls = ["http://ent.163.com/special/dailymovie/"]

    def parse(self, response):
        item = DailyMoiveItem()
        movies = response.xpath('//table[@class="bg_white"]')
        # print(movies)
        for movie_list in movies:
            movie2 = movie_list.xpath('.//tr/td[@width="30%"]')
            for movie in movie2:
                item["movie_name"] = movie.xpath('.//td[@class="fB f14px"]/a/text()').extract()
                item["movie_desc"] = movie.xpath('.//td[@class="cDGray indent2"]/text()').extract()
                yield item
