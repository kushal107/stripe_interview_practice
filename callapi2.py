import requests

def call_api2():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    try:
        response_from_api = requests.get(url)
        response_from_api.raise_for_status

        print(response_from_api.json())

    except Exception as e:
        print(f"Error is {e}")

if __name__ == "__main__":
    call_api2()