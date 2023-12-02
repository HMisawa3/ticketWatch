import scrapy


class LatestGamesSpider(scrapy.Spider):
    name = "latest_games"
    allowed_domains = ["store.steampowered.com"]
    start_urls = ["https://store.steampowered.com/?l=japanese"]

    def parse(self, response):
        # 妥協案
        for i in range(1, 12):
            yield {
                'Title': response.xpath('//*[@id="tab_newreleases_content"]/a[' + str(i) + ']/div[3]/div[1]/text()').get(),
                'URL': response.xpath('//*[@id="tab_newreleases_content"]/a[' + str(i) + ']/@href').get()
            }

        # やりたかった奴
        # latest_games = response.xpath('//*[@id="tab_newreleases_content"]/a')
        # for game in boolatest_gamesks:
        #     yield {
        #         # 'Title': game.xpath('.//div[3]/div[1]/text()').get(),
        #         'URL': game.xpath('.//@href').get()
        #         ##### CSSでの取得は下記
        #         # 'Title': book.css('a::attr(title)').get(),
        #         # 'URL': book.css('a::attr(href)').get()
        #     }

        # 単一には取得できる
        # yield {
        #     'Title': response.xpath('//*[@id="tab_newreleases_content"]/a[1]/div[3]/div[1]/text()').get(),
        #     'URL': response.xpath('//*[@id="tab_newreleases_content"]/a[1]/@href').get()
        # }
        pass
