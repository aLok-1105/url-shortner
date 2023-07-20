# URL Shortener App

## Introduction: 

This project consists of two Python files, `app.py` and `shorten_url.py`, which together implement a URL shortener. The URL shortener takes a long URL as input and returns a shortened version of it. The purpose of this readme file is to provide an overview of the project, its requirements, instructions on how to use it, how it works, an important note, a disclaimer, and a conclusion.

## Requirements: 

To use this URL shortener, you need the following:

1. Python installed on your system (version 3.x recommended).
2. The `flask` library, which can be installed using the following command:
   ```
   pip install flask
   ```

## How to Use: 

1. Ensure you have met the requirements mentioned above.
2. Download both `app.py` and `shorten_url.py` files.
3. Start the server for the URL shortener. The actual server address should replace `"http://127.0.0.1:5000/shorten"` in both files. For the purpose of this readme, let's assume the server is running at `"http://your-url-shortener.com/shorten"`.
4. Open a terminal or command prompt and navigate to the directory where the files are located.
5. Run the `app.py` script by executing the following command:
   ```
   python app.py
   ```
6. Run the `shorten_url.py` script by executing the following command:
   ```
   python shorten_url.py
   ```
6. The script will prompt you to enter the URL you want to shorten.
7. Type or paste the URL and press Enter.
8. The script will make a request to the URL shortener server, and if successful, it will display the shortened URL.

## How It Works: 

1. The `shorten_url` function in both `app.py` and `shorten_url.py` sends a POST request to the specified URL shortener server with the URL to be shortened.
2. The server processes the request and generates a unique shortened URL for the provided long URL.
3. If the server responds with a status code of 200, the script displays the shortened URL on the console.
4. If there is an error (e.g., the server is not reachable or returns an error status code), the script displays an error message.

## Important Note: 

- Please ensure that the URL shortener server is operational and accessible at the specified address before using the script.

## Disclaimer: 

- This URL shortener is a simple example and may not provide all the features or security measures required in a production-ready application.
- The usage and implementation of the server-side URL shortener are beyond the scope of this readme.

## Conclusion: 

This URL shortener project provides a basic implementation of shortening long URLs using a server-based URL shortening service. By following the instructions provided in the "How to Use" section, users can take advantage of the URL shortener to create shortened versions of long URLs for sharing and distribution. Remember to exercise caution and ensure the server is reliable and secure if you are considering using this in a production environment. Feel free to modify and enhance the code to suit your specific needs. Happy URL shortening!