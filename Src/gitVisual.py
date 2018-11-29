from github import Github
import getpass

def main():
user = False
    while(not user):
        username = input("Enter your Github Username:\n")
        password = getpass.getpass(prompt='Enter your password:\n')
        try:
            g = Github(username, password)
            user = True
        except:
            print("Try again")

if __name__== "__main__":
  main()
