import scrapy
import hashlib


class RepsSpider(scrapy.Spider):
    name = "reps"
    allowed_domains = ["ncleg.gov"]
    start_urls = [
            "https://ncleg.gov/Members/MemberList/H",
            "https://ncleg.gov/Members/MemberList/S",
            ]

    def parse(self, response):
        date = response.headers['date'].decode('utf-8')
        url = response.url
        title = response.css('title::text').get()
        hashed = hashlib.sha512(response.css('main').get().encode('utf-8')).hexdigest()
        yield dict(flavor='page', date=date, url=url, title=title, hashed=hashed)
        # pass
