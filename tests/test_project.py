def test_landing(client):
    response = client.get("/")
    assert b"<h1> Landing Page </h1>" in response.data
    assert b"<title> Align </title>" in response.data