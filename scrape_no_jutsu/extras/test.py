from scrapy.selector import Selector
from scrapy.http import HtmlResponse

with open ("contacts", "r") as myfile:
    data = myfile.read()
    myfile.close()

response = Selector(text=data)

# Select the div which has all the contacts information
cont_back = response.xpath('//section[@id="contact-list-container"]').extract()[0]

# Selector for the div which has all contacts info
cont_sel = Selector(text=cont_back)

# Selecting the total number of contacts
total_cont = cont_sel.xpath('//header/section/span/strong/text()').extract()[0]

# Selecting the array of all the contacts divs under the cont_back div
all_cont = cont_sel.xpath('//ul/li[contains(@class,"contact-item-view")]').extract()

# Checking the number of contacts obtained
if not all_cont:
    print "There are no contacts in this page"
elif len(all_cont) < total_cont:
    print "The page has not fully loaded with AJAX data"
else:
    print "All the contacts have been obtained"
