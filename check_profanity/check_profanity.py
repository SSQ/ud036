

def read_text():
    quotes = open("F:\Udacity\ud036\check_profanity\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text()
