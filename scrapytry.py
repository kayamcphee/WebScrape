import scrapy

class StaplesSpider(scrapy.Spider):
    name = 'staples'
    allowed_domains = {'www.staples.com/'}
    start_urls = {'https://www.staples.com/mounts/directory_mounts?'}

    def parse(self, response):
        title = response.xpath('//div/div/div/div/div/div/div/div/div/div/div/div/a/text()').getall()
        price = response.xpath('//div/div/div/div/div/div/div/div/div/div/div/div/div/div/span/test()').getall()

        yield{
            'titles':title,
            'prices':price,
        }

StaplesSpider(scrapy.Spider)
