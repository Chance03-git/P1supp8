import requests

def send_get_request(url):
    """
    Sends an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        tuple: A tuple containing the status code and the response text or dictionary.

    Raises:
        Exception: If the status code is in the range 400-499 (inclusive).
    """
    try:
        # Send the GET request
        response = requests.get(url)

        # Check for client error status codes (400-499)
        if 400 <= response.status_code <= 499:
            raise Exception(f"Client error: {response.status_code} - {response.reason}")

        # Handle JSON response
        if response.headers.get("Content-Type", "").startswith("application/json"):
            return response.status_code, response.json()

        # Return plain text response
        return response.status_code, response.text

    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred while sending the GET request: {e}")

def fetch_postman_token_and_ip():
    """
    Sends a GET request to https://echo.free.beeceptor.com and retrieves the 
    Postman-Token from the headers and IP address from the response body.

    Returns:
        tuple: A tuple containing the Postman-Token and the IP address.

    Raises:
        Exception: If the request fails or required keys are missing.
    """
    url = "https://echo.free.beeceptor.com"
    try:
        response = requests.get(url)

        # Check for successful response
        response.raise_for_status()

        # Extract Postman-Token from headers
        postman_token = response.headers.get("Postman-Token", "Not found")

        # Extract IP address from the response JSON
        response_data = response.json()
        ip_address = response_data.get("ip", "Not found")

        return postman_token, ip_address

    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred while sending the GET request: {e}")
    except ValueError:
        raise Exception("Failed to parse response as JSON.")
def send_post_request():
     url = "https://echo.free.beeceptor.com"
     payload = {"hello": "world"}

     try:
        # Send the POST request with JSON payload
        response = requests.post(url, json=payload)

        # Check for successful response
        response.raise_for_status()

        # Return the status code and response JSON
        return response.status_code, response.json()

     except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred while sending the POST request: {e}")
     except ValueError:
        raise Exception("Failed to parse response as JSON.")
def test_send_get_request():
    # Test with a valid URL returning JSON
    url = "https://jsonplaceholder.typicode.com/posts/1"
    status_code, response = send_get_request(url)
    assert status_code == 200
    assert isinstance(response, dict)

    # Test with a valid URL returning plain text
    url = "https://httpbin.org/html"
    status_code, response = send_get_request(url)
    assert status_code == 200
    assert isinstance(response, str)

    # Test with a client error (404)
    url = "https://jsonplaceholder.typicode.com/invalid"
    try:
        send_get_request(url)
    except Exception as e:
        assert "Client error" in str(e)
def test_fetch_postman_token_and_ip():
    postman_token, ip_address = fetch_postman_token_and_ip()

    # Assert Postman-Token and IP address are not empty
    assert postman_token != "Not found"
    assert ip_address != "Not found"

    print("Test passed: Postman-Token and IP address retrieved successfully.")
def test_send_post_request():
    status_code, response_json = send_post_request()

    # Assert the status code is 200 (OK)
    assert status_code == 200

    # Assert the response contains the sent payload
    assert response_json.get("hello") == "world"

    print("Test passed: POST request sent and response verified successfully.")
