from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class DownloadImg(BaseSpider):
   name = "readimg"
   allowed_domains = ["douban.com"]
   start_urls = []
   f = open("E:\\somegit\\learncrawler\\scrapy\\dbhainv\\douban.txt",'r')
   line = f.readline()
   while line:
       start_urls.append(line)
       line = f.readline()
   counter = 0

   def parse(self, response):
       str = response.url[0:-3]
       self.counter = self.counter+1
       str = str.split('/')
       print '--------------------------------DownLoad Finished',self.counter,str[-1]
       imgfile = open(str[-1],'wb')
       imgfile.write(response.body)





