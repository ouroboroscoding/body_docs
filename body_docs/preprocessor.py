# coding=utf8
""" Pre processor

Converts markdown formats into appropriate constructs in the given format
"""

__author__		= "Chris Nasr"
__version__		= "1.0.0"
__copyright__	= "Ouroboros Coding Inc."
__email__		= "chris@ouroboroscoding.com"
__created__		= "2025-04-24"

__all__ = [ 'preprocess_html' ]

# Python imports
import re

# Constant regular expressions
_link = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')

def _replace(regex, service) -> str:
	"""Replace

	Looks for links in a string, and if any are found, replaces them using the
	given format

	Arguments:
		replace (dict): The regex format for replacing the found strings
		services (dict): The service info with the nouns
	"""

	# First check the service description
	if _link.search(service['description']):
		service['description'] = re.sub(
			_link, regex['link'], service['description']
		)

	# Step through each request
	for d in service['requests']:

		# If we have a description
		if 'description' in d:

			# Check for links
			if _link.search(d['description']):
				d['description'] = re.sub(
					_link, regex['link'], d['description']
				)

		# If data exists and is a list
		if 'data' in d and isinstance(d['data'], list):

			# Step through each element and check the 'descr' field for links
			for dData in d['data']:
				if _link.search(dData['descr']):
					dData['descr'] = re.sub(
						_link, regex['link'], dData['descr']
					)

		# If error exists and is a list
		if 'error' in d and isinstance(d['error'], list):

			# Step through each element and check the 'descr' field for links
			for dError in d['error']:
				if _link.search(dError['descr']):
					dError['descr'] = re.sub(
						_link, regex['link'], dError['descr']
					)

def preprocess_html(service):
	"""Preprocess HTML

	Gets markdown links and converts them to html links, modifies the data in
	place and does not return anything

	Arguments:

	"""
	_replace({
		'link': r'<a href="\2">\1</a>'
	}, service)