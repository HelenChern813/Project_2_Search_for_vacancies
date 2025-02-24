from src.vacancy import Vacancy


def test_vacancy_str(vacancy):
    expected_str = "ID: 100, имя: Python Developer, адрес (url): http://Python_top.com, з/п: 30000, занятость: Полная занятость, описание: Experience with Python"
    assert str(vacancy) == expected_str


def test_vacancy_lt(vacancy):
    other_vacancy = Vacancy({"id": 200, "name": "Java Developer", "url": "http://Java_notop.com", "salary": 400, "snippet": {"requirement": "Experience with Java"}})
    assert vacancy > other_vacancy


def test_vacancy_filter_by_keywords():
    vacancies = [
        Vacancy({"id": 101, "name": "Python Developer", "url": "http://pythonn.com", "salary": 300000, "snippet": {"requirement": "Experience with Python"}}),
        Vacancy({"id": 202, "name": "Java Developer", "url": "http://example.com", "salary": 150000, "snippet": {"requirement": "Experience with Java"}})
    ]
    filtered_vacancies = Vacancy.filter_by_keywords(vacancies, ["Python"])
    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0].id == 101


def test_vacancy_get_top_salary_vacancies():
    vacancies = [
        Vacancy({"id": 103, "name": "Python Developer", "url": "http://example.com", "salary": 2000, "snippet": {"requirement": "Experience with Python"}}),
        Vacancy({"id": 204, "name": "Java Developer", "url": "http://example.com", "salary": 1500, "snippet": {"requirement": "Experience with Java"}}),
        Vacancy({"id": 305, "name": "JavaScript Developer", "url": "http://example.com", "salary": 2500, "snippet": {"requirement": "Experience with JavaScript"}})
    ]
    top_vacancies = Vacancy.get_top_salary_vacancies(vacancies, 2)
    assert len(top_vacancies) == 2
    assert top_vacancies[0].id == 305
    assert top_vacancies[1].id == 103
