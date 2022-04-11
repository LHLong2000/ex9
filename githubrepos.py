import requests
import sys
import argparse
import base64
from github import Github


def get_github_repos():
    print(sys.path)
    username = "pymivn"
    g = Github()
    user = g.get_user(username)

    for repo in user.get_repos():
        print(repo)

    # for repo in user.get_repos():
    #     print_repo(repo)
    #     print("=" * 100)

    # url = f"https://api.github.com/users/{username}"
    # url = f"https://api.github.com/users/{username}/repos"

    # user_data = requests.get(url).json()

    # print(user_data)


# def print_repo(repo):
#     # repository full name
#     print("Full name:", repo.full_name)
#     # repository description
#     print("Description:", repo.description)
#     # the date of when the repo was created
#     print("Date created:", repo.created_at)
#     # the date of the last git push
#     print("Date of last push:", repo.pushed_at)
#     # home website (if available)
#     print("Home Page:", repo.homepage)
#     # programming language
#     print("Language:", repo.language)
#     # number of forks
#     print("Number of forks:", repo.forks)
#     # number of stars
#     print("Number of stars:", repo.stargazers_count)
#     print("-" * 50)
#     # repository content (files & directories)
#     print("Contents:")
#     for content in repo.get_contents(""):
#         print(content)
#     try:
#         # repo license
#         print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
#     except:
#         pass


# Press the green button in the gutter to run the script.
def main():
    get_github_repos()
    # print_repo(repo)


if __name__ == '__main__':
    main()
