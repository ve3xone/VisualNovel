# Определение персонажей игры.
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
default Calmed_Lisa_down = False
default Select_1_and_3 = False
default fifteen_comp = False
default qte_ac3 = False
default fifteen_ac3 = False

# Игра начинается здесь:
label start:

    call ac1 from _call_ac1
    
    call ac2 from _call_ac2

    call ac3 from _call_ac3

    return