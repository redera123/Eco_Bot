import random

Shans = (
    'Не знаешь применению Мусору? Если это одежда, отдай нуждающиемся!',
    'Что делать если много пластиковых бутылок? Сделай из них респиратор! https://www.youtube.com/watch?v=gRUDcqzJAG8 Как на этом видео!',
    'Много ненужной мукалатуры? Сделай из них оригами!',
        )


def Musoru_Shans():
    return random.choice(Shans)

print(Musoru_Shans())