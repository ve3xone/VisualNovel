# Определение персонажей игры.
define unknown = Character('Неизвестный', color="#ffffff")
define unknown_voice = Character('Неизвестный голос ', color="#ffffff")
define liza = Character('Лиза', color="#ffffff")
define anton = Character('Антон', color="#ffffff")
define men = Character('Мужчина', color="#ffffff") #Павел
define pavel = Character('Павел', color="#ffffff") #Павел
define young = Character('Юноша', color="#ffffff")
define robot = Character('Юноша', color="#ffffff")
define scientist = Character('Учёный', color="#ffffff")

#define e = Character('Эйлин', color="#c8ffc8")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

#"О дивный новый мир" (Brave new world)

# Игра начинается здесь:
label start:
    call ac1

    call ac2

    #звук приглушенный стук сердца(1) звук приглушенный стук шестерней и работы механизма(2)
    #show eileen happy #показывает 

    # звуки (1) и (2) стихают звук слабый писк(3)

    #e "Вы создали новую игру Ren'Py."

    #e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    #return