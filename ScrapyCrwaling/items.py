# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapycrwalingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    #접수
    #접수번호
    no = scrapy.Field()
    #접수일자
    acceptDate = scrapy.Field()
    #처리기한
    #민원사무명
    #접수부서
    #접수담당자
    #전화번호
    #이메일

    #진행내역
    #처리내용
    content = scrapy.Field()