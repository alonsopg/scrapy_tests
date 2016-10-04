from scrapy.selector import HtmlXPathSelector
from scrapy import Selector
import csv
import pandas as pd
from scrapy.spiders import Spider
# run with : scrapy crawl craig

class MySpider(Spider):
    name = "craig"
    #con craiglist
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://mexicocity.craigslist.com.mx/search/rea"]


    def parse(self, response):
        hxs = Selector(response)
        titles = hxs.xpath("//span[@class='pl']")
        print ('\n*********Content********\n')
        results = []
        for titles in titles:
            title = titles.xpath("a/text()").extract()
            link = titles.xpath("a/@href").extract()
            results.append([title, link])

            #print('\naquí\n',len(results))

        #with pandas, dump it into a .csv style

        df = pd.DataFrame(results, columns=['A','B'])
        for col in df.columns:
            df[col] = df[col].apply(lambda i: ''.join(i))

        df.to_csv('/Users/user/Desktop/new_dump.csv',index = False)


        # #Dump it into a csv with csv module
        # csv_file = open("/Users/user/Desktop/casas_dump4.csv",'w')
        # wr = csv.writer(csv_file)
        # for row in results:
        #     wr.writerow(row)
        #