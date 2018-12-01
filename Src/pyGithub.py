from github import Github
import getpass

user = False
while(not user):
    username = input("Enter your Github Username:\n")
    password = getpass.getpass(prompt='Enter your password:\n')
    try:
        g = Github(username, password)
        user = True
    except:
        print("Try again")

# print username
user = g.get_user()
print(user.login + "\n")

# print repos
for repo in g.get_user().get_repos():
    print(repo.name)
