class ExternalResCatcher:

    def __init__(self, soup):
        self.soup = soup

    def is_externally_hosted(self, path) -> bool:
        # if it contains the CFC's domain name -> False
        if "cfcunderwriting.com" in path:
            return False

        # if it is a http url to externally hosted domains -> True
        if "http" in path and path.index("http", 0) == 0:
            return True
        return False

    def find_resources(self, tag, attr):
        resources = []
        for eachTag in self.soup.findAll(tag):
            try:
                if self.is_externally_hosted(eachTag[attr]):
                    resources.append(eachTag[attr])
            except KeyError:
                pass

        if not resources:
            return None
        return resources
