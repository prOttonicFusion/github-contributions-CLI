import urllib.request as request
from htmlParser import CustomHTMLParser


def fetchProfilePage(gitHubUser):
    with request.urlopen("https://github.com/{}".format(gitHubUser)) as response:
        html = response.read().decode("utf8")
        return html


def parseContributions(htmlPage):
    parser = CustomHTMLParser()
    parser.feed(htmlPage)
    return parser.contributionDates


def main():
    gitHubUser = "prottonicfusion"
    profilePage = fetchProfilePage(gitHubUser)
    dateData = parseContributions(profilePage)


if __name__ == "__main__":
    main()
