import sys
import MySQLdb
from scrapy.exceptions import DropItem
from scrapy.http import Request

d = MySQLdb.connect(host='localhost', user='root', passwd='a', db='scrape_no_jutsu')
cur = d.cursor()

cur.execute('SELECT id FROM users WHERE name="%s"' % ('Abhishek Sharma'))
result = cur.fetchone()
print result[0]

