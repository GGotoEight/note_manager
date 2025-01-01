# Creating variables
titles = []
username = input("Введите имя пользователя: ")
title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания в формате \"ДД-ММ-ГГГГ\": ")
issue_date = input("Введите дату истечения заметки (дедлайн) в формате \"ДД-ММ-ГГГГ\": ")

# Add all titles in list
titles.extend((title1, title2, title3))

# Print variables
print("Имя пользователя:", username)
print("Заголовки:", *titles)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания:", created_date)
print("Дата истечения заметки (дедлайн):", issue_date, end='')