import scraper
from bs4 import BeautifulSoup
import re

def get_episodes_in_season(num):
	episodes = []
	url = 'https://en.wikipedia.org/wiki/Friends_(season_{})'.format(num)
	raw_html = scraper.simple_get(url)
	html = BeautifulSoup(raw_html, 'html.parser')
	# episodeTable = html.select('table.wikiepisodetable')
	episodeRows = html.select('tr.vevent')
	for row in episodeRows:
		seriesCount = row.select('th')[0].text
		seasonCount = row.select('td')[0].text
		title = row.select('td.summary')[0].text
		episodes.append({
			'seriesCount': seriesCount,
			'seasonCount': seasonCount,
			'title': title
		})
	return episodes

def get_season_hits(num):
	'''
	Accepts a season number and returns the number of hits on its
	Wikipedia page in the last 60 days, and returns that value as an 'int'.
	'''
	summary_url = 'https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/Friends_(season_{})'
	response = scraper.simple_get(summary_url.format(num))
	if response is not None:
		html = BeautifulSoup(response, 'html.parser')
		hitsLink = [a for a in html.select('a') if 'latest-60' in a['href']]
		hitCount = int(hitsLink[0].text.replace(',', ''))
		try:
			return hitCount
		except:
			log_error('Could not parse hit count!')
