# Web-приложение для определения тональности чата Телеграм

## Над проектом работали:

Группа 32: Смирнова А., Кожедуб Н., Багаудинов Э., Петраков В.

## ![Парсинг Телеграмм](images/te.png "Парсинг Телеграмм") Парсинг Телеграмм
Для работы с приложением необходимо выгрузить сообщения из чата Телеграм с помощью API Telegram.
 - До начала работы с  API Telegram, необходимо получить собственный API ID и Hash. 
 - Это можно сделать пройдя по ссылке [telegram.org](https://my.telegram.org/auth?to=apps)
 - Утановить  библиотеку telethon:
```python
pip install telethon
```
 - Применить [код парсинга Телеграм](https://github.com/smirnovaanastasia1234/Te/blob/main/pars_teleg.py ), который расположен в данном репозитории

## Web-приложение для определения тональности текста. 
Web-приложение разделяет сообщения выгруженные из чата Телеграмм на 3 вида:

    0: NEUTRAL
    1: POSITIVE
    2: NEGATIVE

## Streamlit app
Приложение можно найти , щелкнув по значку Streamlit

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://smirnovaanastasia1234-te-hello-tseu9h.streamlit.app/)

[Датасет](https://github.com/smirnovaanastasia1234/Te/blob/main/data.csv), используемый при демонстрации работы приложения.

## Результаты работы приложения
Несколько примеров работы приложения:

* пользователь приложения может отдельно посмотреть негативные, позитивные и нейтральные сообщения:

![Вторая страница](images/2.png "Вторая страница")

* в приложении представлен визуальный анализ сообщений: 
![Анализ](images/3.png "Анализ")

## Использованная литература
* [Ссылка на документацию streamlit](https://docs.streamlit.io/)
* [Ссылка на документацию huggingface](https://huggingface.co/blanchefort/rubert-base-cased-sentiment)
