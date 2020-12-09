from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):
    """A class for parsing contribution dates from a HTML string"""

    contributionDates = list()

    def handle_starttag(self, tag, attrs):
        if (tag == "rect"):
            if (('class', 'day') in attrs):
                contributionDate = {}

                for name, value in attrs:
                    if name == "data-count":
                        contributionDate["contribution-count"] = int(value)
                    if name == "data-date":
                        contributionDate["date"] = value

                self.contributionDates.append(contributionDate)
