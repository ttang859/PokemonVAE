import requests
from tqdm import tqdm

# scrape types from internet
def getType(name):
    path = f"https://pokeapi.co/api/v2/pokemon/{name}"
    try:
        response = requests.get(path)
        response.raise_for_status()  # Raise exception for 4XX and 5XX status codes
        types = response.json()['types']
        if len(types) == 1:
            t1 = types[0]['type']['name']
            return t1, t1
        return types[0]['type']['name'], types[1]['type']['name']
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 'N/A', 'N/A'
    
type1 = []
type2 = []
for i in tqdm(name):
    i = i.lower()
    print(i)
    t1,t2 = getType(i)
    type1.append(t1)
    type2.append(t2)