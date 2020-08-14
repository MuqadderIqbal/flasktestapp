from random import choice

def get_random_joke(joke_category = None):
    available_joke_categories = ["general", "programming", "knock-knock"]
    random_jokes_api = "https://official-joke-api.appspot.com/jokes/{0}/random"
    if not(joke_category) or str.lower(joke_category) not in available_joke_categories:
        joke_category = choice(available_joke_categories) #"general"
    joke_url = random_jokes_api.format(joke_category)
    print("Joke URL:" , joke_url)
    joke_resp_json = requests.get(joke_url).json()[0]
    joke_type = joke_resp_json.get("type")
    joke_setup = joke_resp_json.get("setup")
    joke_punchline = joke_resp_json.get("punchline")
    return (joke_type, joke_setup, joke_punchline)