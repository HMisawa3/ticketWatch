import scrapy
from ticketWatch.items import Post

class ScrapyBlogSpiderSpider(scrapy.Spider):
    name = "scrapy_blog_spider"
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html']

    def parse(self, response):
        books = response.xpath('//h3')
        # books = response.css('h3')

        for book in books:
            yield {
                'Title': book.xpath('.//a/@title').get(),
                'URL': book.xpath('.//a/@href').get()
                ##### CSSでの取得は下記
                # 'Title': book.css('a::attr(title)').get(),
                # 'URL': book.css('a::attr(href)').get()
            }
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        ##### CSSでの取得は下記
        # next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
        pass
