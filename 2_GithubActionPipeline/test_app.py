from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Hello, Its Noizy aka Kushal - Take1 for Gihub Actions" in response.data
