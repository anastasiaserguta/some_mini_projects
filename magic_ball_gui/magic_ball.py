from random import choice
import PySimpleGUI as sg

def about():
    '''
    Программа была написана в марте 2023, когда PySimpleGUI5 еще не требовал регистрации.
    '''

def magic_ball():
    all_answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определенно да', 'Можешь быть уверен в этом', 'Мне кажется, что да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят, что да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Ну типа да', 'Сейчас нельзя предсказать', 'Сконцетрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
    answer = choice(all_answers)
    text_elem = window['-text-']
    text_elem.update('Ответ: {}'.format(answer))

sg.theme('DarkGreen4')

layout = [  [sg.Text('Введи свой вопрос'), sg.InputText()],
            [sg.Button('Узнать ответ'), sg.Button('Всё пока!')],
            [sg.Text('Ответ:', size = (50, 2), key = '-text-') ] ]



window = sg.Window('МАГИЧЕСКИЙ ШАР', layout, size = (500, 100))

while True:
    event, values = window.read()
    if event == 'Узнать ответ':
        magic_ball()

    if event == sg.WIN_CLOSED or event == 'Всё пока!':
        break
    
window.close()