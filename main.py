from class_hh_sj import HeadHunter, SuperJob
from JSONSaver import JSONSaver


# основная функция
def main():
    print("Выберите сайт для поиска вакансий")
    command = input(
        "1 - HeadHunter;\n"
        "2 - SuperJob;\n"
        "exit - для выхода.\n"
        ">>> "
    )
    if command.lower == "exit":
        return
    elif command == "1":
        vacancies_json = []
        keyword = input('Введите профессию для поиска:')
        hh = HeadHunter(keyword)
        hh.get_request()
        hh.get_vacancies(pages_count=5)
        vacancies_json.extend(hh.get_formatted_vacancies())
        job = JSONSaver(keyword=keyword, vacancies_json=vacancies_json)
        while True:
            command = input(
                "1 - Вывеси список вакансий;\n"
                "2 - Отсортировать по зарплате;\n"
                "exit - для выхода.\n"
                ">>> "
            )
            if command.lower == "exit":
                return
            elif command == "1":
                vacancies = job.select()
            elif command == "2":
                vacancies = job.sort_by_salary_from()
            elif command.lower == "exit":
                return
            for vacancy in vacancies:
                print(vacancy, end='\n')

    elif command == "2":
        vacancies_json = []
        keyword = input('Введите профессию для поиска:')
        sj = SuperJob(keyword)
        sj.get_request()
        sj.get_vacancies(pages_count=5)
        vacancies_json.extend(sj.get_formatted_vacancies())
        job = JSONSaver(keyword=keyword, vacancies_json=vacancies_json)
        while True:
            command = input(
                "1 - Вывеси список вакансий;\n"
                "2 - Отсортировать по зарплате;\n"
                "exit - для выхода.\n"
                ">>> "
            )
            if command.lower == "exit":
                break
            elif command == "1":
                vacancies = job.select()
            elif command == "2":
                vacancies = job.sort_by_salary_from()
            elif command.lower == "exit":
                return
            for vacancy in vacancies:
                print(vacancy, end='\n')


if __name__ == "__main__":
    main()
