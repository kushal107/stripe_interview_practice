import requests

def call_api2():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    try:
        response_from_api = requests.get(url)
        response_from_api.raise_for_status()

        print(response_from_api.json())

    #print all the functions we can call from this variable
        print(dir(response_from_api))

    except Exception as e:
        print(f"Error is {e}")

if __name__ == "__main__":
    call_api2()
    #this is a comment