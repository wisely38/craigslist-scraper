 #
 # 
 # Copyright (C) 2018 Raymond Wai Yan Ko <wisely38@hotmail.com>
 #
 # 
 # This file is part of craigslist-scraper.
 # 
 # craigslist-scraper cannot be copied and/or distributed for commercial use 
 # without the express permission of Raymond Wai Yan Ko <wisely38@hotmail.com>
 #
 #

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# from scrapy.signals import item_scraped


def my_callback_function(item, response, spider):
    # Processing here...
    pass


process = CrawlerProcess(get_project_settings())
process.crawl('indeed_dataengineer_spider', 'https://www.indeed.com/jobs?q=data%20engineer&l=San%20Francisco%2C%20CA')

# for crawler in process.crawlers:
#     crawler.signals.connect(my_callback_function, item_scraped)
#
# process.start() # the script will block here until the crawling is finished
# crawler.signals.connect(my_callback_function, item_scraped)

process.start()  # the script will block here until the crawling is finished
