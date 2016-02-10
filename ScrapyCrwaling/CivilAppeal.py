# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from pip._vendor.html5lib import serializer


class CivilAppeal(scrapy.Item):
    no = scrapy.Field()

    #접수
    accept = {}
    #접수번호
    accept['no'] = scrapy.Field()
    #접수일자
    accept['acceptDate'] = scrapy.Field()
    #처리기한
    accept['limitDate'] = scrapy.Field()
    #민원사무명
    accept['office'] = scrapy.Field()
    #접수부서
    accept['department'] = scrapy.Field()
    #접수담당자
    accept['person_in_charge'] = scrapy.Field()
    #전화번호
    accept['tel'] = scrapy.Field()
    #이메일
    accept['email'] = scrapy.Field()

    #진행내역
    #process_history = {}
    #작업종류
    #process_history[]
    #담당자
    #부서
    #일시
    #전화번호
    #이메일

    #결제 진행 상태
    #기안제목
    #결재권자
    #결재결과
    #결재일시
    #결재의견

    #현재상태
    #처리구분
    #해결	처리일자	2016-02-05
    #처리부서	도시환경국 환경과
    #처리담당자	강민희
    #전화번호	02-3423-6227
    #이메일	cm314@gangnam.go.kr
    #처리근거
    #reason
    #처리내용
    #content = scrapy.Field()