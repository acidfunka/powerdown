import sys
import requests
from BeautifulSoup import BeautifulSoup


def scrape_google(keyword):

    # dynamically build the URL that we'll be making a request to
    url = "http://www.google.com/search?q={term}".format(
        term=keyword.strip().replace(" ", "+"),
    )

    # spoof some headers so the request appears to be coming from a browser, not a bot
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "accept-encoding": "gzip,deflate,sdch",
        "accept-language": "en-US,en;q=0.8",
    }

    # make the request to the search url, passing in the the spoofed headers.
    r = requests.get(url, headers=headers)  # assign the response to a variable r

    # check the status code of the response to make sure the request went well
    if r.status_code != 200:
        print("request denied")
        return
    else:
        print("scraping " + url)

    # convert the plaintext HTML markup into a DOM-like structure that we can search
    soup = BeautifulSoup(r.text)

    # each result is an <li> element with class="g" this is our wrapper
    results = soup.findAll("li", "g")

    # iterate over each of the result wrapper elements
    for result in results:

        # the main link is an <h3> element with class="r"
        result_anchor = result.find("h3", "r").find("a")

        # print out each link in the results
        print(result_anchor.contents)


if __name__ == "__main__":

    # you can pass in a keyword to search for when you run the script
    # be default, we'll search for the "web scraping" keyword
    try:
        keyword = sys.argv[1]
    except IndexError:
        keyword = "web scraping"

    scrape_google(keyword)
