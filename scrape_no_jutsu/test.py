# Module for importing variables

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

    print ""

    # Generating a selector for each experience div
    exp_sel = Selector(text=exp_div)

    # Designation of the experience
    print "Designation is : " + exp_sel.xpath('//h4/a/text()').extract()[0]

    # Organization of the experience, along with the alternate path
    org = exp_sel.xpath('//h5/span/strong/a/text()').extract()
    org_alt = exp_sel.xpath('//h5/a/text()').extract()
    if not org and not org_alt:
        print "This designation does not have an associated organization"
    elif not org_alt:
        print org[0]
    else:
        print org_alt[0]

    # from date and to date of this experience
    dates = exp_sel.xpath('//span/time/text()').extract()

    if not dates:
        print "The dates and duration have not been mentioned for this experience"
    elif len(dates) == 1:
        print dates[0] + " - present"
    else:
        print dates[0] + " - " + dates[1]

    # Location of the experience
    location = exp_sel.xpath('//span/span/text()').extract()

    if not location:
        print "The user has not mentioned a location for this particular experience"
    else:
        print location[0]

    # Description of the experience
    description = exp_sel.xpath('//p[contains(@class,"description")]/text()').extract()

    if not description:
        print "The user has not given any description for this particular experience"
    else:
        print description[0]

    print ""
    print ""
















