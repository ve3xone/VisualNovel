#### Игровой экран.
screen fifteen_scr:
   
    ##### Таймер.
    if timer_on:
        timer 1.0 action If(fifteen_timer > 0, [SetVariable("fifteen_timer", fifteen_timer-1), Return("smth")], Return("time_is_up") ) repeat True
        text str(fifteen_timer) xalign 0.1 yalign 0.1
   
    ##### игровое поле
    frame:
        xalign 0.5 yalign 0.5
        background Solid("#ccc") #Frame("pic_1.png", 5, 5) # Фон может быть как сплошным цветом или рамкой, которые использует предопределенное имя отображаемое или файл, также вы можете удалить эту строку, чтобы иметь каркас по умолчанию фон.
       
        grid grid_width grid_height spacing 0:
            for every_tile in tiles_list:
                if every_tile["tile_value"] == empty_tile_value and not fifteen_is_solved:
                    null

                else:
                    button:
                        #####
                        #
                        # Использовать просто цифры (классическая игра пятнашки) - раскомментируйте следующие 4 строки и закомментировать строки, которые используются для показа изображения.
                        #Необходимо установить Размер кнопки.
                        # (Фон может быть как сплошным цветом или рамкой, которые использует предопределенное имя отображаемое или файл, также вы можете удалить эту строку, чтобы кнопка по умолчанию фон.)
                        #xminimum 70 xmaximum 70
                        #yminimum 70 ymaximum 70
                        #background Solid("#c00")
                        #text str(every_tile["tile_value"]) xalign 0.5 yalign 0.5
                        #
                        #####
                       

                        #####
                        #
                        #Следующая строка используется, чтобы показать изображение.
                        left_padding 0 right_padding 0 top_padding 0 bottom_padding 0
                        left_margin 0 right_margin 0 top_margin 0 bottom_margin 0
                        add Crop( ( (every_tile["tile_value"]-1)%grid_width*tile_width,
                                        (every_tile["tile_value"]-1)//grid_width*tile_height,
                                        tile_width,
                                        tile_height),
                                        chosen_img)
                        #
                        #####
                           
                       
                        action [ If (every_tile["tile_number"] not in top_row,
                                true = If (tiles_list[every_tile["tile_number"]-grid_width]["tile_value"] == empty_tile_value,
                                true = [SetDict( tiles_list[every_tile["tile_number"]-grid_width], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                false = None),
                                false = None),
                                If (every_tile["tile_number"] not in bottom_row,
                                true = If (tiles_list[min(len(tiles_list)-1, every_tile["tile_number"]+grid_width)]["tile_value"] == empty_tile_value,
                                true = [SetDict( tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+grid_width))], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                false = None),
                                false = None),
                                If (every_tile["tile_number"] not in left_column,
                                true = If (tiles_list[every_tile["tile_number"]-1]["tile_value"] == empty_tile_value,
                                true = [SetDict( tiles_list[every_tile["tile_number"]-1], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                false = None),
                                false = None),
                                If (every_tile["tile_number"] not in right_column,
                                true = If (tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+1))]["tile_value"] == empty_tile_value,
                                true = [SetDict( tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+1))], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                false = None),
                                false = None), Return("smth")
                                ]

    #####Кнопки, что позволит игроку выйти из игры (особенно полезен, если нет Таймер, чтобы закончить игру)
    #textbutton "Выйти" action Jump("quit_fifteen_game") xalign 0.9 yalign 0.1
   
    ##### Кнопку, которая будет показывать все изображение, должна быть использована только в случае, если игра использует образы (а не цифры).
    textbutton "Показать картину" action If( renpy.get_screen("full_image"), Hide("full_image"), Show("full_image") ) xalign 0.5 yalign 0.1


##### Экран, содержащий изображение, чтобы показать (не полезно в классическом пятнадцать игры).
#
screen full_image:
    add chosen_img xalign 0.5 yalign 0.5 at pic_trans


transform pic_trans:
    alpha 0.0 zoom 0.7
    on show:
        parallel:
            linear 1.0 alpha 1.0
        parallel:
            linear 0.6 zoom 1.2
            linear 0.4 zoom 1.0
    on hide:
        linear 0.5 alpha 0.0
#
#####


label fifteen_game:

    ##### Настройки игры.
    #
    #Давайте установим Размер игрового поля в плитки, например плитка 9 (3 х 3).
    $ grid_width = 4
    $ grid_height = 4
   
    # Следующие 4 стро  ки используются для задания изображение, чтобы решить (может быть удален классический игра пятнашки).
    # Рекомендуется, что все изображения будут меньше, чем размер экрана.
    $ chosen_img = "_abstract.png"
    $ chosen_img_width, chosen_img_height = renpy.image_size(chosen_img)
    $ tile_width = chosen_img_width/grid_width
    $ tile_height = chosen_img_height/grid_height
    #

    # Некоторые полезные вычисления:
    $ top_row = []
    python:
        for i in range(0, grid_width):
            top_row.append (i)
    $ bottom_row = []
    python:
        for i in range(0, grid_width):
            bottom_row.append ( (grid_width*(grid_height-1)+i) )
    $ left_column = []
    python:
        for i in range(0, grid_height):
            left_column.append (grid_width*i)
    $ right_column = []
    python:
        for i in range(0, grid_height):
            right_column.append (grid_width*(i+1)-1)

   
    #Давайте установим игрового поля все плитки на свои места.
    $ tiles_list = []
    python:
        for i in range (0, grid_height):
            for j in range (0, grid_width):
                tiles_list.append ( {"tile_number":(i*grid_width+j), "tile_value":(i*grid_width+(j+1))} )


    #Давайте установим пропущенный плитки - оно может быть случайным или последний в очереди (как в классическом пятнадцать игры).
    $ empty_tile_value = renpy.random.randint ( 1, grid_width*grid_height )
    #$ empty_tile_value = grid_width*grid_height
    #
   
    # Некоторые переменные:
    # позволит нам контролировать, если пропустил плитки должны быть показаны
    $ fifteen_is_solved = False
    # установка таймера, чтобы сделать игру более сложной
    $ fifteen_timer = 120
    # позволит нам контролировать Таймер
    $ timer_on = False
   
    # Это показать на экране игры.
    show screen fifteen_scr
   
    # Чтобы быть уверенным, что головоломка может быть решена, просто беспорядочно двигаться некоторые плитки.
    # Этот процесс может быть показано, что игрок - раскомментируйте строку, которая задает паузу между движениями.
    # Количество ходов должно быть достаточно большим, чтобы перетасовать хорошая плитка,
    # также должно быть нечетным, чтобы избежать ситуации, когда случайные ходы будут приносить все плитки обратно на свои исходные позиции.
    $ shuffle_moves = 21
    label tiles_shuffle:
        if shuffle_moves >0:
            python:
                possible_moves_list = []
                for j in tiles_list:
                    if j["tile_value"] == empty_tile_value:
                        if j["tile_number"] not in top_row:
                            possible_moves_list.append ("top")
                        if j["tile_number"] not in bottom_row:
                            possible_moves_list.append ("bottom")
                        if j["tile_number"] not in left_column:
                            possible_moves_list.append ("left")
                        if j["tile_number"] not in right_column:
                            possible_moves_list.append ("right")
                        move_tile = renpy.random.choice (possible_moves_list)
                        if move_tile == "top":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]-grid_width]["tile_value"]
                            tiles_list[j["tile_number"]-grid_width]["tile_value"] = empty_tile_value
                        elif move_tile == "bottom":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]+grid_width]["tile_value"]
                            tiles_list[j["tile_number"]+grid_width]["tile_value"] = empty_tile_value
                        elif move_tile == "left":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]-1]["tile_value"]
                            tiles_list[j["tile_number"]-1]["tile_value"] = empty_tile_value
                        elif move_tile == "right":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]+1]["tile_value"]
                            tiles_list[j["tile_number"]+1]["tile_value"] = empty_tile_value
                        shuffle_moves -= 1
                        #renpy.pause(0.1)           # Если используется пауза должна быть не так долго.
                        renpy.jump("tiles_shuffle")
               
    #Теперь можно запустить Таймер.
    $ timer_on = True
    $config.skipping=None
    # Игровой цикл.
    label fifteen_game_loop:
        $ renpy.block_rollback()
        $ _skipping = False
        $ result = ui.interact()
        $ fifteen_timer = fifteen_timer
        if result == "time_is_up":
            jump fifteen_lose
        python:
            for j in tiles_list:
                if j["tile_value"]-1 != j["tile_number"]: # будет продолжать игру, если, по крайней мере, одна плитка находится не на своем месте
                    renpy.jump("fifteen_game_loop")
        jump fifteen_win

label fifteen_win:
    #Это позволит отключить Таймер.
    $ timer_on = False
    $ renpy.pause(0.1, hard = True)
    $ renpy.pause(0.1, hard = True)
   
    # Это покажет недостающие плитки на свои места.
    $ fifteen_is_solved = True
    hide screen fifteen_scr
    $ renpy.block_rollback()
    $ _skipping = True
    $ fifteen_comp = True
    jump contiune_2

label fifteen_lose:
    $ timer_on = False
    $ renpy.pause(0.1, hard = True)
    $ renpy.pause(0.1, hard = True)
    hide screen fifteen_scr
    $ renpy.block_rollback()
    $ _skipping = True
    $ fifteen_comp = False
    jump contiune_2

#label quit_fifteen_game:
#    hide screen fifteen_scr
#    return