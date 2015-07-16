# -*- coding: utf-8 -*-

# Scrapy settings for scrape_no_jutsu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrape_no_jutsu'

SPIDER_MODULES = ['scrape_no_jutsu.spiders']
NEWSPIDER_MODULE = 'scrape_no_jutsu.spiders'
ITEM_PIPELINES = {
            'scrape_no_jutsu.pipelines.ScrapeNoJutsuPipeline': 300,
        }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrape_no_jutsu (+http://www.yourdomain.com)'
