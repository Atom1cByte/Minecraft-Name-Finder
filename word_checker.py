import bs4
import requests

def verify_word(word):
    resp = requests.get("https://www.merriam-webster.com/dictionary/"+word)
    soup = bs4.BeautifulSoup(resp.text, "html.parser")
    valid_specific = soup.select("h2>em")
    if len(valid_specific) == 0 or "abbreviation" in resp.text:
        return False
    else:
        return True

print(verify_word("gawad"))