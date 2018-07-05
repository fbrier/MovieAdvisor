from IronwoodScraper import IronwoodScraper
import pyttsx

engine = pyttsx.init()

scraper = IronwoodScraper()
ironwoodMovies = scraper.fetch()
showing = "Ironwood is showing the following movies: "
for m in ironwoodMovies:
    m.dump()
    print

showing = scraper.name + " is showing the following movies: " + ", ".join([x.name.strip() for x in ironwoodMovies])
print showing
engine.say(showing)
engine.runAndWait()