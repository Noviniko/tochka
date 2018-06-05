import requests
import argparse


def github_starring(username):
	url = 'https://api.github.com/users/{}/starred'.format(username)
	r = requests.get(url)
	if r.status_code == 200:
		if 'link' in r.headers:
			stars = []
			last_page = r.links['last']['url']
			while r.url != last_page:
				stars.extend(['{} - {}'.format(item["full_name"], item["stargazers_count"]) for item in r.json()])
				r = requests.get(r.links['next']['url'])
			stars.extend(['{} - {}'.format(item["full_name"], item["stargazers_count"]) for item in r.json()])
			return stars
		else:
			return ['{} - {}'.format(item["full_name"], item["stargazers_count"]) for item in r.json()]
	else:
		return False


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("username", help="display a list of repositories that the user rated on GitHub "
										 "and the number of stars of each repository")
	args = parser.parse_args()

	response = github_starring(args.username)
	if response is not False:
		if len(response) > 0:
			for repository in response:
				print(repository)
		else:
			print("This user has not yet given star for any repository")
	else:
		print("User not found")

