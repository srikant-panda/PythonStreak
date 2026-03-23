import requests    #imports the request module which can send http request to application


def get_a_meal(url):

    meal = requests.get(url)
    response = meal.json()
    print(response['data']['data'][0]['strMeal'])

if __name__ == "__main__":
    url = 'https://api.freeapi.app/api/v1/public/meals?page=1&limit=10&query=rice'
    get_a_meal(url)