import scrapy

class ImdbSpider(scrapy.Spider):

	name = "imdb_spider"
	start_urls = [
		"https://www.imdb.com/title/tt2085059/"
	]

	def parse(self, response):
		"""
		This method finds and navigates to the Cast&Crew section of the web page, 
		and calls parse_full_credits()
		"""
		# Cast&Crew button is nexted in a list of class "ipc-inline-list__item"
		# get the url associated with the button
		cast = response.css("li.ipc-inline-list__item a")[2].attrib["href"]
		# construct the absolute path
		cast = response.urljoin(cast)
		# call parse_full_credits()
		yield scrapy.Request(cast, callback = self.parse_full_credits)

	
	def parse_full_credits(self, response):
		"""
		This method finds and navigates to each actor's web page, 
		and calls parse_actor_page()
		"""	
		# for each actor, find their photo	
		for actor in response.css("td.primary_photo a"):
			# get the url associated with the photo
			actor_page = actor.attrib["href"]
			# construct the absolute path
			actor_page = response.urljoin(actor_page)
			# call parse_actor_page()
			yield scrapy.Request(actor_page, callback = self.parse_actor_page)


	def parse_actor_page(self, response):
		"""
		This method extracts the actor's name and movies/TV shows they have played, 
		and return a dictionary storing the relevant information
		"""	
		# extract actor's name		
		actor_name = response.css("h1.header").css("span.itemprop::text").get()
		# for each work under the Filmograph section, get the name
		for work in response.css("div.filmo-row b"):
			# get the name of the movie/TV show
			movie_or_TV_name = work.css("a::text").get()
			yield { # a generator that spits out a dictionary of actor's name and the movie/TV show one at a time
		 		"actor_name": actor_name,
		 		"movie_or_TV_name": movie_or_TV_name
		 	}

