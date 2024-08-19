from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_chat_completions():
    response = client.post("/chat/completions", json={"messages": [{"content": "Hello", "role": "user"}], "model": "gpt-3.5-turbo"})
    print(response)
    assert response.status_code == 200