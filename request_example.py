import requests

'''
Get all people from the Star Wars API
returns: list of people
'''
def get_people():
    people_list = []
    # Loop through all pages
    next_url = "https://swapi.dev/api/people"
    try:
        while next_url:
            # Fetch data from API
            response = requests.get(next_url)
            # Convert response to JSON
            data = response.json()
            # Get next page URL
            next_url = data['next']
            # Get list of people from JSON
            people = data['results']
            for person in people:
                # Add person to list
                people_list.append(person['name'])
    except Exception as e:
        print("Error fetching people")
    return people_list




print(get_people())