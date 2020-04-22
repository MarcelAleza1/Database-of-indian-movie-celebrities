import scrapy
from ..items import IndianmoviecelebritiesItem

class QuoteSpider(scrapy.Spider):
          name = 'celebrities'
          start_urls = [
                    'https://www.imdb.com/list/ls068010962/'
          ]

          def parse(self,response):
                    items = IndianmoviecelebritiesItem()
                    all_actors = response.css('div.mode-detail')

                    for actor in all_actors:
                              celebrity_name = all_actors.css('.lister-item-header a::text').extract()
                              celebrity_image_link = all_actors.css('img::attr(src)').extract()
                              celebrity_role = all_actors.css('div.text-muted a').extract()
                              celebrity_detail = all_actors.css('div.text-small+ p').extract()

                              items['celebrity_name']=celebrity_name
                              items['celebrity_image_link']=celebrity_image_link
                              items['celebrity_role']=celebrity_role
                              items['celebrity_detail']=celebrity_detail
                             
                              yield items
                    
                    