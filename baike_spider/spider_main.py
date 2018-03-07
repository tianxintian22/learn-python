# coding=utf-8
from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpilderMain(object):
    def __init__(self):
        # url管理器
        self.urls = url_manager.UrlManage()
        # 下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 解析器
        self.parser = html_parser.HtmlParser()
        # 输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        # 抓取的第count个url
        count = 0
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                count += 1
                new_url = self.urls.get_new_url()
                print 'craw %d: %s' %(count, new_url)

                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                # 抓取1000个url
                if count == 1000:
                    break
            except:
                print 'craw failed'

        self.outputer.output_html()

if __name__ == '__main__':
    # 入口url
    root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpilderMain()
    # 启动爬虫
    obj_spider.craw(root_url)