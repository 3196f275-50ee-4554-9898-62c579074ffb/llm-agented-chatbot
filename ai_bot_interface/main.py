from gpt4free import G4FLLM
from langchain.llms.base import LLM
from g4f import Provider, models
import mysql.connector
from mysql.connector import Error
import time

def ProcessTextDB(text, id=1):
    llm: LLM = G4FLLM(
        model=models.gpt_35_turbo,
        provider=Provider.Yqcloud,
    )

    print(f"Processing text: {text}")
    MSG = f"""
        Answer as an analyst would answer. Always answer in Russian Language. My message for you: {text}. If you need, you can write HTML code with tailwind for difficult view or bootstrap for usual basics css styles, this code will be rendered for me. Do not use Markdown, LATeX, use only html and text. Always answer using HTML code. you will communicate with the employees of the construction company and you should be a useful assistant.
    """

    if text == "message_loyality":
        MSG = f"""
            Answer as an analyst would answer. Always answer in Russian Language. Придумай стратегию программы лояльности по привлечению клиентов туристического приложения. Базовая информация о приложении: Вы также можете узнать актуальную информацию о мероприятиях, сможете подобрать и забронировать экскурсии. А если вы предпочитаете прогулки, в нашем приложении есть пешие маршруты по городу и его окрестностям. Вы сможете исследовать достопримечательности Анапы любым удобным вам способом, будь то на автомобиле, пешком или на велосипеде. При ответе используй HTML таблицу..
        """

    if text == "Расчитай ":

        PROMPT = "Answer as an analyst would answer. Always answer in Russian Language. If you need, you can write HTML code with tailwind for difficult view or bootstrap for usual basics css styles, this code will be rendered for me. Do not use Markdown, LATeX, use only html and text. Always answer using HTML code."

        listOfReq = [
            f"{PROMPT} Создай таблицу HTML которая будет содержать 20 идей для программы лояльности и включать: номер, название, предпологаемая степень конверсии",
            f'{PROMPT} Создай список HTML из возможных кризисов для программы лояльности клиентам турристического приложения в России, Сочи. Под каждым пунктом списка добавь кнопку с белым текстом и черным фоном с данписью: Добавить в базу. У этой кнопки должен быть аргумент wire:click="$set("text", "ТУТ ДОЛЖЕН БЫТЬ ТЕКСТ ИЗ СПИСКА НАД КНОПКОЙ")"',
            f'{PROMPT} Создай график показывающий динамику востребованности туризма в Сочи, Россия используя примитивы div и style. ',
        ]

        connection = mysql.connector.connect(host="localhost",
                                             database='laravel',
                                             user='sail',
                                             password='password')
        if connection.is_connected():
            for req in listOfReq:
                cursor = connection.cursor()
                insert_query = ("INSERT INTO message_jobs (message_id, request) "
                                "VALUES (%s, %s)")
                cursor.execute(insert_query, (id, req))
                connection.commit()


        table_res = llm("Answer as an analyst would answer. Always answer in Russian Language. If you need, you can write HTML code with tailwind for difficult view or bootstrap for usual basics css styles, this code will be rendered for me. Do not use Markdown, LATeX, use only html and text. Always answer using HTML code. Создай таблицу HTML которая будет содержать 20 идей для программы лояльности и включать: номер, название, предпологаемая степень конверсии")
        status = llm('Answer as an analyst would answer. Always answer in Russian Language. If you need, you can write HTML code with tailwind for difficult view or bootstrap for usual basics css styles, this code will be rendered for me. Do not use Markdown, LATeX, use only html and text. Always answer using HTML code. Создай список HTML из возможных кризисов для программы лояльности клиентам турристического приложения в России, Сочи. Под каждым пунктом списка добавь кнопку с белым текстом и черным фоном с данписью: Добавить в базу. У этой кнопки должен быть аргумент wire:click="$set("text", "ТУТ ДОЛЖЕН БЫТЬ ТЕКСТ ИЗ СПИСКА НАД КНОПКОЙ")"')

        # res = llm(MSG)
        table_res = table_res.replace("```html", "").replace("```", "")
        status = status.replace("```html", "").replace("```", "")
        res = f"""
            <div class="flex space-x-4 w-full">
            <div class="w-2/3 p-4 rounded-2xl bg-gray-200 hover:bg-gray-300 text-black ring-1 ring-gray-500">
                {table_res}
            </div>
            <div class="w-full p-4 rounded-2xl bg-gray-200 hover:bg-gray-300 text-black ring-1 ring-gray-500">
                {status}
            </div>
            </div>
        """
        print(res)
        return res

    res = llm(MSG)
    res = """
    Понял, спасибо за пояснение.

Составление сметы строительного проекта включает в себя несколько ключевых этапов, которые помогают обеспечить точность и полноту оценки затрат. Рассмотрим основные шаги:

1. **Определение объема работ**
    Первым шагом является детальное определение объема работ, которые необходимо выполнить. Это включает в себя анализ проектной документации, чертежей и спецификаций.

2. **Составление списка материалов и оборудования**
    На основании проектной документации составляется перечень всех необходимых материалов и оборудования. Важно учитывать качество, количество и стоимость каждого элемента.

3. **Расчет трудозатрат**
    Необходимо оценить количество рабочих часов, необходимых для выполнения каждого этапа строительства, и определить стоимость труда.

4. **Учет накладных расходов**
    Включите в смету все накладные расходы, такие как аренда техники, транспортные расходы, страхование и административные затраты.

5. **Оценка непредвиденных затрат**
    Рекомендуется включить резервный фонд для покрытия непредвиденных затрат, которые могут возникнуть в процессе строительства.

6. **Анализ и проверка сметы**
    После составления сметы необходимо провести тщательную проверку всех расчетов и при необходимости скорректировать данные. Это может включать внутренние аудиты или консультации с экспертами.

Следуя этим шагам, вы сможете составить точную и полную смету строительного проекта, что позволит избежать перерасхода средств и задержек в ходе выполнения работ.

Теперь представлю график этапов в виде HTML кода:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Этапы составления сметы</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-4">
        <h1 class="mb-4">Этапы составления сметы строительного проекта</h1>
        <ol class="list-group">
            <li class="list-group-item">
                <h5>Определение объема работ</h5>
                <p>Анализ проектной документации, чертежей и спецификаций.</p>
            </li>
            <li class="list-group-item">
                <h5>Составление списка материалов и оборудования</h5>
                <p>Составление перечня всех необходимых материалов и оборудования.</p>
            </li>
            <li class="list-group-item">
                <h5>Расчет трудозатрат</h5>
                <p>Оценка количества рабочих часов и стоимости труда.</p>
            </li>
            <li class="list-group-item">
                <h5>Учет накладных расходов</h5>
                <p>Включение накладных расходов, таких как аренда техники и транспортные расходы.</p>
            </li>
            <li class="list-group-item">
                <h5>Оценка непредвиденных затрат</h5>
                <p>Включение резервного фонда для непредвиденных затрат.</p>
            </li>
            <li class="list-group-item">
                <h5>Анализ и проверка сметы</h5>
                <p>Проверка всех расчетов и корректировка данных.</p>
            </li>
        </ol>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
    """
    return res



def chatName(text):
    MSG = f"""
        Write short name for chat where message is: {text}
    """
    llm: LLM = G4FLLM(
        model=models.gpt_35_turbo,
        # provider=Provider.Aichat,
    )
    res = llm(MSG)
    res = res.replace("```html", "").replace("```", "")
    print(res)
    return res

def getDBData():
    try:
        # Establish a database connection
        connection = mysql.connector.connect(host='localhost',
                                             database='laravel',
                                             user='sail',
                                             password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            print("Connected to MySQL database")  # Добавлено для логирования

            # Select the first item with is_processed=False and is_sended=False
            query = ("SELECT id, chat_id, text FROM messages "
                     "WHERE is_done = False AND is_send_to_processing = False "
                     "LIMIT 1")
            cursor.execute(query)

            # Fetch one record
            record = cursor.fetchone()
            print(f"Fetched record: {record}")

            if record:
                id, chat_id, text = record

                # Update is_sended to True for the fetched record
                update_query = ("UPDATE messages SET is_send_to_processing = True "
                                "WHERE text = %s")
                cursor.execute(update_query, (text,))
                connection.commit()

                # Call the ProcessTextDB function
                answer = ProcessTextDB(text, id)

                # Update is_processed to True for the fetched record
                update_query = ("UPDATE messages SET is_done = True "
                                "WHERE text = %s")
                cursor.execute(update_query, (text,))
                connection.commit()

                # Create a new message with the answer and actor set to 'ai'
                insert_query = ("INSERT INTO messages (chat_id, text, actor, is_done, is_send_to_processing) "
                                "VALUES (%s, %s, 'ai', True, True)")
                cursor.execute(insert_query, (chat_id, answer))
                connection.commit()

            else:
                print("No items to process.")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def main():

    while(True):
        getDBData()
        time.sleep(5)


if __name__ == "__main__":
    main()
