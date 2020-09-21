import requests
import json
from datetime import datetime

def getAuthorData(a):
    return requests.get(f'https://api.github.com/users/{a}/repos').json()

def getRepoList():
    with open('repos.txt') as r:
        return [i.strip() for i in r.read().lower().strip().split('\n')]

def parseDatetime(dt):
    return datetime.strptime(dt, '%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    repoList = getRepoList()
    authors, repos = zip(*[i.split('/') for i in repoList])
    
    authorData = {}
    for a in set(map(lambda x : x.lower(), authors)):
        authorData[a] = getAuthorData(a)

    repoData = []
    for a, r in zip(authors, repos):
        matchingRepos = [i for i in authorData[a] if i['name'].lower() == r.lower()]

        if len(matchingRepos) == 0:
            print(f'Repo {a}/{r} not found!')
            
        repo = matchingRepos[0]

        repoData.append({
            'name': repo['name'],
            'owner': repo['owner']['login'],
            'has_pages': repo['has_pages'],
            'language': repo['language'],
            'description': repo['description'],
            'url': repo['html_url'],
            'stars': repo['stargazers_count'],
            'watchers': repo['watchers_count'],
            'forks': repo['forks'],
            'created_at': repo['created_at']
        })

    repoData = sorted(repoData, key = lambda x : parseDatetime(x['created_at']), reverse=True)

    with open('repos.json', 'w') as r:
        json.dump(repoData, r)
