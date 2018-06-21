from logging import getLogger

import scrapy
from pydispatch import dispatcher
from scrapy import item, signals

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.utils import response

from scrapy.contrib.loader import ItemLoader

from MPspider.items import WxhItem
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class WxhSpider(scrapy.Spider):
    name = "Wxhspider"
    allowed_domains = ['sogou.com']

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1400, 700)


    def __del__(self):
        self.browser.close()


    def parse(self, response):
        sel = scrapy.Selector(response)
        sel.

    def start_requests(self):

        url = 'http://weixin.sogou.com/'
        browser = webdriver.Chrome()
        browser.get(url)
        elem = browser.find_element_by_xpath('//*[@id="query"]')
        elem.clear()
        elem.send_keys("GQ实验室")
        scbutton = browser.find_element_by_class_name('swz2')
        scbutton.click()



        # for query in MPname:
        #     query.encode()
        #     query_url = 'http://weixin.sogou.com/weixin?type=1&' \
        #                 's_from=input&query=' + query + '&ie&=utf8&_sug_=n&_sug_type_'
        #     yield scrapy.Request(
        #         query_url,
        #         meta={},
        #         callback=self.parse,
        #         errback=self.error
        #     )

    def parse(self, response):
        self.logger.info("Start to parse the url %s \n", response.url)
        item = ItemLoader(item=WxhItem(), response=response)
        item.add_xpath('mpid', '//div[@class="news-box"]//li//div[@class="txt-box"]//p[@class="info"]//label//text()')
        item.add_xpath('mpname', '//div[@class="news-box"]//li//div[@class="txt-box"]//p[@class="tit"]//a//em/text()')
        item.add_xpath('url', '//div[@class="news-box"]//li//div[@class="img-box"]//a//@href')

        # item['mpid'] = response.xpath('//div[@class="news-box"]//li//div[@class="txt-box"]//p['
        #                               '@class="info"]//label//text()')
        #
        # item['mpname'] = response.xpath('//div[@class="news-box"]//li//div[@class="txt-box"]//p['
        #                                 '@class="tit"]//a//em/text()')
        #
        # item['url'] = response.xpath('//div[@class="news-box"]//li//div[@class="img-box"]//a//@href')

    def closed(self, reason):
        self.driver.quit()
