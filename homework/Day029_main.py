import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_board = ['Stock', 'Gossiping']
    #target_board = ['Gossiping']
    process = CrawlerProcess(get_project_settings())
    for board in target_board:
        print('board: ', board)
        process.crawl('PTTCrawler', board=board)
    process.start()
      
    
if __name__ == '__main__':
    main()
