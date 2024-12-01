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