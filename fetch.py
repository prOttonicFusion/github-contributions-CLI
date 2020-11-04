import urllib.request as request
from htmlParser import CustomHTMLParser

parser = argparse.ArgumentParser(
    description='Fetch your GitHub contribution stats')
parser.add_argument('-N', metavar='days', type=int, default=7, dest="dayDisplayCount",
                    help='number of days to show (default: 7)')


def fetchProfilePage(gitHubUser):
    with request.urlopen("https://github.com/{}".format(gitHubUser)) as response:
        html = response.read().decode("utf8")
        return html


def parseContributions(htmlPage):
    parser = CustomHTMLParser()
    parser.feed(htmlPage)
    return parser.contributionDates


def main():
    args = parser.parse_args()

    gitHubUser = "prottonicfusion"
    profilePage = fetchProfilePage(gitHubUser)
    dateData = parseContributions(profilePage)


if __name__ == "__main__":
    main()
