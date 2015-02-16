import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapeTorr.items import ScrapetorrItem

class Scrapetorr(CrawlSpider):
    name = "scrapetorr"
    allowed_domains = ["thepiratebay.se"]
    start_urls = ["https://thepiratebay.se/top"]

    rules = (
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('thepiratebay\.se\/top', )), callback='parse_item', follow= True),
    )
    
    
    def parse_item(self, response):
        for sel in response.xpath('//tr/td[2]'):
            item = ScrapetorrItem()
	    item['link'] = sel.xpath('a[1]/@href').extract()
            yield item
