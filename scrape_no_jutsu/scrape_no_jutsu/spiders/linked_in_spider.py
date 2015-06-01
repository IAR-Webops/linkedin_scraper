from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
from scrapy.contrib.spiders import CrawlSpider, Rule

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector


class LinkedInSpider(CrawlSpider):
    name = 'linkedin'
    allowed_domains = ['linkedin.com']
    login_page = 'https://www.linkedin.com/uas/login'

    start_urls = ["https://www.linkedin.com/edu/alumni?id=13501"]


    def start_requests(self):
        yield Request(
                url=self.login_page,
                callback=self.login,
                dont_filter=True
                )

    def login(self, response):
        return FormRequest.from_response(response,
                formdata={'session_key': 'dharani.manne@gmail.com', 'session_password': 'amulyaabhi'},
                callback=self.check_login_response)

    def check_login_response(self, response):
        if "Sign Out" in response.body:
            self.log("\n\n\nSuccessfully logged in. Let's start crawling!\n\n\n")
            self.log('Hi, this is an item page! %s' % response.url)
            return Request(url='https://www.linkedin.com/profile/view?id=9798246')

        else:
            self.log("\n\n\nFailed, Bad times :(\n\n\n")


    def parse(self, response):
        self.log("\n\n\n We got data! \n\n\n")

        item = LinkedInItem()

        item['name'] = response.xpath('//span[@class="full-name"]/text()').extract()[0]
        exp = response.xpath('//a[@title="Learn more about this title"]/text()').extract()

        locations = response.xpath('//a[@dir="auto"]/text()').extract()

        int i = 0

        for x in exp:
            item['experiences'][i] = x
            i = i + 1


#        filename = response.url.split("/")[-2]
#        with open(filename, 'wb') as f:
#            f.write(response.body)

