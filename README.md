## test  
cd {elasticsearch home}/bin     
./elasticsearch  
excute program  
localhost:9200/scrapy/_search?q=*&pretty  
  
## next task
* 단일 사이트 풀 크롤링, 오토 쓰로틀링 및 딜래이 설정
* 에러 및 로깅 처리
* [LinkExtrator](http://doc.scrapy.org/en/1.0/topics/link-extractors.html#module-scrapy.linkextractors.lxmlhtml) 검토
* 자동화(참조. [api](https://github.com/scrapy/scrapyd))
* Lucene 연계 방법 검토(Solr은 연계할 수 있는듯.하지만 Lucene은???)
* elasticsearch 연동 시 문제점 검토
* broad crawling 구현(참조.[broad crawl](http://doc.scrapy.org/en/1.0/topics/broad-crawls.html),[redis를 이용한 크롤링 분산처리](https://getpocket.com/a/read/1100339970))
* 웹 서비스의 개발(참조.[scrapy-jsonrpc](https://github.com/scrapy-plugins/scrapy-jsonrpc))
* 운영 상에서 필요한 것들 및 기타 검토 사항...([Telnet Console](http://doc.scrapy.org/en/1.0/topics/telnetconsole.html))  
* 유닛 테스트는 어떻게 해야 할까?([Spiders Contracts](http://doc.scrapy.org/en/1.0/topics/contracts.html))