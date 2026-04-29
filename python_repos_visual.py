import requests
import plotly.express as px

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories'
url += '?q=language:python&sort=stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)  
print(f'Status code: {r.status_code}')

# Process results.
response_dict = r.json()    
print(f'Total repositories: {response_dict["total_count"]}')

# Explore information about the repositories.
repo_dicts = response_dict['items']
repo_names, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # Build hover text for each repository.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f'{owner}<br />{description}'
    hover_texts.append(hover_text)

# Create a bar chart to visualize the star counts.
fig = px.bar(x=repo_names, y=stars, labels={'x': 'Repository', 'y': 'Stars'})
fig.show()