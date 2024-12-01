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