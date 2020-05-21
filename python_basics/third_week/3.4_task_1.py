# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с
# дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и
# из C в B можно перейти за один переход.
#
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

import requests
import re

start_link = [input()]
end_link = input()


def find_links(links):
    """
    :param links: принимает список сo ссылками
    :return: возвращает новые найденные ссылки
    """
    found_links = []
    for link in links:
        link = requests.get(link)  # проверяем каждую ссылку
        if link.status_code == 200:  # если страница существует, то забираем текст
            text = link.text
            found_links.extend(re.findall(r"https.+html", text))  # добавляем новые найденные ссылки
    return found_links


first_level_links = find_links(start_link)
second_level_links = find_links(first_level_links)

if end_link in second_level_links:  # проверяем, есть ли искомая ссылка в списке
    print("Yes")
else:
    print("No")
