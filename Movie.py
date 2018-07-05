class Movie:
    def __init__(self):
        self.name = ""
        self.genre = ""
        self.times = []
        self.ratings = {}
        self.rated = ""

    def dump(self):
        print "Name: " + self.name
        print "Rated: " + self.rated
        print "Times: " + ",".join([str(x) for x in self.times])
