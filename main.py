from src.interaction_hh import HeadHunterAPI
from src.vacancy import Vacancy
from src.json_saver import JSONSaver


def user_interaction():
    '''Функция для взаимодействия с пользователем'''

    print("Рады приветствовать Вас в поиске вакансий на HeadHunter!")

    # Запрос у пользователя
    search_query = input("Введите поисковый запрос для запроса вакансий: ")

    # Загрузка вакансий
    vacancies_HH = HeadHunterAPI()
    vacancies_HH = vacancies_HH.get_vacancies(search_query)

    # Создание списка экземпляров класса Vacancy
    vacancies = [Vacancy(vacancy_data) for vacancy_data in vacancies_HH]

    while True:
        print("\nВыберите действие:")
        print("1. Получить топ N вакансий по зарплате")
        print("2. Получить вакансии с ключевым словом в описании")
        print("3. Сохранить вакансии в файл")
        print("4. Выйти")

        client = input("Введите номер желаемого действия: ")

        if client == "1":
            # Запрос количества вакансий для отображения в топе по зарплате
            top_n = int(input("Введите количество вакансий для отображения в топе по зарплате: "))
            top_vacancies = Vacancy.get_top_salary_vacancies(vacancies, top_n)
            for vacancy in top_vacancies:
                print(vacancy)

        elif client == "2":
            # Запрос ключевого слова для фильтрации вакансий по описанию
            keyword = input("Введите ключевое слово для фильтрации вакансий по описанию: ")
            filtered_vacancies = Vacancy.filter_by_keywords(vacancies, [keyword])

            return filtered_vacancies

        elif client == "3":
            # Сохранение вакансий в файл
            vacancies_dicts = [vacancy.attributes() for vacancy in vacancies]
            jn_file = JSONSaver()
            jn_file.write_file(vacancies_dicts)
            return print('Вакансии успешно сохранены в файл.')

        elif client == "4":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    user_interaction()
