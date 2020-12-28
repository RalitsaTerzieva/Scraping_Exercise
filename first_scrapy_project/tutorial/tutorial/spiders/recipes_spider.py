import scrapy


class RecipesSpider(scrapy.Spider):
    name = "recipes"

    start_urls = [
        'https://sprinkledfood.com/category/vegan/' 
    ]
       

    def parse(self, response):
        for post in response.css('div.archive-item-content'):
            title = post.css('.archive-item-header h3 a::text')[0].get()
            prep = post.css('.archive-item-meta-cooking-time::text')[0].get()
            yield {
                'title': title,
                'preparation': prep
            }
        
        next_page = response.css('.archive-pagination-next::attr(href)').get()
        if next_page is not None:
             yield response.follow(next_page, callback=self.parse)