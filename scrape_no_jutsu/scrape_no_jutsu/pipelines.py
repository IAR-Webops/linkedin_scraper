# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import MySQLdb
from scrapy.exceptions import DropItem
from scrapy.http import Request

class ScrapeNoJutsuPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost', user='root', passwd='a', db='scrape_no_jutsu')
        self.conn.set_character_set('utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute('SELECT * FROM users WHERE name="%s"' % (item['name'].encode('utf-8')))
            if (self.cursor.rowcount > 0) :
                print "This user is already present in the db"
            else :
                self.cursor.execute("INSERT INTO users (name) VALUES (%s)", (item['name'].encode('utf-8')))
                self.conn.commit()

                self.cursor.execute('SELECT id FROM users WHERE name="%s"' % (item['name'].encode('utf-8')))
                result = self.cursor.fetchone()

                #print item['[experiences']
                for exp in item['experiences']:
                    if (isinstance( exp, ( int, long ) )):
                        self.cursor.execute('INSERT INTO experiences (user_id, designation, organization, from_date, to_date, location, description) VALUES (%s, %s, %s, %s, %s, %s, %s)', ( result[0], item['experiences'][exp][0], item['experiences'][exp][1], item['experiences'][exp][2], item['experiences'][exp][3], item['experiences'][exp][4], item['experiences'][exp][5]))
                        self.conn.commit()

                #print item['educations']
                for edu in item['educations']:
                    if (isinstance( edu, ( int, long ) )):
                        #self.cursor.execute("INSERT INTO educations (user_id, university, degree, major, from_date, to_date) VALUES (%s, %s, %s, %s, %s, %s)", ( result[0], item['educations'][edu][0], item['educations'][edu][1], item['educations'][edu][2], item['educations'][edu][3], item['educations'][edu][4]))
                        self.cursor.execute('INSERT INTO educations (user_id, university, degree, major) VALUES (%s, %s, %s, %s)', (result[0], item['educations'][edu][0], item['educations'][edu][1], item['educations'][edu][2]))
                        self.conn.commit()

                #print result


        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

        return item
