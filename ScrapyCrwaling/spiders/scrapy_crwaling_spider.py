# -*- coding: utf-8 -*-

import scrapy
import sys
import re

from ScrapyCrwaling.CivilAppealLoader import CivilAppealLoader
from ScrapyCrwaling.items import ScrapycrwalingItem

reload(sys)
sys.setdefaultencoding('utf-8')


# 민원 정보를 스크래랩핑한다.
class CivilAppealSpider(scrapy.Spider):
    name = "CivilAppeal"
    allowed_domains = ["eminwon.seoul.kr"]

    domain = 'https://gangnam.eminwon.seoul.kr'
    searchLocation = '/emwp/gov/mogaha/ntis/web/caf/mwwd/action/CafMwWdOpenAction.do'
    searchUri = domain + searchLocation

    # TODO: 파라미터는 조작이 가능하게 셋팅해야 한다.
    listParam = {
        'menu_id': 'CAFOPNWebMwOpenL'
        , 'method': 'selectListMwOpn'
        , 'jndinm': 'CafMwWdOpenEJB'
        , 'methodnm': 'selectListMwOpn'
        , 'context': 'NTIS'
        , 'mw_take_no': ''
        , 'mw_aplct_pwd': ''
        , 'strt_date': '20160203'
        , 'end_date': '20160210'
        , 'pageIndex': '1'
        , 'pageSize': '50'
        , 'field': 'mw_date'
        , 'keyword': ''
        , 'pageSize1': '50'
        , 'strt_yy': '2016'
        , 'strt_mm': '02'
        , 'strt_dd': '03'
        , 'end_yy': '2016'
        , 'end_mm': '02'
        , 'end_dd': '10'
        , 'pageSize2': '50'
    }

    def start_requests(self):
        return [scrapy.FormRequest(self.searchUri,
                                   method='POST',
                                   formdata=self.listParam,
                                   callback=self.parse)]

    def parse(self, response):
        # 전체 페이지 수를 얻어 각 페이지를 순환하며 페이지 링크를 얻어온다.
        # 해결건만을 추려 상세 건을 얻어온다.
        count = re.search('[0-9]+', response.xpath('//table/tr/td[@width="100"]/text()').extract()[1]).group(0)
        page_count = 50.0
        total = int(round(float(count) / page_count))

        for pageNumber in range(1, total + 1):
            list_param = self.listParam.copy()
            list_param['pageIndex'] = str(pageNumber)
            yield scrapy.FormRequest(self.searchUri,
                                     method='POST',
                                     formdata=list_param,
                                     callback=self.parse_list)

    def parse_list(self, response):
        for index, status in enumerate(response.xpath('//table[@class="table-caf-02"]/tr/td[5]/text()').extract()):
            if status == "해결":
                key = re.search('[0-9]+', response.xpath('//table[@class="table-caf-02"]/tr/td[3]//@href')
                                .extract()[index]).group(0)
                print key
                # detail 파라미터 리펙토링 필요
                detail_param = {
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
                    response.urljoin('/emwp/gov/mogaha/ntis/web/caf/mwwd/action/CafMwWdOpenAction.do'),
                    method='POST', formdata=detail_param, callback=self.parse_detail)

    def parse_detail(self, response):
        # item_loader = CivilAppealLoader(ItemLoader(item=ScrapycrwalingItem(), response=response))
        item_loader = CivilAppealLoader(item=ScrapycrwalingItem(), response=response)
        item_loader.add_xpath("no", "//table[@class='table-caf-04'][1]/tr[1]/td[1]/text()")
        item_loader.add_xpath("content", "//table[@class='table-caf-04'][4]/tr[5]/td[1]/text()")
        item = item_loader.load_item()
        yield item
