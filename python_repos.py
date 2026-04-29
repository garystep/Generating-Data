import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories'
url += '?q=language:python&sort=stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)  
print(f'Status code: {r.status_code}')

# Convert the response to a dictionary and print the number of repositories.
response_dict = r.json()

# Process results.
print(f'Total repositories: {response_dict["total_count"]}')
print(f'Items in this response: {len(response_dict["items"])}')

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f'\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print(f'\nName: {repo_dict["name"]}')
    print(f'Owner: {repo_dict["owner"]["login"]}')
    print(f'Stars: {repo_dict["stargazers_count"]}')
    print(f'Repository: {repo_dict["html_url"]}')
    print(f'Description: {repo_dict["description"]}')

