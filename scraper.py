import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
	'''
	This attempts a HTTP GET request pointed at the given 'url'.
	If the content type is HTML or XML, return the text content;
	otherwise, return None. 
	'''
	try:
		with closing(requests.get(url, stream=True)) as resp:
			if is_good_response(resp):
				return resp.content
			else:
				print('Bad response.')
				return None
	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None

def is_good_response(resp):
	'''
	This returns true is the response appear to be valid HTML; otherwise false.
	'''
	content_type = resp.headers['Content-Type'].lower()
	return (resp.status_code == 200 and content_type is not None and 'html' in content_type)

def log_error(e):
	'''
	Show error
	'''
	print(e)