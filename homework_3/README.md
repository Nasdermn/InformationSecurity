# ДЗ № 3

Перед выполнением заданий при скачивании репозитория убедитесь, что у вас на компьютере есть Python 3.11, а также путь к нему в переменной среды Path. После этого, находясь в репозитории homework_3, выполните следующие команды:

```
py -m venv venv
```

```
venv/Scripts/activate
```

```
pip install -r requirements.txt
```

```
pip install dlib.whl
```

#### Задание 1

Для проверки первого задания укажите проверяемое фото в переменной analysing_img в файле biometry.py и запустите программу следующей командой, находясь в папке homework_3:

```
py ./biometry.py
```

#### Задание 2

Для проверки второго задания сделайте следующие действия:

1. Укажите проверяемое фото в переменной analysing_img в файле scanface.py
2. Добавьте фотографии шаблонов, на основе которых будет вестись обучение, в папку templates
3. Запустите программу следующей командой, находясь в папке homework_3:

```
py ./scanface.py
```