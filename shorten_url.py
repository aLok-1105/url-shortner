
import requests

def shorten_url(url_to_shorten):
    base_url = "http://127.0.0.1:5000/shorten"  # Replace with the actual URL of your URL shortener
    data = {'url': url_to_shorten}

    try:
        response = requests.post(base_url, data=data)
        if response.status_code == 200:
            print("Shortened URL:", response.text)
        else:
            print("Error:", response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

url = input("Enter the URL: ")

url_to_shorten = url
shorten_url(url_to_shorten)