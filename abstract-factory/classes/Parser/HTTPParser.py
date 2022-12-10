from classes.Parser.Parser import Parser
from BeautifulSoup import BeautifulStoneSoup

class HTTPParser(Parser):
    def __call__(self, content):
        filenames = []
        soup = BeautifulStoneSoup(content)
        links = soup.table.findAll('a')
        for link in links:
            filenames.append(link.text)
        return '\n'.join(filenames)