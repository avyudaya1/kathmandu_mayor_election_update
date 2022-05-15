def scrape_election():
    import requests
    from bs4 import BeautifulSoup
    import json

    URL = 'https://localelection.ekantipur.com/pradesh-3/district-kathmandu/kathmandu?lng=eng'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find("div", class_="row nominee-list-group")

    mayors = results.find("ul", class_="list-group list-group-flush")

    mayor_name = mayors.find_all("div", class_="candidate-name")
    candidate_party_name = mayors.find_all("div", class_="candidate-party-name")
    vote_numbers = mayors.find_all("div", class_="vote-numbers")
    image = mayors.find_all("div", class_="candidate-img")
    img = []

    for i in image:
        if i.img:
            img.append(i.img['src'])


    len_name = len(mayor_name)

    final = []

    for x in range(0, len_name):
        final.append({'mayor_name': mayor_name[x].text, 'candidate_party_name': candidate_party_name[x].text, 'vote_numbers': vote_numbers[x].text, 'image': img[x]})

    return final