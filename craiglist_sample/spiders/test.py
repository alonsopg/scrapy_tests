from scrapy.selector import HtmlXPathSelector
import pandas as pd
from scrapy.spider import BaseSpider

# run with : scrapy crawl craig

class MySpider(BaseSpider):
    name = "craig"
    #con craiglist
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://mexicocity.craigslist.com.mx/search/rea"]


    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//span[@class='pl']")
        for titles in titles:
            title = titles.select("a/text()").extract()
            link = titles.select("a/@href").extract()
            print(title, link)
