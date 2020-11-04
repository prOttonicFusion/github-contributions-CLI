import argparse
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


def renderDatesForOutput(dateData, dayDisplayCount):
    daysToRender = dateData[-dayDisplayCount:]
    outPutString = ""
    for day in daysToRender:
        outPutString += "{}: {}\n".format(day["date"],
                                          day["contribution-count"])
    return outPutString


def main():
    args = parser.parse_args()

    gitHubUser = "prottonicfusion"
    profilePage = fetchProfilePage(gitHubUser)
    dateData = parseContributions(profilePage)

    print(renderDatesForOutput(dateData, args.dayDisplayCount))


if __name__ == "__main__":
    main()
