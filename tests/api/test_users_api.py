def test_get_posts(api_base_url, http_client):
    r = http_client.get(f"{api_base_url}/posts")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 1