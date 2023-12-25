image red_ball = "images/_ball.png"

screen zaglushka():
    text "Кол-во: [run] Ошибки:[error_runs] , Кликайте ЛКМ" xalign 0.1 yalign 0.1

screen keypress():
    text "Кол-во: [run] Ошибки:[error_runs] , Кликайте ЛКМ" xalign 0.1 yalign 0.1
    key "mouseup_1" action Return(True)
    timer 0.8 action Return(False)

label startqte:
    $ _dismiss_pause = False
    $ _dismiss_skip = False
    $ skip = False
    $ pause = 2.0
    $ run = 0
    $ error_runs = 0
    $ renpy.block_rollback()
    $ _skipping = False
    jump start_game

label start_game:
    $ renpy.block_rollback()
    if error_runs == 3:
        #4 ошибки если то выходим из миниигры
        $ _dismiss_pause = False
        $ _dismiss_skip = False
        $ skip = False
        $ pause = 2.0
        $ run = 0
        $ error_runs = 0
        $ renpy.block_rollback()
        $ _skipping = True
        jump qte_lose
    if run == 13:
        #Выходим из миниигры потому что выйграли
        $ _dismiss_pause = False
        $ _dismiss_skip = False
        $ skip = False
        $ pause = 2.0
        $ run = 0
        $ error_runs = 0
        $ renpy.block_rollback()
        $ _skipping = True
        jump qte_win
    show screen zaglushka
    show image("_loading_{}.png".format(run))

    show red_ball:
        xpos 850  # начальная позиция шарика по оси X
        ypos 600  # начальная позиция шарика по оси Y
        linear pause ypos 100  # движение вверх за 2 секунды до позиции 100 по оси Y
    pause pause
    show red_ball:
        xpos 850  # начальная позиция шарика по оси X
        ypos 100  # начальная позиция шарика по оси Y
        linear pause ypos 600  # движение вверх за 2 секунды до позиции 100 по оси Y
    $ renpy.block_rollback()
    pause pause-0.25
    $ renpy.block_rollback()
    call screen keypress
    $ renpy.block_rollback()
    #"You [_return] to press Q"
    #"[pause] [run]"
    if _return:
        $ run += 1
        if run == 4:
            $ pause = 1.5
        if run == 8:
            $ pause = 1
        jump start_game
    else:
        with hpunch
        $ error_runs += 1
        $ run = 0
        jump start_game
    #"Теперь красный шарик двигается вверх!"
    # добавьте свой код дальше

