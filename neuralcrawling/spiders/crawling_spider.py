from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow=r"catalogue/category"), follow=True),
        Rule(LinkExtractor(allow=r"catalogue", deny=r"category"), callback='parse_item', follow=True),
    )

    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json',
    }

    def parse_item(self, response):
        yield {
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            "availability": response.css(".availability::text").re_first(r'\w+'),
        }




#from scrapy.spiders import CrawlSpider, Rule
#from scrapy.linkextractors import LinkExtractor

#class CrawlingSpider(CrawlSpider):
    #name = "mycrawler"
   # allowed_domains = ["toscrape.com"]
    #start_urls = ["http://books.toscrape.com/"]
    #rules = (
       # Rule(LinkExtractor(allow="catalogue/category")),
        #Rule(LinkExtractor(allow="catalogue", deny="category"), callback='parse_item'),
    #)
#custom_settings = {
   # 'CLOSESPIDER_PAGECOUNT': 10 # stop after 10 pages
#}


#def parse_item(self, response):
   # yield {
       # "title": response.css(".product_main h1::text").get(),
        #"price": response.css(".price_color::text").get(),
      #  "availability": response.css(".availability::text")[1].get().replace("\n", "").replace(" ", ""),
    #}