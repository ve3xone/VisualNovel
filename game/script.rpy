﻿# Определение персонажей игры.
define unknown = Character('Неизвестный', color="#ffffff")
define unknown_she = Character('Неизвестная', color="#ffffff")
define unknown_voice = Character('Неизвестный голос ', color="#ffffff")
define liza = Character('Лиза', color="#ffffff")
define anton = Character('Антон', color="#ffffff")
define men = Character('Мужчина', color="#ffffff") #Павел
define pavel = Character('Павел', color="#ffffff") #Павел
define young = Character('Юноша', color="#ffffff")
define robot = Character('Робот', color="#ffffff")
define robots = Character('Роботы', color="#ffffff")
define i_pavel_liza = Character('Я, Павел и Лиза', color="#ffffff")
define robot_teacher = Character('Робот-учитель', color="#ffffff")
define robot_moroz = Character('Робот-мороженщик', color="#ffffff")
define kid = Character('Ребенок', color="#ffffff")
define scientist = Character('Учёный', color="#ffffff")
define leader = Character('Ведущий', color="#ffffff")
define robot_leader = Character('Робот-ведущий', color="#ffffff")
define megabrain = Character('Мегамозг', color="#ffffff")

#Переменные выборов
default flipped_the_booklet = False
default qte_comp = False
default qte_losed = False
default Calmed_Lisa_down = False
default Select_2_and_3 = False
default fifteen_comp = False
default qte_ac3 = False
default fifteen_ac3 = False

# Игра начинается здесь:
label start:

    #типо печатает на клавиатуре
    show text "g" with Dissolve(0.08)
    show text "go" with Dissolve(0.08)
    show text "goy" with Dissolve(0.08)
    show text "goyd" with Dissolve(0.08)
    show text "goyda" with Dissolve(0.08)
    show text "goyda " with Dissolve(0.08)
    show text "goyda g" with Dissolve(0.08)
    show text "goyda ga" with Dissolve(0.08)
    show text "goyda gam" with Dissolve(0.08)
    show text "goyda game" with Dissolve(0.08)
    show text "goyda games" with Dissolve(0.08)
    show text "goyda games " with Dissolve(0.08)
    show text "goyda games п" with Dissolve(0.08)
    show text "goyda games пр" with Dissolve(0.08)
    show text "goyda games пре" with Dissolve(0.08)
    show text "goyda games пред" with Dissolve(0.08)
    show text "goyda games предс" with Dissolve(0.08)
    show text "goyda games предст" with Dissolve(0.08)
    show text "goyda games предста" with Dissolve(0.08)
    show text "goyda games представ" with Dissolve(0.08)
    show text "goyda games представл" with Dissolve(0.08)
    show text "goyda games представля" with Dissolve(0.08)
    show text "goyda games представляе" with Dissolve(0.08)
    show text "goyda games представляет" with Dissolve(0.08)

    pause 1.5

    call ac1 from _call_ac1
    
    call ac2 from _call_ac2

    call ac3 from _call_ac3

    return