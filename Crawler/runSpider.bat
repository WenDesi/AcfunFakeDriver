@echo off  
E:  
cd E:\python\AcfunFakeDriver\Crawler
start python crawler_manager.py
ping 0.0.0.0  -n 3 > null
cd AcFunComment
start scrapy crawl comment

exit