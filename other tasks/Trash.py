# Определим типы отходов
coin = 'монетка'
potatoes = 'гнилая картошка'
papers = ('картон', 'бумага', 'паспорт')  # уместное использование кортежей
metals = ('консерва', 'вилка', coin, 'бп')
plastics = ('бутылка', 'ведро')
# Открываем контейнер для отходов
# Металл, пластик, другие отходы будем сваливать в кучу
paper_trash, metal_trash, plastic_trash, undefined_trash = [], [], [], []
# Мусоровоз приехал и конвеер запускается
while True:
    try:
        trash = input()
        if trash in papers:
            paper_trash.append(trash)
        elif trash in metals:
            metal_trash.append(trash)
        elif trash in plastics:
            plastic_trash.append(trash)
        else:
            undefined_trash.append(trash)
    except(EOFError, KeyboardInterrupt):
        break

print('содержимое баков:', metal_trash, plastic_trash, undefined_trash)

# Конвеер рассортировал мусор по бакам
# Попробуем найти в баке что-то полоезное, например монетку
try:
    coin_index = metal_trash.index(coin)
    my_coin = metal_trash.pop(coin_index)
    print(f' Ура, я нашёл: "{my_coin}"')
    print('Содержимое бака с металлом после изъятия монетки:', metal_trash)
except ValueError:
    print('В этот раз ничего полезного =(')

# ------------ Обработка металла
# отсортируем металлический мусор по размеру:
metal_trash.sort(key=lambda trash: len(trash))
print('Содержимое бака с металлом после сортировки по возростанию:', metal_trash)
metal_trash.sort(key=lambda trash: len(trash), reverse=True)
print('Содержимое бака с металлом после сортировки по убыванию:', metal_trash)

# Пресуем металлический мусор
metal_ball = '+'.join(metal_trash)
print(f'Вот такой получился комок металла:, "{metal_ball}"')
metal_trash = metal_ball  # Закинем обратно в бак

# ------------ Обработка бумаги
# Отправляем бумажный мусор под пресс. В один момент времени пресс может сжать только одну еденицу мусора
# В итоге должен получится один большой комок 'paper_ball'
paper_ball = ''
while paper_trash:
    last_trash = paper_trash.pop()
    paper_ball += last_trash  # пресуем в комок очередной мусор
print(f'Вот такой получился комок бумаги:, "{paper_ball}"')
paper_trash.append(paper_ball)  # закинем обратно в бак

# ------------ Обработка пластика
plastic_ball = '+'.join(plastic_trash)
paper_trash = [plastic_ball]  # закинем обратно в бак
print(f'Вот такой получился комок пластика:, "{plastic_ball}"')

# ------------ Другие отходы просто сожгём вместе с баком
# Узнаем для статистики, сколько в баке кг гнилой картошки
print(f'В других отходах найдено :, {undefined_trash.count(potatoes)} кг. гнилой картошки')

# Теперь загрузим отсортированные отходы и увезем на переработку
result = paper_trash + metal_trash + plastic_trash
print('Содержимое фургона с отсортированными отходами', result)

