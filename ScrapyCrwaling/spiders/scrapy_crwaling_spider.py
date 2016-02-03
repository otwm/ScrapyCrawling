# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import sys
import re

from ScrapyCrwaling.items import ScrapycrwalingItem

reload(sys)
sys.setdefaultencoding('utf-8')


def make(key):
    startUrl = "https://gangnam.eminwon.seoul.kr"
    detailUrl = "/emwp/gov/mogaha/ntis/web/caf/mwwd/action/CafMwWdOpenAction.do"
    startUrl + detailUrl


class CivilAppealSpider(scrapy.Spider):
    name = "CivilAppeal"
    allowed_domains = ["eminwon.seoul.kr"]
    start_urls = [
        "https://gangnam.eminwon.seoul.kr/emwp/gov/mogaha/ntis/web/caf/mwwd/action/CafMwWdOpenAction.do?method=selectListMwOpn&menu_id=CAFOPNWebMwOpenL&jndinm=CafMwWdOpenEJB&methodnm=selectListMwOpn&context=NTIS"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #    f.write(response.body)

        startUrl = "https://gangnam.eminwon.seoul.kr"
        detailUrl = "/emwp/gov/mogaha/ntis/web/caf/mwwd/action/CafMwWdOpenAction.do"

        for index, status in enumerate(response.xpath('//table[@class="table-caf-02"]/tr/td[5]/text()').extract()):
            if status == "해결":
                key = re.search('[0-9]+', response.xpath('//table[@class="table-caf-02"]/tr/td[3]//@href')
                                .extract()[index]).group(0)
                print key
                myFormData = {
                    'method': 'selectMwOpnDtl'
                    , 'jndinm': 'CafMwWdOpenEJB'
                    , 'methodnm': 'selectMwOpnDtl'
                    , 'context': 'NTIS'
                    , 'mw_take_no': key
                    , 'mw_aplct_pwd': ''
                    , 'strt_date': ''
                    , 'end_date': ''
                    , 'pageIndex': ''
                    , 'pageSize': ''
                    , 'field': 'mw_date'
                    , 'keyword': ''
                    , 'pageSize1': '20'
                    , 'strt_yy': '2016'
                    , 'strt_mm': '01'
                    , 'strt_dd': '27'
                    , 'end_yy': '2016'
                    , 'end_mm': '02'
                    , 'end_dd': '03'
                    , 'pageSize2': '20'
                }

                yield scrapy.FormRequest(
                    startUrl + detailUrl, method='POST', formdata=myFormData, callback=self.parse_dir_contents)

                # Request(startUrl + detailUrl,callback=self.parse_dir_contents,method='POST')

    def parse_dir_contents(self, response):
        item = ScrapycrwalingItem()
        item['no'] = (response.xpath("//table[@class='table-caf-04'][1]/tr[1]/td[1]/text()").extract()[:1] or [None])[0]
        item['acceptDate'] = (response.xpath("//table[@class='table-caf-04'][1]/tr[2]/td[1]/text()").extract()[:1] or [None])[0]
        item['content'] = (response.xpath("//table[@class='table-caf-04'][4]/tr[5]/td[1]/text()").extract()[:1] or [None])[0]
        yield item