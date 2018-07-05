import requests
from bs4 import BeautifulSoup, ResultSet, NavigableString
import re

from Movie import Movie

class IronwoodScraper:

    def __init__(self):
        self.url = "http://ironwoodcinemas.com/"
        self.name = "Ironwood 8 Cinemas"

    def fetch(self):
        result = requests.get(self.url)
        if (result.status_code != 200) :
            return false

        movieList = []
        content = result.content
        soup = BeautifulSoup(content, 'html.parser')
        samples = soup.find_all(id="showtimes")  # type: ResultSet
        for s in samples:
            curMovie = Movie()
            nametag = s.find("a", "name")
            # curMovie.name =
            m = re.search('\s*([ \w:;\'\"\&\%\#\@\!\+\=\/\<\>\{\}\-,\.]+)\s*\(([0-9A-Z\-]+)\)\s*', nametag.contents[0])
            curMovie.name = m.group(1)
            curMovie.rated = m.group(2)
            runTime = s.find_all("span", class_="smallfont")[1].contents[0]
            times = s.find("span", text="Today: ").next_sibling.next_sibling
            while self.expiredMovieTime(times) and not (times.name == 'br'):
                times = times.next_sibling
            if not (times.name == 'br'):
                curMovie.times = times.replace(',', ' ').split()
            movieList.append(curMovie)
        return movieList

    def expiredMovieTime(self, timeElement):
        # type: (object) -> bool
        isExpired = (not isinstance(timeElement, NavigableString)) or not timeElement.replace(',', ' ').strip()
        return isExpired



