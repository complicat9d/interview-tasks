import httpx
from typing import Dict
from bs4 import BeautifulSoup, Tag
import csv

from utils.log import logger


URL = "https://ru.wikipedia.org"


def get_next_page(page: Tag) -> str | None:
    next_page = page.find_all(name="a", title="Категория:Животные по алфавиту")[-1]
    link_next_page = (
        next_page["href"] if next_page.text == "Следующая страница" else None
    )
    return link_next_page


def parser(url: str) -> Dict[str, int]:
    result = {}

    while True:
        with httpx.Client() as client:
            response = client.get(url)
        print(response.text)
        soup = BeautifulSoup(markup=response.text, features="html.parser")
        page = soup.find(name="div", id="mw-pages")

        next_page = get_next_page(page)
        if next_page is None:
            break

        symbol_group = page.find(name="div", class_="mw-category-columns").find_all(
            name="div", class_="mw-category-group"
        )

        for item in symbol_group:
            symbol = item.h3.text
            count_animals = len(item.find_next(name="ul"))

            if symbol not in result:
                result[symbol] = 0
                logger.info(f"Обрабатываются названия на букву - {symbol}")
            result[symbol] += count_animals

        url = f"{URL}{next_page}"

    return result


def write_to_file(obj: Dict[str, int]) -> None:
    with open("beasts.csv", mode="w") as file:
        writer = csv.writer(file, delimiter=",")

        for symbol, count in obj.items():
            writer.writerow([symbol, count])


if __name__ == "__main__":
    result = parser("https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту")
    write_to_file(result)
