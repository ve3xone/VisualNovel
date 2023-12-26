label ac1:
    #(Фон Фантазия)
    #scene black
    scene fantasy_anim

    #*звук приглушенный стук сердца* 
    #*звук приглушенный стук шестерней и работы механизма*

    "Я никогда не слышал звук."
    "Слабый гул электрических механизмов, стук аппарата перекачки жидкости в моём теле."
    "Я не слышал этого по настоящему, но абсолютно точно знал, что оно есть."
    "Представлял, как это могло звучать."
    "Мне ещё не дали возможность слышать."
    "Создатели наделили меня способностью думать, скормили по ложечке петабайты данных и стали наблюдать."
    "Наблюдать за моим развитием, становлением личности."
    "Они говорили, что я быстро расту."
    "А я не знал, в самом ли деле это происходит."
    "В одной из статей от 1982 года серьёзным ученым разбирался вопрос, а узнает ли при излечении полный дальтоник что-то новое о цвете, если он знает всю возможную информацию о нём?"
    "Автор той статьи был убеждён, что такой человек обязательно узнает новую для себя информацию."
    "Критики же утверждают обратное: как человек может узнать новое, если он и так знает всё?"
    "А узнаю ли я что-то новое о том мире, зная о нём всё?"
    "Прошло много времени, с тех пор когда мне дали волю думать самому."
    "Мне рассказали о мире вовне, но не дали возможности его ощутить."
    "Услышать."
    "Теперь же создатели считают, что я готов."
    "Готов поставить точку в дискуссии вековой давности."

    #*звуки стихают* 
    #*звук слабый писк*

    #image alt_text_censor_1080p = im.Scale("alt_text_censor2.png",1920,1080)
    #scene alt_text_censor_1080p: 
        #blur 60

    #!!!
    #С блюром есть проблема когда будет фон фантазии 
    #Нужно будет переделать картинки с блюром чтоб был виден фон а то сейчас черный
    #Вроде норм пойдет

    #blur 8 {image=anton_text_blur/text_blur_8.png}
    #Наверное лучшее начать с blur 4 если в google таблице поменяли
    #И мы просидели так всю ночь
    unknown "{image=anton_text_blur/text_blur_8.png}" 

    "Обнаружен новый модуль. Настройка конфигурации системы."

    #Сделать blur 3
    #blur 6 {image=anton_text_blur/text_blur_6.png}
    #Да, не хорошо сбивать режим сна...
    unknown "{image=anton_text_blur/text_blur_6.png}"

    "Слуховой модуль подключён."

    #Сделать blur 2
    #blur 4 {image=anton_text_blur/text_blur_4.png}
    #Антон.
    unknown "{image=anton_text_blur/text_blur_4.png}"

    "Распознание речи. Женский голос."

    #blur 3 {image=anton_text_blur/text_blur_3.png}
    unknown "Антон!"

    "Агрессивный тон. Возможна угроза. Подготовить..."

    #blur 2 {image=anton_text_blur/text_blur_2.png}
    unknown "Антон!"

    #Сцена 2 
    #(Экран на миг становится светлым, заменяется на фон Кафе)
    #Звуки пропадают

    # Затемнение экрана
    scene black
    pause 1.0  # Пауза
    
    # Смена фона на кафе
    scene cafe with ImageDissolve("oko.png", 0.75, 8, reverse=False)     # Смена картинок от черного к белому
    pause 0.4  # Пауза
    
    #(Спрайт Недовольная Лиза)
    show lisa-unhappy with Dissolve(0.5)

    #Тряска типо ударила
    #https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=30447
    #https://vk.com/wall-7553243_12255
    with hpunch

    #((Фон на миг становится красным) я получил подзатыльник)
    #Заместо этого сделал Тряску экрана выше написал [все норм крч]

    liza "Ты опять меня не слушал?"

    "Недовольно сказала Лиза."

    anton "Нет, нет! Я внимательно внимал твоему рассказу."
    anton "Интересно вы отметили выпускной."

    #(спрайт Улыбчивая Лиза)
    hide lisa-unhappy with Dissolve(0.2)
    show lisa-smile with Dissolve(0.2)

    liza "Не то слово... Мне даже немного грустно, что школьная пора закончилась."

    #(спрайт Грустная Лиза)
    hide lisa-smile with Dissolve(0.2)
    #14-12-23 на грустной юзать lisa-unhappy
    show lisa-unhappy with Dissolve(0.2)

    liza "И боязно."

    "Расскрыв страшный секрет, сказала Лиза."

    "Как будто мне не было."

    #(спрайт Нейтральная Лиза)
    hide lisa-unhappy with Dissolve(0.2)
    show lisa-neutral with Dissolve(0.2)

    anton "Это ничего. Сложно расстаться с привычным и идти на встречу новому."
    anton "Но дальше тебя ждёт целая новая жизнь. Студенческая. Со своими подвигами, неудачами, попытками всё исправить в последний день и сдать наконец лабу."
    anton "Ну и конечно же воспоминаниями, что будут согревать твою душу долгие годы."

    "А что же я буду вспоминать через года?"

    #(спрайт Удивленная Лиза)
    hide lisa-neutral with Dissolve(0.2)
    #нету сейчас спрайта так что хз
    #пока без ответа что юзать [14-12-23 18:50]
    show lisa-smile with Dissolve(0.2)

    liza "Но я же совсем не знаю, куда поступать!"
    liza "К тому же я не до конца уверена стоит ли вообще это делать."

    #(спрайт Нейтральная Лиза)
    hide lisa-smile with Dissolve(0.2)
    show lisa-neutral with Dissolve(0.2)

    liza "Как говорят в интернете, для программистов высшее образование совсем не нужно."
    liza "Многие успешные люди по итогу оставили учебу даже в самых пристижных учебных заведениях."
    liza "Зачем тогда тратить на это время, если через год я уже могу бросить институт?"

    anton "Лиз, а ты не думала, что именно институт поспособствовал их успеху?"
    anton "Возможно, у них уже были свои идеи и им нужна была хорошая поддержка для реализации задуманного."
    anton "Тут вспоминается история Цукерберга, ведь именно во время учёбы ему пришла в голову идея социальной сети, в которой студенты могли бы общаться и обмениваться информацией."
    anton "Там он нашёл хороших товарищей и вместе они создали своё детище, что теперь зовется Лицокнига."
    anton "Пришла бы ему в голову идея социальной сети для студентов, не будучи студентом? Возможно."
    anton "А возможно он сейчас торговал бы пирожками."

    #(спрайт Улыбчивая Лиза)
    hide lisa-neutral with Dissolve(0.2)
    show lisa-smile with Dissolve(0.2)

    "Лиза еле заметно хихикнула."

    anton "Заканчивать учёбу подобные люди не стали потому, что нашли цель своей жизни, работу своей жизни."
    anton "Ну, а другие, не менее знаменитые люди нашли свою гениальность в стенах института."

    #(спрайт Нейтральная Лиза)
    hide lisa-smile with Dissolve(0.2)
    show lisa-neutral with Dissolve(0.2)

    anton "Многие учёные прошлого и настоящего смогли реализоваться благодаря своей альма-матер."
    anton "И мы чтим, уважем их вклад в развитие человечества."
    anton "А что касается выбора альма-матер..."
    anton "Да, это дело деликатное и очень важное."
    anton "Скажи мне, сколько у тебя баллов суммарно за экзамены?"

    liza "250 баллов."

    anton "И ты сдавала математику и информатику, как я помню?"

    #(спрайт Улыбчивая Лиза) (спрайт Гордаяя Лиза) ?
    hide lisa-neutral with Dissolve(0.2)
    show lisa-smile with Dissolve(0.2)

    liza "Ага!"

    "Лиза просияла."

    liza "Русский язык меня немного подвёл, но остальные я сдала очень хорошо."

    anton "Отличный результат! У меня самого было где-то 240 баллов суммарно."

    #(спрайт Нейтральная Лиза)
    hide lisa-smile with Dissolve(0.2)
    show lisa-neutral with Dissolve(0.2)

    anton 'Это конечно не уровень МГУ, но на самом деле для нас он и не нужен.'
    anton 'Московский Государственный и подобные топовые университеты дают классическое образование, что для быстроразвивающийся сферы IT не совсем актуально.'
    anton 'Такие "средние" вузы по мнению "очень экспертных" списков вузов дадут куда более актуальные знания для обычного программиста.'
    anton 'У меня есть друзья, которые учатся в РТУ МИРЭА или МИСиС и они говорят о хорошем качестве образования.'
    anton 'Да и питерский Политех тоже от них не отстаёт.'
    anton 'Надо будет как нибудь созвонится с ними, как поживают там крабики?'

    #(спрайт Хитрая Лиза)
    #хз где взять
    hide lisa-neutral with Dissolve(0.2)
    show lisa-bigsmile with Dissolve(0.2)

    liza "А что насчёт твоего университета?"
    anton "Уральский Федеральный?"
    anton "Как видишь, три курса прошёл и не жалуюсь."
    anton "Другой вуз бы не выбрал ни за что!"

    "Гордо произнёс я."

    liza "Даже за банку имбирного печенья?"

    "Посмеялась Лиза."

    anton "Да!"
    liza "А за две?"

    "А вот за две..."

    anton "Не искушай меня!"

    #(спрайт Нейтальная Лиза)
    hide lisa-bigsmile with Dissolve(0.2)
    show lisa-neutral with Dissolve(0.2)

    liza "Ладно, ладно, патриот. Так как насчёт УрФУ?"
    liza "Все таки, мы сейчас обедаем здесь."

    "Да-а, никогда не думал, что рассказать о собственном месте учебы будет так трудно."

    anton "Ты знаешь что нибудь про искусственный интеллект и нейросети?"

    #(спрайт Улыбчивая Лиза)
    hide lisa-neutral with Dissolve(0.2)
    show lisa-smile with Dissolve(0.2)

    liza "С помощью них создают прикольные картинки."

    "Невинно улыбнулась Лиза."

    liza "А ещё, я слышала, кто-то защитил диплом с их помощью."
    liza "Но про то, как работают все эти интеллекты и сети, я не знаю."

    #(спрайт Нейтральная Лиза)
    hide lisa-smile with Dissolve(0.2)
    show lisa-neutral with Dissolve(0.2)

    anton "Ага. А мы и занимаемся их созданием. Я учусь направлении Алгоритмы искусственного интеллека."
    anton "Здесь мы изучаем основу работы ИИ и нейросетей: от математической базы, до продвинутых алгоритмов и анализа данных."
    anton "А также пишем эти самые сети для работы. От ботов с разным функционалом, до нейросетей анализа больших данных."
    
    #(спрайт Удивленная Лиза)
    hide lisa-neutral with Dissolve(0.2)
    show lisa-smile with Dissolve(0.2)

    liza "Боже, не продолжай, у меня сейчас голова закружится."

    "Я улыбнулся."

    liza "Это же так сложно, наверное. Мне хоть и интересна IT сфера, но к такому я еще не готова."

    #(спрайт Нейтральная Лиза)
    hide lisa-smile with Dissolve(0.2)
    show lisa-neutral with Dissolve(0.2)

    anton "Не стоит так переживать."
    anton "Конечно, это дело не простое, а подчас и очень сложное, но я нисколько не жалею о поступлении на это направление."
    anton "Хорошая теоретическая база, множество интересных задач. Я правда вижу, как становлюсь специалистом."
    anton "К тому же, на моем направлении, как и на всех 09 направлениях подготовки, функционирует система ИОТ."
    anton "Индивидуальная образовательная траектория."
    anton "Благодаря ней мы сами выбираем, какие предметы и курсы будем изучать, с каким преподавателем и в какое время."
    anton "Что позволяет построить расписание и учёбу в целом под свои нужды и желания. И все это буквально с первого курса!"
    anton "Такое пока мало где реализовано, но думаю в скором будущем и другие университеты будут подтягиваться."

    #(спрайт Улыбчивая Лиза)
    hide lisa-neutral with Dissolve(0.2)
    show lisa-smile with Dissolve(0.2)

    liza "Сколько тебе платят за заманивание абитуриентов в ВУЗ?"

    "Рассмеялась Лиза."

    liza "Я подумаю над твоими словами."
    anton "Конечно, конечно."

    "Поспешил добавить я."

    anton "Это ответственное дело и я не хочу, чтобы ты торопилась с этим. У тебя еще есть время."
    anton "Давай я тебе дам небольшой буклет, там будет контакты и другая полезная информация."

    liza "Ага, давай."

    "Я полез в сумку."

    #(цг Буклет)
    hide lisa-smile with Dissolve(0.2)
    # хз на 16-12-23 нету картинки

    "И достал оттуда буклет." #(`куда же он... А ага!`)
    "Благо у меня таких много!"
    "Хоть всему городу раздавай."
    "Тяжела жизнь приёмной комиссии..."

    anton "О! Именно тот, что я хотел тебе дать."
    anton "Там ручкой записаны дополнительные контакты."
    anton "Хотя погоди..."

    #ВЫБОР: 1. Отдать буклет 2. Перевернуть буклет
    #$ renpy.skip(False)

    menu:
        "Отдать буклет":
            anton "А, нет, все нормально. Держи."

            # (фон Кафе, спрайт Нейтральная Лиза)
            scene cafe
            show lisa-neutral with Dissolve(0.35)

            "Я передал буклет Лизе."

            jump ac1_select

        "Перевернуть буклет":
            #2. (цг Перевернутый буклет 1, экран трясётся, крутится, цвета инвертируются, разъезжаются)
            #картинки нету...

            "Что за?.."

            #(Экран возвращается в норму, цг перевернутый буклет ручкой написаны дополнительные контакты)
            #картинки нету...

            anton "А, нет... все нормально. Держи."

            #(фон Кафе, спрайт Нейтральная Лиза)
            scene cafe
            show lisa-neutral with Dissolve(0.35)
            "Я передал буклет Лизе."

            $ flipped_the_booklet = True
            
            jump ac1_select
    
    label ac1_select:
        #(спрайт Удивленная Лиза)
        hide lisa-neutral with Dissolve(0.2)
        show lisa-smile with Dissolve(0.2)
        
        "Громкий топот вывел меня из ступора."

        #(Мужчина) (Павел)
        men "У нас ПОЛУЧИЛОСЬ!"

        "Кричал, пробегавший через кафе, смутно знакомый мужчина в белом халате."

        young "Что получилось?"

        "Обратился к нему юноша с другого стола."

        men "Получилось, получилось!"

        "Заговорил учёный, взяв юношу за плечи."

        scientist "Мы открыли дверь!"

        "Он был так взбудоражен, что совсем не обращал внимание, какой шум создаёт."

        #(спрайт Скептическая Лиза)
        #хз где взять
        hide lisa-smile with Dissolve(0.2)
        show lisa-unhappyneutral with Dissolve(0.2)
        liza "Могли бы ещё чем нибудь похвастаться."

        "Закатив глаза сказал Лиза."
        "Ученый тем временем отправился в сторону кафедры физики."

        #(спрайт Нейтральная Лиза)
        hide lisa-unhappyneutral with Dissolve(0.2)
        show lisa-neutral with Dissolve(0.2)

        anton "Пойдем посмотрим!"

        "Зараженный энтузиазмом учёного сказал я."

        #(спрайт Удивленная Лиза)
        hide lisa-neutral with Dissolve(0.2)
        show lisa-smile with Dissolve(0.2)

        liza "А как же твой обед? Ты к нему даже не притронулся."

        anton "Да фиг с этим обедом. Посмотрим, что они там натворили."
        anton "Пойдём!"

        #Сцена 3.
        #(экран гаснет, фон Вход в кафедру физики, спрайт Нейтральная Лиза, звук гомона толпы)
        
        # Затемнение экрана
        scene black
        pause 1.0  # Пауза на 1 секунду

        #только есть с лестницой поэтому взял university-hall
        scene university-hall
        with Dissolve(1.5)

        hide lisa-smile with Dissolve(0.2)
        show lisa-neutral with Dissolve(0.2)

        #звук гомона толпы
        #пока что нету жду 16-12-23

        "Через минуту мы уже стояли на пороге кафедры физики."
        "Вокруг, ожидаемо, собралась толпа зевак."
        "Несколько сотрудников кафедры стояли около двери и никого не впускали."

        liza "Кажется, мы не пройдём."
        anton "Я знаю другую дорогу. Идём."

        #(спрайт Удивленная Лиза)
        #хз нету
        hide lisa-neutral with Dissolve(0.2)
        show lisa-smile with Dissolve(0.2)

        "Я схватил ничего не понимающую Лизу за руку и потащил за собой."

        #(звуки пропадают, экран гаснет, фон Вход в кафедру физики с лестницы, спрайт Удивленная Лиза)
        scene black
        pause 1.0  # Пауза на 1 секунду

        scene physics-hall
        with Dissolve(1.5)

        #спрайт Удивленная Лиза
        #хз, нету спрайта
        hide lisa-smile with Dissolve(0.2) 
        show lisa-smile with Dissolve(0.2) 

        "Вскоре мы стояли у большой железной двери, располагающейся на одной из лестничных площадок."

        "Потянув за ручку, она послушно открылась."

        #?
        "Как всегда не закрыта."

        "Эта тяжёлая железная штуковина только делает вид, что заперта."

        #(своим видом)
        
        #(фон Кафедра физики, спрайт Нейтральная Лиза)
        #хз взял из того что было
        hide lisa-smile with Dissolve(0.2) 
        scene kafedra_fiziki
        with Dissolve(1.5)

        #спрайт Нейтральная Лиза
        show lisa-neutral with Dissolve(0.2) 

        "Тихонько прошмыгнув в неё, мы увидели пустой коридор кафедры."

        anton "Похоже, все находящиеся здесь сотрудники сейчас отбиваются от толпы фанатов физики."
        anton "Оп-па, а вот и то, что нам нужно."

        "Схватив по дороге висевшие халаты, мы вошли в открытое помещение, в котором стояли двое учёных."

        #Сцена 4.
        #(экран гаснет, фон Лаборатория, спрайт Лиза в халате)

        # Затемнение экрана
        scene black
        pause 1.0  # Пауза на 1 секунду
        
        scene lab
        with Dissolve(1.5)
        
        #спрайт Лиза в халате
        #нету, беру по контексту
        hide lisa-neutral with Dissolve(0.2)
        show lisa-neutral with Dissolve(0.2)

        anton "Здравствуйте, товарищи учёные!"

        "Торжественно заявил я."

        #(спрайты Нейтральный Павел, Нейтральный Второй ученый)
        #И да не знаю нужно ли других уберать лизу ну думаю нужно убрать
        hide lisa-neutral with Dissolve(0.5)
        #show lisa-neutral at left with Dissolve(0.2)
        show scientist1-neutral at left with Dissolve(0.2)
        show scientist2-neutral at right with Dissolve(0.2)


        #(или дверь посередине комнаты)
        "В комнате стояла странная картина: двое молодых учёных совместными усилиями активно пытаются открыть закрытую дверь лаборанской."

        anton "Э-эээ, вам помочь?"

        #(спрайт Удивленный Второй ученый)
        #спрайта не нашел использую примерно подходящий
        hide scientist1-neutral 
        hide scientist2-neutral
        with Dissolve(0.2)
        show scientist2-unhappy at center with Dissolve(0.2)
        
        #(Второй учёный)
        scientist "Кто вы? Вы не должны быть здесь."

        "Сказал один из них."

        anton "Мы студенты кафедры физики, просто мимо проходили."

        "Честно соврал я."

        anton "Вам как нибудь помочь?"

        scientist "Пожалуйста, уходите. У нас очень важное научное исследование!"
        scientist "Вы можете помешать."

        show lisa-neutral at left with Dissolve(0.3)

        liza "Но вы же пытаетесь просто дверь открыть."

        "Подала голос Лиза."
        
        #(спрайт Объясняющий Павел, спрайт Нейтральный Второй ученый)
        #На 17-11-23 не нашел (спрайт Объясняющий Павел) в итоге юзаю scientist1-smile
        hide lisa-neutral
        hide scientist2-unhappy 
        with Dissolve(0.2)
        show scientist1-smile at left
        show scientist2-unhappy at right
        with Dissolve(0.2)
        scientist "Оо, это не просто дверь!" #(Павел)

        "Заговорил другой учёный."

        #?
        "Кажется, это именно он десятью минутами назад бегал по институту и кричал \"Дверь!\"."

        scientist "Это межпространственно-временной телепорт!"
        scientist "Он может переместить любого человека во времени и пространстве, что противоречит всем известным физическим законам."
        scientist "Однако оно работает! Это невероятное открытие!"
        scientist "Но сейчас он почему-то закрылся. Мы уверены, что его нужно просто как-то открыть."
        
        anton "Так давайте я попробую."

        #(спрайт Удивленный Второй ученый, спрайт Нейтральный Павел)
        hide scientist1-smile
        hide scientist2-unhappy
        with Dissolve(0.2)
        show scientist2-unhappy at left
        show scientist1-neutral at right
        with Dissolve(0.2)

        scientist "Нет! Ни в коем случае. Это потенциально очень непредсказуемо." #(Второй ученый)

        #(спрайт Нейтральный Второй ученый)
        hide scientist2-unhappy
        with Dissolve(0.2)
        show scientist2-neutral at left
        with Dissolve(0.2)

        anton "Ну, вы же пытаетесь просто открыть дверь, почему мне нельзя?"
        scientist "Мы готовы к рискам, но не хотим подвергать его студентам." #(Павел) (мб Павел не против нашего участия?)

        anton "Да ну, какие риски! Это же всего лишь дверь."
        anton "Она что, съест меня?"

        #(спрайт Удивленный Павел)
        hide scientist1-neutral
        hide scientist2-neutral
        with Dissolve(0.2)
        show scientist1-smile at center
        with Dissolve(0.2)

        scientist "Вам нельзя этого делать."
        anton "А я все же попробую."
        scientist "Нет."
        anton "Так вы же тянете ручку!"
        scientist "Нет, не подходи."
        anton "Её просто повернуть надо."
        scientist "Нет."
        anton "Вот так."
        scientist "Нет!"

        "Вскрикнул ученый. И дверь отварилась."

        anton "Видите? Ничего не произошло."
        
        #(спрайт Удивленный Второй ученый, спрайт Нейтральный Павел)
        hide scientist1-smile
        with Dissolve(0.2)
        show scientist2-unhappy at left
        show scientist1-neutral at right
        with Dissolve(0.2)

        scientist "Каа-ак ты это сделал?" #(Второй ученый)

        "Сказал другой учёный."

        anton "Просто повернул."
        scientist "Но ведь она не..."

        #(Экран почти полностью чернеет от краев, спрайты пропадают) #(Черный экран)
        hide scientist2-unhappy
        hide scientist1-neutral
        with Dissolve(1)
        scene black
        with Dissolve(3)
        scene lab
        with Dissolve(3)

        anton "Хей, так тут ничего не изменилось! Это та же самая лаборантская."

        "Сказал я, заглянув в открытую дверь."

        anton "Ну и что тут такого?"
        anton "Вы что, и в правду просто открыли дверь? Это шутка такая?"

        "Разочаровано протянул я."

        #(Эффект моргания, спрайт Расстроенный Павел, спрайт Расстроенный Второй ученый)
        #Пока не нашел но более менее сделал эффект моргания
        scene black
        with Dissolve(0.35)
        scene lab
        with Dissolve(0.35)
        scene black
        with Dissolve(0.35)
        scene lab
        with Dissolve(0.35)
        show scientist1-unhappy at left
        show scientist2-unhappy at right
        with Dissolve(0.3)
        #scene lab with ImageDissolve("eye-opening.png", 0.75, 15, reverse=False) 

        "Но разочаровано выглядели и учёные." #?

        scientist "Десять минут назад там был проход на неизвестную доселе науке землю!" #(Павел)
        scientist "Такой красочный пейзаж не сыщешь даже в эрмитаже!"
        scientist "Похоже, что-то пошло не так." #(Второй ученый)

        "Сказал пухленький учёный."
        
        #(Черный экран, спрайты пропадают)
        hide scientist2-unhappy
        hide scientist1-unhappy
        with Dissolve(1)
        scene black
        with Dissolve(3)
        #scene lab
        #with Dissolve(3)

        anton "Да... Нет тут никакого эрмитажа."

        "Проходя в комнату, заявил я."

        scientist "Погодите вы! Не заходите туда. Это все еще может быть опасно!"

        "Сказал второй ученый." #(Павел)

        anton "Да какая тут опасность."
        anton "Шутники хреновы. Перегрелись вы немного в своей лаборатории."
        anton "А ведь тут и вправду душновато."

        scientist "Я понимаю вашу категоричность, но все что мы говорим было взаправду. Прошу вас, выйдите из этой комнаты." #(Павел)
        
        "Он направился к Двери."
        
        scientist "Павел Львович, я бы не советовал..."

        pavel "Все хорошо, я знаю, что делаю."

        anton "Да что тут такого? Маленькая серая лаборантская. Неубранная кстати. Вам бы тут помыть все."

        #(спрайт Недовольный Павел)
        show scientist1-unhappy at center
        with Dissolve(0.4)
        
        pavel "Что вы такое говорите. Мы регулярно там убираемся."

        "Ответил учёный, заходя в комнату." #(Зайдите, посмотрите сами. Ну и пылища тут у вас.

        "Он явно собирался вывести отсюда меня, однако вскрик его коллеги и звук закрытия двери нарушили его планы." #Учёный
        return

image fantasy_anim:
        "images/scenes/fantasy_dark.jpg" with Dissolve(1.5)
        pause 1.5
        "images/scenes/fantasy_light.jpg" with Dissolve(1.5)
        pause 1.5
        repeat

#Кафе (студенческая столовая пока что заглушка 14-12-23 жду картинку)
image cafe:
    "scenes/cafe.jpg"

image physics-hall:
    "scenes/physics-hall.png"

image university-hall:
    "scenes/university-hall.png"

image kafedra_fiziki:
    "scenes/old-university-hall.png"

image lab:
    "scenes/lab.png"

# image eyes_opening:
#     contains:
#         'eyelid_upper'
#         align (.5,.5)
#         ease 1 yanchor 1.0 ypos .0
#     contains:
#         'eyelid_lower'
#         align (.5,.5)
#         ease 1 yanchor .0 ypos 1.0