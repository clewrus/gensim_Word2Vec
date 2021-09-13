# Векторна семантика
Виробнича практика в університеті

## Вимоги
+ Python

## Встановлення
1. Створити віртуальне середовище
    ```sh
    virtualenv -p python3 .
    source ./bin/activate
    ```
2. Склонувати проект
    ```sh
    git clone https://github.com/clewrus/gensim_Word2Vec.git
    ```
3. Вcтановити залежності
    ```sh
    pip install -r requirements.txt
    ```
4. Створити папку **dataset** на одному рівні з кореневою папкою проекту та завнатжити в неї текстовий файл з датасетом. Датаcети можна завантажити з сайту за [посиланням](https://lang.org.ua/uk/corpora/).
5. Для редагування та виконання потрібен jupyter notebook
    ```sh
    pip install jupyterlab
    jupyter notebook
    ```


## Використання
1. Виконати код файлу **create_embeddings.ipynb**. В результаті буде створено модель та записано її до файлу **500mb_wiki.model**.

2. Виконати файл **find_close.py** передавши до аргументів назву файлу з моделлю та ключове слово.
    ```sh
    python find_close.py "model_name" "word_to_test"
    ```
