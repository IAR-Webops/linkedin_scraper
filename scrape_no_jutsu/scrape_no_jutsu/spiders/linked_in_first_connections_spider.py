from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
import os
import json


class LinkedPySpider(InitSpider):
    name = 'l1con'
    allowed_domains = ['linkedin.com']
    login_page = 'https://www.linkedin.com/uas/login'
    start_urls = ["https://www.linkedin.com/contacts/api/contacts/more/?start=0&count=60&fields=id"]

    def init_request(self):
        #"""This function is called before crawling starts."""
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        pwd = os.path.dirname(os.path.abspath(__file__))
        pwd = pwd[0:-23]
        #log.msg("The pwd variable has the path: " + pwd)
        f = open(pwd+'creds', 'r')
        username = f.readline()
        password = f.readline()
        return FormRequest.from_response(response,
                    formdata={'session_key': username, 'session_password': password},
                    callback=self.check_login_response)

    def check_login_response(self, response):
        #"""Check the response returned by a login request to see if we aresuccessfully logged in."""
        if "Sign Out" in response.body:
            self.log("\n\n\nSuccessfully logged in. Let's start crawling!\n\n\n")
            # Now the crawling can begin..

            return self.initialized()

        else:
            self.log("\n\n\nFailed, Bad times :(\n\n\n")
            # Something went wrong, we couldn't log in, so nothing happens.s

    def parse(self, response):
        #self.log("\n\n\n We got data! \n\n\n")

        # Name of the cadidate
        #item['name'] = response.xpath('//span[@class="full-name"]/text()').extract()[0]
        #self.log("\n\n\n Now scraping data of first connections of Mr.Dharani\n\n\n")

        # Initially, fetch the total number of connections


        # Select the container which has all the contacts information
        #cont_back = response.xpath('//section[@id="contact-list-container"]').extract()

        # Generating a selector for the container to look into what is present in it
        #cont_sel = Selector(text=cont_back)

        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

        file_name = open(filename)
        json_file = json.load(file_name)

        f_name = "multi_contacts"
        with open(f_name, 'wb') as f:
            for x in json_file['contacts']:
                f.write(x['id'])
                f.write('\n')

        #os.remove(filename)
