import requests

def call_api():
    try:
        url = "https://jsonplaceholder.typicode.com/todos/1"
        response_from_api = requests.get(url)

        #check for the return code under 299
        response_from_api.raise_for_status()

        data_from_api = response_from_api.json() #parse json into python dictionary

        print(data_from_api)

    except Exception as e:
        print(f"Error is{e}")

if __name__ == "__main__":
    call_api()
