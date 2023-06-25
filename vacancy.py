class Vacancy:
    def __init__(self, vacancy):
        self.employer = vacancy["employer"]
        self.title = vacancy["title"]
        self.url = vacancy["url"]
        self.api = vacancy["api"]
        self.salary_from = vacancy["salary_from"]
        self.salary_to = vacancy["salary_to"]
        self.currency = vacancy["currency"]

    def __str__(self):
        if not self.salary_from and not self.salary_to:
            salary = "Не указана"
        else:
            salary_from, salary_to = "", ""
            if self.salary_from:
                salary_from = f"от {self.salary_from}  {self.currency}"
                if self.currency != "RUR":
                    salary_from += f"({round(self.salary_from * 1, 2)} RUR)"

            if self.salary_to:
                salary_to = f"от {self.salary_to}  {self.currency}"
                if self.currency != "RUR":
                    salary_to += f"({round(self.salary_to * 1, 2)} RUR)"
            salary = " ".join([salary_from, salary_to]).strip()
        return f"""
Работодатель: \"{self.employer}\"
Вакансия: \"{self.title}\"
Зарплата: {salary}
Ссылка: {self.url}
        """
