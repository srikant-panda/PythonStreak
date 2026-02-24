import requests

def get_randomjokes(id):

    url = f'https://api.freeapi.app/api/v1/public/randomjokes/{id}'

    response = requests.get(url)
    data = response.json()

    if data['success'] and data['statusCode'] and 'data' in data:
        joke_id = data['data']['id']
        joke = data['data']['content']

        print(f'joke id : {joke_id}\n joke : {joke}')
    


if __name__ == '__main__':

        try:
             id = input("Enter a random joke id to get the joke (id <=100): ")
             get_randomjokes(id)
        except ConnectionError:
             print('Connection failed. Check your internet connection!')
        except:
             print('Unable to fetch data. Try again.')