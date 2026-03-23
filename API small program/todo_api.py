import requests
import tabulate

def create_todo(title, description):
    url = 'https://api.freeapi.app/api/v1/todos/'

    request_body = {
        'description': description,
        'title': title
    }
    response = requests.post(url, request_body)
    data = response.json()
    if data['success'] and 'data' in data:
        print(data['message'])
        print(tabulate.tabulate([data['data']], headers='keys', tablefmt='fancy_grid'))

    else:
        print('Something went wrong. Try again.', data['statusCode'])
        # print('Error details:', data)
        # print('Request body:', request_body)
    

if __name__ == '__main__' : 
    try:
        title = input('Enter the title of your todo(required): ')
        description = input("Enter the description about your todo(required): ")
        create_todo(title, description)
    except ConnectionError:
        print('Connection failed. Check your internet connection!')
    except Exception as e:
        print('Unable to fetch data. Try again.')