import scrapy


class LatestGamesSpider(scrapy.Spider):
    name = "latest_games"
    allowed_domains = ["store.steampowered.com"]
    start_urls = ["https://store.steampowered.com/?l=japanese"]

    def parse(self, response):
        for i, game in enumerate(response.xpath('//*[@id="tab_newreleases_content"]/a')):
            yield {
                'Title': game.xpath('.//div[3]/div[1]/text()').get(),
                'URL': game.xpath('.//@href').get()
            }
            if i == 10:
                break

        # 初期記述
        # for i in range(1, 12):
        #     yield {
        #         'Title': response.xpath('//*[@id="tab_newreleases_content"]/a[' + str(i) + ']/div[3]/div[1]/text()').get(),
        #         'URL': response.xpath('//*[@id="tab_newreleases_content"]/a[' + str(i) + ']/@href').get()
        #     }

        pass
