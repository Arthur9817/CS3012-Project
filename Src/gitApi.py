import requests
import csv

def main():
    repo_list = []
    stars_list = []

    repos = requests.get('https://api.github.com/search/repositories?q=stars%3A>1&sort=stars&order=desc&page=&per_page=10&rel="next"').json()
    for item in repos['items']:
        repo_list.append(item['name'])
        stars_list.append(item['stargazers_count'])

    with open('data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Repo', 'Stars'])
        for i in range(len(repo_list)):
            writer.writerow([repo_list[i],stars_list[i]])

if __name__== "__main__":
  main()
