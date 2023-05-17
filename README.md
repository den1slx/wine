# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Установите зависимости командой:
```commandline
pip install -r requirements.txt
```

- Получите подсказку командой:
```commandline
python main.py -h
```
- Файл `example.xlsx` Используется по умолчанию. Скопируйте его и заполните своими данными.
Пример таблицы:

| Категория    | Название            | Сорт            | Картинка                 | Акция                | Цена |
|--------------|---------------------|-----------------|--------------------------|----------------------|------|
| Белые вина   | Белая леди          | Дамский пальчик | belaya_ledi.png          | Выгодное предложение | 399  |
| Белые вина   | Кокур               | Кокур           | kokur.png                |                      | 450  |
| Напитки      | Коньяк классический |                 | konyak_klassicheskyi.png |                      | 350  |
| Красные вина | Черный лекарь       | Качич           | chernyi_lekar.png        |                      | 399  |

- Запустите сайт командой: 
```commandline
python main.py
```
или
```commandline
python main.py -p example.xlsx -ip images\
```

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).


