import urllib.request as request


def fetchProfilePage(gitHubUser):
    with request.urlopen("https://github.com/{}".format(gitHubUser)) as response:
        html = response.read()
        return html


def main():
    gitHubUser = "prottonicfusion"
    profilePage = fetchProfilePage(gitHubUser)
    print(profilePage)


if __name__ == "__main__":
    main()
