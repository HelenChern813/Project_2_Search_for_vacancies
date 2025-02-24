import json
from typing import Any


class Vacancy:
    """Класс обрабатвающий ваканссии"""

    __slots__ = ("_id", "_name", "_url", "_salary", "_employment", "_requirement")

    def __init__(self, id, name, url, salary, employment, requirement) -> None:
        """Инициализация класса"""

        self._id: int = id
        self._name: str = name
        self._url: str = url
        self._salary: int = salary
        self._employment: str = employment
        self._requirement: str = requirement

    def __str__(self) -> str:
        """Строковая информация о вакансии"""

        return f"ID: {self._id}, имя: {self._name}, адрес (url): {self._url}, з/п: {self._salary}, занятость: {self._employment}, описание: {self._requirement}"

    @staticmethod
    def __validate_salary(salary: Any) -> int:
        """Валидация вакансий по зарплате"""

        if isinstance(salary, dict):
            if "to" in salary and salary["to"] is not None:
                return salary["to"]
            elif "from" in salary and salary["from"] is not None:
                return salary["from"]
            else:
                return 0
        elif salary is None:
            return 0
        else:
            return salary

    @classmethod
    def cast_to_object_list(cls, json_obj: json) -> list:
        """Преобразование объекта JSON в объект Python"""

        object_py = []
        for i in json_obj:
            object_py.append(i)
        return object_py

    def __eq__(self, other: Any) -> Any:
        """Сравнение равенства вакансий"""

        if isinstance(other, Vacancy):
            return self.__validate_salary == other.__validate_salary
        raise TypeError

    def id(self) -> int:
        """Полуение отдельно информации про ID"""

        return self._id

    def name(self) -> str:
        """Полуение отдельно информации про название"""

        return self._name

    def url(self) -> str:
        """Полуение отдельно информации про адрес(url)"""

        return self._url

    def salary(self) -> int:
        """Полуение отдельно информации про з/п"""

        return self._salary

    def requirement(self) -> str:
        """Полуение отдельно информации про описание"""

        return self._requirement

    def employment(self) -> str:
        """Полуение отдельно информации про занятость"""

        return self._employment

    @staticmethod
    def filter_by_keywords(vacancies: list, keywords: list) -> list:
        """Фильтрует список вакансий по ключевым словам"""

        filtered_vacancies = []
        for vacancy in vacancies:
            string_for_searching = (vacancy.name + str(vacancy.requirement)).lower()
            check_status = True
            for keyword in keywords:
                if keyword.lower() not in string_for_searching:
                    check_status = False
                    break
            if check_status:
                filtered_vacancies.append(vacancy)

        return filtered_vacancies

    @staticmethod
    def get_top_salary_vacancies(vacancies: list, top_n: int) -> list:
        """Метод дл полуения топ вакансий по зарплате"""

        valid_vacancies = [vacancy for vacancy in vacancies if isinstance(vacancy, Vacancy)]
        sorted_vacancies = sorted(valid_vacancies, key=lambda x: x.salary, reverse=True)
        return sorted_vacancies[:top_n]
