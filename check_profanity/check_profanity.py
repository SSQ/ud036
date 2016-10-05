import urllib

def read_text():
    quotes = open("F:\Udacity\ud036\check_profanity\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    url = "https://wdylike.appspot.com/?q=" + text_to_check
    #print(url)
    connection = urllib.urlopen(url)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("Curse word not exist")
    else:
        print("Could not scan the document correctly")

read_text()
