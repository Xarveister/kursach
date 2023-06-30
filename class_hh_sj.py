from abc import ABC, abstractmethod
import requests


# создание абстрактного класса
class API(ABC):
    @abstractmethod
    def get_request(self):
        """Метод для загрузки файла JSON """
        pass

    @abstractmethod
    def get_vacancies(self):
        """Метод для получения вакансий """
        pass


class HeadHunter(API):
    """ Класс для подключения к API hh.ru"""
    url = "https://api.hh.ru/vacancies"

    def __init__(self, keyword):
        self.params = {
            "per_page": 100,
            "page": None,
            "text": keyword,
            "archived": False
        }

        self.headers = {
            "User-Agent": "My_programm"
        }

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    def get_request(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        return response.json()["items"]

    def get_vacancies(self, pages_count=2):
        self.vacancies = []
        for page in range(pages_count):
            page_vacancies = []
            self.params["page"] = page
            page_vacancies = self.get_request()
            self.vacancies.extend(page_vacancies)
            print(f"Загружено вакансий: {len(page_vacancies)}")

    def get_formatted_vacancies(self):
        """Метод для получения форматированной вакансии"""
        formatted_vacancies = []
        for obj in self.vacancies:
            formatted_vacancy = {
                "employer": obj["employer"]["name"],
                "title": obj["name"],
                "url": obj["alternate_url"],
                "api": "HeadHunter",
            }
            salary = obj["salary"]
            if salary:
                formatted_vacancy["salary_from"] = salary["from"]
                formatted_vacancy["salary_to"] = salary["to"]
                formatted_vacancy["currency"] = salary["currency"]
            else:
                formatted_vacancy["salary_from"] = None
                formatted_vacancy["salary_to"] = None
                formatted_vacancy["currency"] = None
                formatted_vacancy["currency_value"] = None
            formatted_vacancies.append(formatted_vacancy)

        return formatted_vacancies


class SuperJob(API):
    """ Класс для подключения к API superjob.ru"""
    url = "https://api.superjob.ru/2.0/vacancies"

    def __init__(self, keyword):
        self.params = {
            "count": 100,
            "page": None,
            "keyword": keyword,
            "archived": False
        }
        self.headers = {"Host": "api.superjob.ru",
                        "X-Api-App-Id": "v3.r.14797195.b8900603b5b2879d3bf3b698f1255351ad5aa88a.3eba69026fe9e2cfd4ffa5d1eaabe41bd0388603",
                        "Authorization": "Bearer r.000000010000001.example.access_token",
                        "Content-Type": "application/x-www-form-urlencoded"}

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    def get_request(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        return response.json()["objects"]

    def get_vacancies(self, pages_count=2):
        self.vacancies = []
        for page in range(pages_count):
            page_vacancies = []
            self.params["page"] = page
            page_vacancies = self.get_request()
            self.vacancies.extend(page_vacancies)
            print(f"Загружено вакансий: {len(page_vacancies)}")

    def get_formatted_vacancies(self):
        """Метод для получения форматированной вакансии"""
        formatted_vacancies = []
        sj_currencies = {
            "rub": "RUR",
            "uah": "UAH",
            "uzs": "UZS"
        }
        for obj in self.vacancies:
            formatted_vacancy = {
                "employer": obj["firm_name"],
                "title": obj["profession"],
                "url": obj["link"],
                "api": "SuperJob",
                "salary_from": obj["payment_from"] if obj["payment_from"] and obj["payment_from"] != 0 else None,
                "salary_to": obj["payment_to"] if obj["payment_to"] and obj["payment_to"] != 0 else None,
            }
            if obj["currency"] in sj_currencies:
                formatted_vacancy["currency"] = sj_currencies[obj["currency"]]
            elif obj["currency"]:
                formatted_vacancy["currency"] = "RUR"
            else:
                formatted_vacancy["currency"] = None
            formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies
