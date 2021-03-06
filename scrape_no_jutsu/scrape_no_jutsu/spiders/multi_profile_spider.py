from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrape_no_jutsu.items import LinkedInItem

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy import log
import os


class LinkedinSpider(InitSpider):
    name = 'multi'
    allowed_domains = ['linkedin.com']
    login_page = 'https://www.linkedin.com/uas/login'
    start_urls = []

    def init_request(self):
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        pwd = os.path.dirname(os.path.abspath(__file__))
        pwd = pwd[0:-23]
        #log.msg("The pwd variable has the path: " + pwd)
        f = open(pwd+'creds', 'r')
        username = f.readline()
        password = f.readline()
        f.close()
        g = open(pwd+'multi_file', 'r')
        str = g.readline()
        for x in str.split(' '):
            if x[-1]=='\n':
                self.start_urls.append("https://www.linkedin.com/profile/view?id="+x[0:-1])
            else:
                self.start_urls.append("https://www.linkedin.com/profile/view?id="+x)
        #log.msg("The username is:" + username)
        #log.msg("The password is:" + password)
        return FormRequest.from_response(response,
                formdata={'session_key': username, 'session_password': password},
                callback=self.check_login_response)

    def check_login_response(self, response):
        if "Sign Out" in response.body:
            self.log("\n\n\nSuccessfully logged in. Let's start crawling!\n\n\n")
            return self.initialized()
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

        item = LinkedInItem()

        print 'Name : ' + response.xpath('//span[@class="full-name"]/text()').extract()[0]
        item['name'] = response.xpath('//span[@class="full-name"]/text()').extract()[0]

        exp = 0
        item['experiences'] = {}

        for exp_div in exp_divs:

            item['experiences'][exp] = {}

            print ''

            exp_sel = Selector(text=exp_div)

            print "Designation is : " + exp_sel.xpath('//h4/a/text()').extract()[0]
            item['experiences'][exp][0] = exp_sel.xpath('//h4/a/text()').extract()[0]


            org = exp_sel.xpath('//h5/span/strong/a/text()').extract()
            org_alt = exp_sel.xpath('//h5/a/text()').extract()
            if not org and not org_alt:
                print "This designation does not have an associated organization"
                item['experiences'][exp][1] = ''
            elif not org_alt:
                print org[0]
                item['experiences'][exp][1] = org[0]
            else:
                print org_alt[0]
                item['experiences'][exp][1] = org_alt[0]

            dates = exp_sel.xpath('//span/time/text()').extract()

            if not dates:
                print "The dates and duration have not been mentioned for this experience"
                item['experiences'][exp][2] = ''
                item['experiences'][exp][3] = ''
            elif len(dates) == 1:
                print dates[0] + " - present"
                item['experiences'][exp][2] = dates[0]
                item['experiences'][exp][3] = 'present'
            else:
                print dates[0] + " - " + dates[1]
                item['experiences'][exp][2] = dates[0]
                item['experiences'][exp][3] = dates[1]

            location = exp_sel.xpath('//span/span/text()').extract()

            if not location:
                print "The user has not mentioned a location for this particular experience"
                item['experiences'][exp][4] = ''
            else:
                print location[0]
                item['experiences'][exp][4] = location[0]

            description = exp_sel.xpath('//p[contains(@class,"description")]/text()').extract()

            if not description:
                print "The user has not given any description for this particular experience"
                item['experiences'][exp][5] = ''
            else:
                print description[0]
                item['experiences'][exp][5] = description[0]

            print ''

            exp = exp+1



        edu_back = Selector(text=response.xpath('//div[contains(@class,"background-education")]').extract()[0])

        edu_divs = edu_back.xpath('//div[contains(@class,"section-item")]').extract()

        print '--------------------------------------------------------------------------------------------------'
        print ''
        print 'Education information:'
        print ''
        print '--------------------------------------------------------------------------------------------------'

        edu = 0
        item['educations'] = {}

        for edu_div in edu_divs:

            item['educations'][edu] = {}

            print ''

            edu_sel = Selector(text=edu_div)

            print "Institute/College/School is : " + edu_sel.xpath('//h4/a/text()').extract()[0]
            item['educations'][edu][0] = edu_sel.xpath('//h4/a/text()').extract()[0]

            degree = edu_sel.xpath('//header/h5/span[contains(@class,"degree")]/text()').extract()

            if not degree:
                print "The user does not have a degree in this particular education"
                item['educations'][edu][1] = ''
            else:
                print degree[0]
                item['educations'][edu][1] = degree[0]

            major = edu_sel.xpath('//header/h5/span[contains(@class,"major")]/a/text()').extract()

            if not major:
                print "The user does not have a major in this particular education"
                item['educations'][edu][2] = ''
            else:
                print major[0]
                item['educations'][edu][2] = major[0]

            dates = edu_sel.xpath('//span[contains(@class,"education-date")]/time/text()').extract()

            if not dates:
                print "The dates and duration have not been mentioned for this education"
                item['educations'][edu][3] = ''
                item['educations'][edu][4] = ''
            elif len(dates) == 1:
                print dates[0] + " - present"
                item['educations'][edu][3] = dates[0]
                item['educations'][edu][4] = 'present'
            else:
                print dates[0] + "" + dates[1]
                item['educations'][edu][3] = dates[0]
                item['educations'][edu][4] = dates[1]

            act_soc = edu_sel.xpath('//p[contains(@class,"activities")]/a/text()').extract()

            j = 0
            item['educations'][edu][5] = {}
            for a_s in act_soc:
                print "The following activity was done by the candidate during this education: " + a_s
                item['educations'][edu][5][j] = a_s
                j = j + 1


            courses = edu_sel.xpath('//dl[contains(@class,"education-associated")]/dd/ul/li/text()').extract()

            k = 0
            item['educations'][edu][6] = {}
            for course in courses:
                print "This course has been taken during his education here: " + course
                item['educations'][edu][6][k] = course
                k = k + 1

            print ''

            edu = edu+1

        print '--------------------------------------------------------------------------------------------------'

################################### Education Code Ends ########################################
################################################################################################

        return item
