import pytest
import requests

def test_get_user():
    # Проверка GET-запроса на получение данных пользователя
    response = requests.get(f"https://reqres.in/api/users/1")

    # Проверяем статус-код
    assert response.status_code == 200

    # Проверяем структуру и значения JSON
    data = response.json()
    assert data["data"]["id"] == 1
    assert isinstance(data["data"]["email"], str)


def test_create_user():
    # Проверка POST-запроса на создание нового пользователя
    payload = {"name": "Максим", "age": 21, "job": "Junior QA Engineer"}
    response = requests.post(f"https://reqres.in/api/users", json=payload)

    # API возвращает 201 Created
    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Максим"
    assert "id" in data
    assert "createdAt" in data


def test_update_user():
    # Проверка PUT-запрос на обновление данных пользователя
    payload = {"name": "Максим", "age": 30, "job": "QA Lead"}
    response = requests.put(f"https://reqres.in/api/users/1", json=payload)

    # Проверяем статус-код
    assert response.status_code == 200

    data = response.json()
    assert data["job"] == "QA Lead"
    assert "updatedAt" in data