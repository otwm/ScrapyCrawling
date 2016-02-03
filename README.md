## test  
cd {elasticsearch home}/bin     
./elasticsearch  
excute program  
localhost:9200/scrapy/_search?q=*&pretty  
  
## next task
* 단일 사이트 풀 크롤링, 오토 쓰로틀링 및 딜래이 설정
* 에러 및 로깅 처리
* 자동화
* elasticsearch 연동 보강
* broad crawling 구현(참조.[broad crawl](http://doc.scrapy.org/en/1.0/topics/broad-crawls.html),[redis를 이용한 크롤링 분산처리](https://getpocket.com/a/read/1100339970))
* 웹 서비스의 개발(참조.[scrapy-jsonrpc](https://github.com/scrapy-plugins/scrapy-jsonrpc))  