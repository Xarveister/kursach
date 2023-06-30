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
                salary_to = f"до {self.salary_to}  {self.currency}"
                if self.currency != "RUR":
                    salary_to += f"({round(self.salary_to * 1, 2)} RUR)"
            salary = " ".join([salary_from, salary_to]).strip()
        return f"""
Работодатель: \"{self.employer}\"
Вакансия: \"{self.title}\"
Зарплата: {salary}
Ссылка: {self.url}
        """

    def __lt__(self, other):
        salary_to_self = self.salary_to if self.salary_to else 0
        salary_from_self = self.salary_from if self.salary_from else 0

        salary_to_other = other.salary_to if other.salary_to else 0
        salary_from_other = other.salary_from if other.salary_from else 0
        return (salary_to_self, salary_from_self) < (salary_to_other, salary_from_other)
    def __gt__(self, other):
        salary_to_self = self.salary_to if self.salary_to else 0
        salary_from_self = self.salary_from if self.salary_from else 0

        salary_to_other = other.salary_to if other.salary_to else 0
        salary_from_other = other.salary_from if other.salary_from else 0
        return (salary_to_self, salary_from_self) > (salary_to_other, salary_from_other)