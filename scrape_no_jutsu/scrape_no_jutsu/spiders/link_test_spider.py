from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector


class LinkedPySpider(InitSpider):
    name = 'linktest'
    allowed_domains = ['linkedin.com']
    login_page = 'https://www.linkedin.com/uas/login'
    start_urls = ["https://www.linkedin.com/profile/view?id=95618844","https://www.linkedin.com/profile/view?id=9798246"]

    def init_request(self):
        #"""This function is called before crawling starts."""
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        #"""Generate a login request."""
        return FormRequest.from_response(response,
                    formdata={'session_key': 'dharani.manne@gmail.com', 'session_password': 'amulyaabhi'},
                    callback=self.check_login_response)

    def check_login_response(self, response):
        #"""Check the response returned by a login request to see if we aresuccessfully logged in."""
        if "Sign Out" in response.body:
            self.log("\n\n\nSuccessfully logged in. Let's start crawling!\n\n\n")
            # Now the crawling can begin..

            return self.initialized() # ****THIS LINE FIXED THE LAST PROBLEM*****

        else:
            self.log("\n\n\nFailed, Bad times :(\n\n\n")
            # Something went wrong, we couldn't log in, so nothing happens.s

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



