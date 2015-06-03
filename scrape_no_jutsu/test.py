from scrapy.selector import Selector
from scrapy.http import HtmlResponse

with open ("profile", "r") as myfile:
    data = myfile.read()
    myfile.close()

response = Selector(text=data)

# Retrieving the whole div with the experience data in it
exp_back = Selector(text=response.xpath('//div[contains(@class,"background-experience")]').extract()[0])

# Retrieving the list of divs which host individual experiences
exp_divs = exp_back.xpath('//div[contains(@class,"section-item")]').extract()


#Looping over each experience div to get the required data
for exp_div in exp_divs:
    exp_sel = Selector(text=exp_div)
    print "Title is : " + exp_sel.xpath('//h4/a/text()').extract()[0]
