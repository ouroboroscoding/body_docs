from setuptools import setup

with open('README.md', 'r') as oF:
	long_description=oF.read()

setup(
	name='body_docs',
	version='1.0.0',
	description='Provides a cli to generate documentation using body services',
	long_description=long_description,
	long_description_content_type='text/markdown',
	project_urls={
		'Documentation': 'https://github.com/ouroboroscoding/body_docs',
		'Source': 'https://github.com/ouroboroscoding/body_docs',
		'Tracker': 'https://github.com/ouroboroscoding/body_docs/issues'
	},
	keywords=[ 'body', 'rest', 'documentation' ],
	author='Chris Nasr - Ouroboros Coding Inc.',
	author_email='chris@ouroboroscoding.com',
	license='MIT',
	packages=[ 'body_docs' ],
	package_data={ 'body_docs': [
		'templates/*.j2'
	] },
	python_requires='>=3.10',
	install_requires=[
		'Jinja2>=3.1.5,<3.2',
		'strings-oc>=1.0.7,<1.1'
	],
	entry_points={
		'console_scripts': ['body-docs=body_docs.__main__:cli']
	},
	zip_safe=True
)