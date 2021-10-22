import scrapy

class ImdbSpider(scrapy.Spider):

	name = "imdb_spider"
	start_urls = [
		"https://www.imdb.com/title/tt2085059/"
	]

	def parse(self, response):
		cast = response.css("li.ipc-inline-list__item a")[2].attrib["href"]
		cast = response.urljoin(cast)
		yield scrapy.Request(cast, callback = self.parse_full_credits)

	
	def parse_full_credits(self, response):
		for actor in response.css("td.primary_photo a"):
			actor_page = actor.attrib["href"]
			actor_page = response.urljoin(actor_page)
			yield scrapy.Request(actor_page, callback = self.parse_actor_page)


	def parse_actor_page(self, response):
		actor_name = response.css("h1.header").css("span.itemprop::text").get()
		for work in response.css("div.filmo-row b"):
			movie_or_TV_name = work.css("a::text").get()
			yield { # a generator that spits on a dictionary one at a time
		 		"actor_name": actor_name,
		 		"movie_or_TV_name": movie_or_TV_name
		 	}

