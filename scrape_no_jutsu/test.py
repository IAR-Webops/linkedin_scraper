# Module for importing variables

from scrapy.selector import Selector
from scrapy.http import HtmlResponse

with open ("profile", "r") as myfile:
    data = myfile.read()
    myfile.close()

response = Selector(text=data)

################################################################################################
################################## Experiences Code ############################################


# Retrieving the whole div with the experience data in it
exp_back = Selector(text=response.xpath('//div[contains(@class,"background-experience")]').extract()[0])

# Retrieving the list of divs which host individual experiences
exp_divs = exp_back.xpath('//div[contains(@class,"section-item")]').extract()


#Looping over each experience div to get the required data
for exp_div in exp_divs:

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


################################# Experiences Code Ends ########################################
################################################################################################



################################################################################################
##################################### Education Code ###########################################


# Retrieving the whole div with the education data in it
edu_back = Selector(text=response.xpath('//div[contains(@class,"background-education")]').extract()[0])

# Retrieving the list of divs which host individual experiences
edu_divs = edu_back.xpath('//div[contains(@class,"section-item")]').extract()

#Looping over each education div to get the required data
for edu_div in edu_divs:

    # Generating a selector for each education div
    edu_sel = Selector(text=edu_div)

    # Institute/College/School of Education
    print "Institute/College/School is : " + edu_sel.xpath('//h4/a/text()').extract()[0]

    # Degree of the student in this education
    degree = edu_sel.xpath('//header/h5/span[contains(@class,"degree")]/text()').extract()

    if not degree:
        print "The user does not have a degree in this particular education"
    else:
        print degree[0]

    # Major of the student in this Education
    major = edu_sel.xpath('//header/h5/span[contains(@class,"major")]/a/text()').extract()

    if not major:
        print "The user does not have a major in this particular education"
    else:
        print major[0]

    # from date and to date of this education
    dates = edu_sel.xpath('//span[contains(@class,"education-date")]/time/text()').extract()

    if not dates:
        print "The dates and duration have not been mentioned for this education"
    elif len(dates) == 1:
        print dates[0] + " - present"
    else:
        print dates[0] + "" + dates[1]

    # Activities and Societies of the candidate during this education
    act_soc = edu_sel.xpath('//p[contains(@class,"activities")]/a/text()').extract()

    # Looping through all his activities and societies
    for a_s in act_soc:
        print "The following activity was done by the candidate during this education: " + a_s


    # Courses taken by the student during his education
    courses = edu_sel.xpath('//dl[contains(@class,"education-associated")]/dd/ul/li/text()').extract()

    # Looping through all his courses
    for course in courses:
        print "This course has been taken during his education here: " + course







