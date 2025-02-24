import json
import os
from typing import Any

from src.base_json_saver import BaseJSONSaver


class JSONSaver(BaseJSONSaver):
    """Класс для сохранения информации о вакансиях в JSON-файл"""

    def __init__(self, file_name: str = "vacancy_file.json", path_to_file: str = "../data/") -> None:
        """Инициализация класса"""

        self.file_name: str = file_name
        self.path_to_file: str = path_to_file
        os.makedirs(self.path_to_file, exist_ok=True)

    def write_file(self, vacancy_list: list) -> None:
        """Метод для записи данных в файл"""

        full_name = self.path_to_file + self.file_name

        with open(full_name, "w", encoding="utf-8") as file:
            json.dump(vacancy_list, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, vacancies: Any) -> None:
        """Реализованный метод для добавления вакансий в файл"""

        with open(self.path_to_file + self.file_name, "a", encoding="UTF-8") as file:
            json.dump(vacancies, file)

    def delete_vacancy(self) -> None:
        """Метод для удаления информации о вакансиях"""

        with open(self.path_to_file + self.file_name, "w", encoding="utf-8") as file:
            json.dump("[]", file, indent=4, ensure_ascii=False)

    def info_vacancy(self) -> list[dict]:
        """Реализованный метод для получения данных из файла"""

        with open(self.path_to_file + self.file_name, "r", encoding="utf-8") as file:
            return json.load(file)
