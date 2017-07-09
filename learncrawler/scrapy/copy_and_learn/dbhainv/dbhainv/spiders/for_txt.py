from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from dbhainv.items import DoubanimageItem
class DouBanImage(BaseSpider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [];
    f = open('douban.txt', 'wb')
    for i in range(0,1900,40):
        start_urls.append('http://movie.douban.com/subject/10581289/photos?type=S&start=%d&sortby=vote&size=a&subtype=a'%i)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li/div/a/img/@src').extract()
        items = []
        for site in sites:
            site = site.replace('thumb','photo')
            self.f.write(site)
            self.f.write('\r\n')
            item = DoubanimageItem()
            item['ImageAddress'] = site
            items.append(item)
        return items
