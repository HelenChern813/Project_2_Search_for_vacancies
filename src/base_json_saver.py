from abc import ABC, abstractmethod
from typing import Any


class BaseJSONSaver(ABC):
    """Абстрактный класс для классов реализующих сохранение и использование вакансий в файлах"""

    @abstractmethod
    def add_vacancy(self, vacancies: Any) -> None:
        """Метод для добавления вакансий в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self) -> None:
        """Метод для удаления информации о вакансиях"""
        pass

    @abstractmethod
    def info_vacancy(self) -> list[dict]:
        """Метод для получения данных из файла"""
        pass
