from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
from scrapy.contrib.spiders import CrawlSpider, Rule

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector


class LinkedinSpider(CrawlSpider):
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

        # Name of the cadidate
        item['name'] = response.xpath('//span[@class="full-name"]/text()').extract()[0]

        # Retrieving the whole div with the experience data in it
        exp_back = Selector(text=response.xpath('//div[contains(@class,"background-experience")]').extract()[0])

        # Retrieving the list of divs which host individual experiences
        exp_divs = exp_back.xpath('//div[contains(@class,"section-item")]').extract()

        #Looping over each experience div to get the required data
        for exp_div in exp_divs:
            exp_sel = Selector(text=exp_div)
            print exp_sel.xpath('//h4/a/text()').extract()[0]




        '''

        item = LinkedInItem()

        # Name of the candidate
        item['name'] = response.xpath('//span[@class="full-name"]/text()').extract()[0]

        # Storing the experiences array
        exp = response.xpath('//a[@title="Learn more about this title"]/text()').extract()

        # Organizations where the member has worked for experiences (use only first len(exp) for the results)
        org = response.xpath('//a[@dir="auto"]/text()').extract()

        # The timeline array pertaining to all experiences
        exp_times = response.xpath('//span[@class="experience-date-locale"]/time/text()').extract()

        int i = 0

        for x in exp:
            item['experiences'][i][0] = x
            item['experiences'][i][1] = org[i]
            if len(exp_times)%2 == 0:
                item['experiences'][i][2] = exp_times[i*2]
                item['experiences'][i][3] = exp_times[i*2+1]
            else:
                if i == 0:
                    item['experiences'][i][2] = exp_times[0]
                    item['experiences'][i][3] = 'present'
                else:
                    item['experiences'][i][2] = exp_times[i*2-1]
                    item['experiences'][i][3] = exp_times[i*2]
            i = i + 1

        '''

# Location and description were not possible because the coorelation is not achievable in this model

        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)



