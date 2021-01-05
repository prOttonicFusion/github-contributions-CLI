import urllib.request as request
import urllib.error as requestError
from htmlParser import CustomHTMLParser
from colors import bcolors
from colors import styledString
import argparse
import configparser
import math
import os


def initParse():
    """Parse command line arguments & config file contents"""
    dirname = os.path.dirname(__file__)
    config = configparser.ConfigParser()
    config.read(os.path.join(dirname, "config.ini"))

    parser = argparse.ArgumentParser(
        description='Fetch your GitHub contribution stats')
    parser.add_argument('-N', metavar='days', type=int, default=7, dest="dayDisplayCount",
                        help='number of days to show (default: 7)')
    parser.add_argument('-t', '--today', metavar='days', action='store_const', const=1, dest="dayDisplayCount",
                        help='display today\'s contributions (default: 7)')
    parser.add_argument('-u', '--user', metavar='userName', type=str, default=config['DEFAULT']['GitHubUsername'], dest="gitHubUser",
                        help='specify GitHub username (default: read from config.ini)')
    parser.add_argument('-m', '--marker', metavar='markerSymbol', type=str, default="", dest="markerSymbol",
                        help='specify progress bar marker symbol (default: read from config.ini)')

    args = parser.parse_args()

    if (args.gitHubUser == ""):
        print(styledString(
            "GitHub username not specified! Make sure to add it to 'config.ini' or specify one using the '-u' flag", bcolors.FAIL))
        exit(1)
    
    if (args.markerSymbol == ""):
        configFileMarker = config['DEFAULT']['ProgressBarMarker']
        if (configFileMarker != ""):
            args.markerSymbol = configFileMarker
        else:
            args.markerSymbol = "▰"

    return args


def fetchProfilePage(gitHubUser):
    """Attempt to download the GitHub profile page.
    Returns a HTML string on success"""
    try:
        styledString
        with request.urlopen("https://github.com/{}".format(gitHubUser)) as response:
            html = response.read().decode("utf8")
            return html
    except requestError.HTTPError as exc:
        print(styledString("Unable to fetch profile page: ", bcolors.FAIL), exc)
        exit(1)


def parseContributions(htmlPage):
    """Parse a HTML string
    Returns a list of contribution dates"""
    parser = CustomHTMLParser()
    parser.feed(htmlPage)
    return parser.contributionDates


def visualizeContributionCount(count, marker):
    """Returns a visualization string of the inputed contribution count"""
    marker = styledString(marker, bcolors.OKGREEN)
    if (count == 0):
        return ""
    elif (count <= 20):
        return math.ceil(count/2) * marker
    else:
        return marker * 10


def renderDatesForOutput(dateData, dayDisplayCount, marker):
    """Returns a rendered output string"""
    daysToRender = dateData[-dayDisplayCount:]
    outPutString = ""
    for day in daysToRender:
        date = day["date"]
        contributionCount = day["contribution-count"]
        visualization = visualizeContributionCount(contributionCount, marker)

        if visualization == "":
            outPutString += "{}: {}\n".format(date, contributionCount)
        else:
            outPutString += "{}: {} {}\n".format(date,
                                                 visualization,
                                                 contributionCount)
    return outPutString


def main(args):
    profilePage = fetchProfilePage(args.gitHubUser)
    dateData = parseContributions(profilePage)

    print(renderDatesForOutput(dateData, args.dayDisplayCount, args.markerSymbol))


if __name__ == "__main__":
    args = initParse()
    main(args)
