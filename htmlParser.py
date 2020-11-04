from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):

    contributionDates = list()

    def handle_starttag(self, tag, attrs):
        if (tag == "rect"):
            if (('class', 'day') in attrs):
                contributionDate = {}

                for name, value in attrs:
                    if name == "data-count":
                        contributionDate[name] = int(value)
                    if name == "data-date":
                        contributionDate[name] = value

                self.contributionDates.append(contributionDate)
