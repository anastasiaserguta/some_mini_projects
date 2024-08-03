from random import *
from sys import exit

all_word = [
            'сосед', 'зло', 'житель', 'грудь', 'спорт', 'психология', 'диван', 'влияние', 'телевизор',
            'пора', 'еда', 'край', 'забота', 'комплекс', 
            'сожаление', 'эпоха', 'перевод', 'приятель', 
            'музей', 'звонок', 'диван', 'фон', 'князь', 
            'цена', 'союз', 'гражданин', 'плечо', 
            'взаимодействие', 'дело', 'доктор', 'машина', 
            'получение', 'завод', 'достоинство', 'вина', 'клуб', 
            'степень', 'русский', 'снег', 'кожа', 'начальство', 
            'канал', 'сущность', 'собрание', 'проведение', 'двигатель', 
            'курс', 'конструкция', 'память', 'система', 'материал', 'клуб', 
            'глубина', 'комплекс', 'тема', 'издание', 'государство', 'кризис', 
            'фронт', 'предел', 'сочинение', 'положение', 'дача', 'перевод', 
            'препарат', 'профессор', 'рабочий', 'свидетель', 'округ', 
            'правило', 'обработка', 'инженер', 'проверка', 'сумка', 
            'деталь', 'признание', 'деталь', 'мешок', 'корпус', 'хозяйство', 
            'величина', 'сведение', 'слово', 'брак', 'присутствие', 'покой', 
            'достоинство', 'страна', 'капитан', 'эксперт', 'качество', 
            'председатель', 'проверка', 'промышленность', 'налог', 
            'квартира', 'повод', 'обеспечение', 'программа', 'лейтенант'
    ]

one_word = choice(all_word)
total = -1
total_word = 0
score = 6

def base_game():

    '''
    Старый тренировочный проект 2023 года. Требует оптимизации с точки зрения более краткого изложения и построения кода.
    Несмотря на ошибки, на мой взгляд, выглядит интересно!
    PS: выполнен в рамках прохождения курса на платформе Stepik.
    '''
    
    def hangman(total):
        stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
        return stages[total]

    def game():
        global total
        global total_word
        global score

        
        
        one_word1 = one_word
        
        secret = ['*' for i in range(len(one_word))]
        
        # while total >= -6 and total_word <= len(one_word):
        while score > -1:
            print(*secret)
            score -= 1
            print('Осталось', score, 'попыток')
            if total == -1:
                print(hangman(total))
                your_answer = input('Введи слово или букву слова ')
                if your_answer == one_word:
                    print('Ты угадал! Молодец, это слово - ', one_word)
                    break
                elif your_answer in one_word:
                    print('Такая буква есть, ты прав! ')
                    for_count = one_word.count(your_answer)
                    if for_count > 1:
                        for j in range(len(one_word)):
                            if one_word[j] == your_answer:
                                secret[j] = your_answer
                            
                        total_word += 1
                        
                    else:
                        position = one_word1.find(your_answer)
                        secret[position] = your_answer
                        total_word += 1
                    
                    
                else:
                    print('Упс, ошибочка:( ')
                    total += -1
                    
                    
            
            elif total == -2:
                print(hangman(total))
                your_answer = input('Введи слово или букву слова ')
                if your_answer == one_word:
                    print('Ты угадал! Молодец, это слово - ', one_word)
                    break
                elif your_answer in one_word:
                    print('Такая буква есть, ты прав! ')
                    for_count = one_word.count(your_answer)
                    if for_count > 1:
                                            
                        for j in range(len(one_word)):
                            if one_word[j] == your_answer:
                                secret[j] = your_answer
                                               
                        total_word += 1
                        
                    else:
                        position = one_word1.find(your_answer)
                        secret[position] = your_answer
                        total_word += 1
                else:
                    print('Упс, ошибочка:( ')
                    total += -1
                    print(hangman(total))

            elif total == -3:
                print(hangman(total))
                your_answer = input('Введи слово или букву слова ')
                if your_answer == one_word:
                    print('Ты угадал! Молодец, это слово - ', one_word)
                    break
                elif your_answer in one_word:
                    print('Такая буква есть, ты прав! ')
                    for_count = one_word.count(your_answer)
                    if for_count > 1:
                                           
                        for j in range(len(one_word)):
                            if one_word[j] == your_answer:
                                secret[j] = your_answer
                            
                        total_word += 1
                        
                    else:
                        position = one_word1.find(your_answer)
                        secret[position] = your_answer
                        total_word += 1
                else:
                    print('Упс, ошибочка:( ')
                    total += -1
                    print(hangman(total))    

            elif total == -4:
                print(hangman(total))
                your_answer = input('Введи слово или букву слова ')
                if your_answer == one_word:
                    print('Ты угадал! Молодец, это слово - ', one_word)
                    break
                elif your_answer in one_word:
                    print('Такая буква есть, ты прав! ')
                    for_count = one_word.count(your_answer)
                    if for_count > 1:
                                            
                        for j in range(len(one_word)):
                            if one_word[j] == your_answer:
                                secret[j] = your_answer
                            
                        total_word += 1
                        
                    else:
                        position = one_word1.find(your_answer)
                        secret[position] = your_answer
                        total_word += 1
                else:
                    print('Упс, ошибочка:( ')
                    total += -1
                    print(hangman(total))
            
            elif total == -5:
                print(hangman(total))
                your_answer = input('Введи слово или букву слова ')
                if your_answer == one_word:
                    print('Ты угадал! Молодец, это слово - ', one_word)
                    break
                elif your_answer in one_word:
                    print('Такая буква есть, ты прав! ')
                    for_count = one_word.count(your_answer)
                    if for_count > 1:
                                            
                        for j in range(len(one_word)):
                            if one_word[j] == your_answer:
                                secret[j] = your_answer
                            
                        total_word += 1
                        
                    else:
                        position = one_word1.find(your_answer)
                        secret[position] = your_answer
                        total_word += 1
                else:
                    print('Упс, ошибочка:( ')
                    total += -1
                    print(hangman(total))

            elif total == -6:
                print(hangman(total))
                your_answer = input('Введи слово или букву слова ')
                if your_answer == one_word:
                    print('Ты угадал! Молодец, это слово - ', one_word)
                    break
                elif your_answer in one_word:
                    print('Такая буква есть, ты прав! ')
                    for_count = one_word.count(your_answer)
                    if for_count > 1:
                                            
                        for j in range(len(one_word)):
                            if one_word[j] == your_answer:
                                secret[j] = your_answer
                            
                        total_word += 1
                        
                        total_word += 1
                        
                    else:
                        position = one_word1.find(your_answer)
                        secret[position] = your_answer
                        total_word += 1
                else:
                    print('Упс, ошибочка:( ')
                    total += -1
                    print(hangman(total))

    def starting():
        if answer.lower() == 'да':
            game()
        elif answer.lower() == 'нет':
            print('Ну ладно, до свидания:(')
            exit()

    name = input('Добро пожаловать в БАЛДУ 0.1! Введите Ваше имя: ')
    print(name, ',', 'в этой игре тебе нужно за ограниченное количество попыток (пока не нарисуется виселица) угадать слово, загаданное программой из определенного списка')
    answer = input('Начнем? Введи ДА или НЕТ: ')
    starting()

    if total == -7:
        print('Ясно. Проиграл.')
        print(one_word)
    else:
        print('Ого!')




print(base_game.__doc__)
base_game()