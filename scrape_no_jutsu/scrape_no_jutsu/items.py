# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeNoJutsuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LinkedInItem(scrapy.Item):
    # name of the person
    name = scrapy.Field()

    # All the previous experiences of the candidate, along with the following data:
    # 0-designation, 1-organization, 2-from_date, 3-to_date, 4-location, 5-description
    # experiences[x][] : x will be the iterator for various experiences
    # experiences[][y] : y will be the iterator for all the information related to each experience
    experiences = scrapy.Field()

    # current designation, as in linked in
    current = scrapy.Field()

    # previous designation, as in linked in
    previous = scrapy.Field()

    # All the educational information pertaining to the candidate, in the following format:
    # 0-university, 1-degrees, 2-major, 3-from_date, 4-to_date, 5-activities_societies, 6-courses
    # educations[x][y][z] : x will be the iterator for various educational qualifications
    # educations[x][y][z] : y will be the iterator for all the information related to each education
    # educations[x][y][z] : z will be the optional iterator, incase any field has multiple entries
    educations = scrapy.Field()

    # email of the person, as in linked in
    email = scrapy.Field()

    # instant messaging service used by the person, as in linked in
    im = scrapy.Field()

    pass
