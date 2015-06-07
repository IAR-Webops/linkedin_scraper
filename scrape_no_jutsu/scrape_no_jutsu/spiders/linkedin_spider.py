from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
from scrapy.contrib.spiders import CrawlSpider, Rule

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy import log
import os


class LinkedinSpider(CrawlSpider):
    name = 'linkedin'
    allowed_domains = ['linkedin.com']
    login_page = 'https://www.linkedin.com/uas/login'
    start_urls = ["https://www.linkedin.com/edu/alumni?id=9798246"]

    def start_requests(self):
        yield Request(
                url=self.login_page,
                callback=self.login,
                dont_filter=True
                )

    def login(self, response):
        pwd = os.path.dirname(os.path.abspath(__file__))
        pwd = pwd[0:-23]
        log.msg("The pwd variable has the path: " + pwd)
        f = open(pwd+'creds', 'r')
        username = f.readline()
        password = f.readline()
        #log.msg("The username is:" + username)
        #log.msg("The password is:" + password)
        return FormRequest.from_response(response,
                formdata={'session_key': username, 'session_password': password},
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
        #item['name'] = response.xpath('//span[@class="full-name"]/text()').extract()[0]

        exp_back = Selector(text=response.xpath('//div[contains(@class,"background-experience")]').extract()[0])

        exp_divs = exp_back.xpath('//div[contains(@class,"section-item")]').extract()

        print '-----------------------------------------------------------------------------------------'
        print ''
        print 'Experiences information:'
        print ''
        print '--------------------------------------------------------------------------------------------------'

        for exp_div in exp_divs:

            print ''

            exp_sel = Selector(text=exp_div)

            print "Designation is : " + exp_sel.xpath('//h4/a/text()').extract()[0]

            org = exp_sel.xpath('//h5/span/strong/a/text()').extract()
            org_alt = exp_sel.xpath('//h5/a/text()').extract()
            if not org and not org_alt:
                print "This designation does not have an associated organization"
            elif not org_alt:
                print org[0]
            else:
                print org_alt[0]

            dates = exp_sel.xpath('//span/time/text()').extract()

            if not dates:
                print "The dates and duration have not been mentioned for this experience"
            elif len(dates) == 1:
                print dates[0] + " - present"
            else:
                print dates[0] + " - " + dates[1]

            location = exp_sel.xpath('//span/span/text()').extract()

            if not location:
                print "The user has not mentioned a location for this particular experience"
            else:
                print location[0]

            description = exp_sel.xpath('//p[contains(@class,"description")]/text()').extract()

            if not description:
                print "The user has not given any description for this particular experience"
            else:
                print description[0]

            print ''



        edu_back = Selector(text=response.xpath('//div[contains(@class,"background-education")]').extract()[0])

        edu_divs = edu_back.xpath('//div[contains(@class,"section-item")]').extract()

        print '--------------------------------------------------------------------------------------------------'
        print ''
        print 'Education information:'
        print ''
        print '--------------------------------------------------------------------------------------------------'

        for edu_div in edu_divs:

            print ''

            edu_sel = Selector(text=edu_div)

            print "Institute/College/School is : " + edu_sel.xpath('//h4/a/text()').extract()[0]

            degree = edu_sel.xpath('//header/h5/span[contains(@class,"degree")]/text()').extract()

            if not degree:
                print "The user does not have a degree in this particular education"
            else:
                print degree[0]

            major = edu_sel.xpath('//header/h5/span[contains(@class,"major")]/a/text()').extract()

            if not major:
                print "The user does not have a major in this particular education"
            else:
                print major[0]

            dates = edu_sel.xpath('//span[contains(@class,"education-date")]/time/text()').extract()

            if not dates:
                print "The dates and duration have not been mentioned for this education"
            elif len(dates) == 1:
                print dates[0] + " - present"
            else:
                print dates[0] + "" + dates[1]

            act_soc = edu_sel.xpath('//p[contains(@class,"activities")]/a/text()').extract()

            for a_s in act_soc:
                print "The following activity was done by the candidate during this education: " + a_s


            courses = edu_sel.xpath('//dl[contains(@class,"education-associated")]/dd/ul/li/text()').extract()

            for course in courses:
                print "This course has been taken during his education here: " + course

            print ''
        print '--------------------------------------------------------------------------------------------------'

################################### Education Code Ends ########################################
################################################################################################



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


# Location and description were not possible because the coorelation is not achievable in this model

        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

        '''


