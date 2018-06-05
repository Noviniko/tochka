from setuptools import setup


setup(
	name='tochka', 
	packages=['tochka',],
	version='0.0.1',
	url='https://github.com/Noviniko/tochka',
	author='Nikolay',
	author_email='noviniko97@gmail.com',
	description='This utility displays a list of repository GitHub that a particular user rated with a star and the number of stars for each repository',
	entry_points={
		'console_scripts': [
			'tochka = tochka.tochka:main',
		# We use this line to map our `main()` method in tochka.py
		# to a shell command `tochka`
		],
	},
)
