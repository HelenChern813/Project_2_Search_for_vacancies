from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для работы с API Хедхантера"""

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list:
        """Метод для полуения списка вакансий в формате JSON"""

        pass
