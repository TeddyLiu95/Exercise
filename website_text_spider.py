# website_text_spider.py
# created on 20th April 2019
'''
This will print the website information text[:1000] 
once you pass the website url.
'''
__author__ = 'TeddyLiu95'
__version__ = '1.0'


import requests
import argparse

def spider(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		print(r.text[:1000])
	except:
		print('爬取失败')

def get_parser():		
	parser = argparse.ArgumentParser(description='To get web information by url')
	parser.add_argument('url', type=str, nargs=1, help='web url')
	return parser
	
def main():
	parser = get_parser()
	args = vars(parser.parse_args())
	url = args['url'][0]
	return spider(url)

if __name__ == '__main__':
	main()