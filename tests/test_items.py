import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app

# Use in-memory SQLite for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_headers(client):
    client.post("/users/", json={"username": "testuser", "password": "testpassword123"})
    response = client.post("/token", data={"username": "testuser", "password": "testpassword123"})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_create_item(client, auth_headers):
    response = client.post("/items/", json={"name": "Test Item", "price": 10.5}, headers=auth_headers)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert "id" in data

def test_create_item_invalid(client, auth_headers):
    response = client.post("/items/", json={"name": "Invalid"}, headers=auth_headers)
    assert response.status_code == 422

def test_list_items(client, auth_headers):
    response = client.get("/items/", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_item(client, auth_headers):
    # Create item first
    create_resp = client.post("/items/", json={"name": "Get Me", "price": 5.0}, headers=auth_headers)
    item_id = create_resp.json()["id"]
    
    response = client.get(f"/items/{item_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["name"] == "Get Me"

def test_get_item_not_found(client, auth_headers):
    response = client.get("/items/9999", headers=auth_headers)
    assert response.status_code == 404

def test_update_item(client, auth_headers):
    # Create item first
    create_resp = client.post("/items/", json={"name": "Update Me", "price": 5.0}, headers=auth_headers)
    item_id = create_resp.json()["id"]
    
    response = client.patch(f"/items/{item_id}", json={"price": 15.0}, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["price"] == 15.0

def test_update_item_not_found(client, auth_headers):
    response = client.patch("/items/9999", json={"price": 15.0}, headers=auth_headers)
    assert response.status_code == 404

def test_delete_item(client, auth_headers):
    # Create item first
    create_resp = client.post("/items/", json={"name": "Delete Me", "price": 5.0}, headers=auth_headers)
    item_id = create_resp.json()["id"]
    
    response = client.delete(f"/items/{item_id}", headers=auth_headers)
    assert response.status_code == 200
    
    # Verify deletion
    get_resp = client.get(f"/items/{item_id}", headers=auth_headers)
    assert get_resp.status_code == 404

def test_delete_item_not_found(client, auth_headers):
    response = client.delete("/items/9999", headers=auth_headers)
    assert response.status_code == 404
