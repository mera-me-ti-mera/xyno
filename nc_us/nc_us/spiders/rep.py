import scrapy


class RepSpider(scrapy.Spider):
    name = "rep"
    allowed_domains = ["ncleg.gov"]
    start_urls = ["https://ncleg.gov/Members/Biography/H/819"]

    def parse(self, response):
        pass
