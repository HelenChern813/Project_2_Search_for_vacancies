import pytest

from src.vacancy import Vacancy


@pytest.fixture
def request_get():
    return {"items": [{"id": "59784231", "name": "Разработчик Python"}]}


@pytest.fixture
def load_vacancies_result():
    return [{"id": "59784231", "name": "Разработчик Python"}]


@pytest.fixture
def vacancy_data():
    return {
        "id": 100,
        "name": "Python Developer",
        "url": "http://Python_top.com",
        "salary": {"from": 5000, "to": 30000},
        "employment": 'Полная занятость',
        "snippet": {"requirement": "Experience with Python"}
    }


@pytest.fixture
def vacancy(vacancy_data):
    return Vacancy(vacancy_data)
