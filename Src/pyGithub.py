from github import Github

# access token
g = Github("25f572250448e6bdbc516c765d575cb89fdb76bd")

# print username
user = g.get_user()
print(user.login + "\n")

# print repos
for repo in g.get_user().get_repos():
    print(repo.name)
