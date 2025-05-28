# Get Lyrics (of a song) from Gaana
from requests_html import HTMLSession

session = HTMLSession()

r= session.get("https://gaana.com/lyrics/bade-achhe-lagte-hain")
try:
    r.raise_for_status()
    lyr= r.html.find(".lyr_data",first=True)
    lyrics= lyr.find("._inner",first=True)
    # print(lyrics.text)

    lyrics_ = lyrics.find("p")
    for i in lyrics_[0:4]:
        print(i.text)
    print("<3")
    
except Exception as e:
    print(f"There was a problem: {e}")
    
# print("This will always be executed")