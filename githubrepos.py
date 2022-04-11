import sys
from github import Github


def get_github_repos(username):
    g = Github()
    user = g.get_user(username)

    for repo in user.get_repos():
        print(repo)


def main():
    get_github_repos(sys.argv[1])


if __name__ == '__main__':
    main()
