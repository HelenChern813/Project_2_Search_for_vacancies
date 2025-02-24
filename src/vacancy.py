from typing import Any


class Vacancy:
    """Класс обрабатвающий ваканссии"""

    id: int
    name: str
    url: str
    salary: int
    employment: str
    requirement: str

    __slots__ = ("id", "name", "url", "salary", "employment", "requirement")

    def __init__(self, data: dict) -> None:
        """Инициализация класса"""

        for attr in self.__slots__:
            if attr in data:
                setattr(self, attr, data[attr])
        self.salary = self.__validate_salary(self.salary)
        self.requirement = data["snippet"]["requirement"]

    def __str__(self) -> str:
        """Строковая информация о вакансии"""

        return f"ID: {self.id}, имя: {self.name}, адрес (url): {self.url}, з/п: {self.salary}, занятость: {self.employment}, описание: {self.requirement}"

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

    def __lt__(self, other: Any) -> Any:
        """Сравнение зарплаты"""

        if isinstance(other, Vacancy):
            return self.salary < other.salary
        raise TypeError

    def __eq__(self, other: Any) -> Any:
        """Сравнение равенства вакансий"""

        if isinstance(other, Vacancy):
            return self.__validate_salary == other.__validate_salary
        raise TypeError

    def attributes(self) -> dict:
        """ Метод для получения атрибутов, указанных в __slots__ """
        return {attr: getattr(self, attr) for attr in self.__slots__ if hasattr(self, attr)}

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
        """Метод для полуения топ вакансий по зарплате"""

        valid_vacancies = [vacancy for vacancy in vacancies if isinstance(vacancy, Vacancy)]
        sorted_vacancies = sorted(valid_vacancies, key=lambda x: x.salary, reverse=True)
        return sorted_vacancies[:top_n]
