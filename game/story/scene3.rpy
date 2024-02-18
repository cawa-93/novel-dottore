
define was_letter_send = False

label scene3:
  
    scene bg tavern
    with fade
    play music "№2_321220__ralexpdx__my-tavern-1.wav"

    pause

    scene bg tavern zoomed
    show tavernkeeper
    with  fade

    T "Вітаю! Займайте будь-який вільний стіл, більшість відвідувачів вже пообідали, тому місця вистачає."

    call scene3_tavern_menu
    

    T "За п’ять хвилим подам."

    call scene3_tavern_drinks
    show tavernkeeper happy

    T "Очікуйте."

    scene bg tavern table


    """
    Ти сідаєш за стіл на двох, який знаходиться на другому поверсі таверни, подалі від чужих очей та розмов.
    
    Дійсно, за кілька хвилин тобі приносять замовлення. Ти з радістю відмічаєш, що незнайома страва дуже смачна, тому ти замовляєш ще одну порцію, якою можна повільно насолоджуватись найближчу годину.
    
    Так як ніхто не бачить тебе, ти обережно підіймаєш рукав плаща та розглядаєш тверді лусочки, які знову з’явились під час загострення хвороби.
    """


    window hide
    with None
    show half_black 
    show hands tavern
    with dissolve
    pause


    """
    Пальці погано гнуться та тремтять, а рани під лусочками – болять так сильно, що хочеться плакати.
    
    Ти приречено чухаєш в одну нігтем і розчаровано розумієш, що нарости стали більш твердими у порівнянні з тими, якими ти їх пам'ятаєщ.

    Одна надія на те, що вчені з Академії дійсно знайшли ліки від цієї хвороби. Ти сподіваєшся, що лікування не займе багато часу, адже вдома тебе з нетерпінням чекає мама та маленький брат, якого потрібно щодня доглядати.

    Елеазар став для тебе справжнім покаранням.

    Ти більше не можеш досхочу гуляти зі своїми друзями, ходити з ними до Високого Озера на ночівлі та разом шукати сезонні ягоди в глибині лісу.

    Не можеш їсти улюблений падісаровий пудинг, адже після нього лусочки болять ще сильніше, а шкіра навколо них тріскає та свербить.

    Не можеш допомагати мамі по господарству так майстерно і швидко, як ще кілька років тому.

    Ти не хочеш стати тягарем для своєї родини і тому ти зараз тут – у місті Сумеру, щоб попросити одного з вчених Академії про допомогу.
    """

    DT "Вітаю!"

    pause
    hide hands tavern 
    hide half_black
    with dissolve

    window auto


    pause

    hide hand
    show dottore street 1
    

    GG "Ой!"

    "Ти так поринаєш у свої думки, що навіть не помічаєш, як до тебе підходить незнайомий чоловік у масці."
    
    "Яка цікава мода в цьому місті."


    DT "Не лякайся. У мене невелика перерва в роботі, тож я вирішив спуститись у трактир пообідати. Випадково побачив у тебе на руках елеазар і вирішив підійти."

    menu ():
        DT "Тут не зайнято?"

        "Прошу":
            $ False
        "Мій друг зараз прийде":
            DT "Хм… Дійсно? Тоді почекаю його разом з тобою, якщо ти не проти."

    # false_choice(["fff"])

    show dottore street hand 1
    DT "Хочеш фокус? Я вмію читати чужі думки."

    GG "Ніхто цього не вміє."

    DT "Що ж, готовий посперечатися на 1000 мори, що я все ж маю певні здібності."

    DT "Хм…"
    show dottore street 4

    DT "Ти живеш не у цьому місті, а подорожуєш здалеку?"

    DT "До тебе долетіла новина, що в Академії ось-ось знайдуть ліки від елеазару і ти хочеш стати піддослідною мишкою."

    GG "Мишкою?"

    GG "..."

    DT "Робота зобов’язує бути таким."

    show dottore street 2

    DT "Розслабся."

    DT "Мене звати Дотторе і це я шукаю ліки від елеазару. Маю в цьому напрямі деякий прогрес, тому зараз мені потрібні пацієнти, які готові допомогти у експериментах. Ти ж за цим тут?"
    
    
    """
    Ти збентежено кліпаєш очима та ствердно киваєш головою. Що це: удача, чи архонти намагаються пошвидше спекатись тебе?
    """

    window hide
    with fade

    """
    Дотторе на хвилину відходить і повертається вже з двома чашками в руках.
    """
    
    
    show half_black 
    show tee
    with dissolve

    pause
    hide tee 
    hide half_black
    with dissolve

    window auto

    show dottore street 1

    DT "Сподіваюсь, тобі сподобається. Це мій найкращий збір, тримаю для особливих гостей."

    "Ти обережно відсьорбуєш чай, який тобі подав Дотторе. Незважаючи на те, що він досить гарячий, напій тобі до смаку і ти продовжуєш його пити, періодично дмухаючи над поверхнею."
    show dottore street hand 3
    DT "Отже, розкажи мені, як давно ти хворієш?"


    menu:
        "Кілька місяців":
            DT "Недовго. Значить, є більше шансів, що ліки швидко подіють і ти через тиждень підеш додому."
        "Кілька років":
            DT "Добре, що ти тут. Обіцяю, я докладу всіх зусиль, щоб змінити твоє життя."

    DT "Пропоную надовго не відкладати і розпочати роботу вже сьогодні. Боюсь, час грає проти нас, тому треба розібратись з цим якнайшвидше."

    GG "Погоджуюсь. Можна поставити одне запитання?"

    show dottore street hand 2

    DT "Звісно."

    menu:
        "Це боляче?":
            DT "Скоріше так, аніж ні. Але обіцяю, що після того, як я з тобою попрацюю, хвороба тебе більше не турбуватиме."
        "Це довго?":
            DT "Якщо робити висновок з твоїх симптомів, я думаю, знадобиться кілька тижнів. Деяких пацієнтів я відпускав через кілька днів після початку лікування. "
        "Чи хтось вже вилікувався?":
            DT "Так. Принаймні, хвороба їх більше не хвилювала."

    show dottore street 2

    DT "Тепер моя черга питати. Елеазаром у родині хворієш тільки ти?"

    GG "Так. Брат та мама не заражені."

    show dottore street 1

    DT """
    Не був би я таким впевненим. Дуже часто діти хворіють разом, тільки у одного елеазар проявляється раніше, а у іншого – пізніше, іноді навіть через кілька років.
    """

    show dottore street 

    """
    
    Якщо симптомів ще нема, я радив би все одно перевірити його стан. Вилікувати елеазар до перших лусочок на тілі можливо одним щепленням, тоді як у твоєму випадку може знадобитись більше часу.
    
    Можемо відправити брату листа, щоб він прибув сюди і я його зміг оглянути. Якщо все буде добре – підете додому разом, або залишитесь ще на кілька днів.

    """

    show dottore street hand 1

    """

    В Сумеру скоро відбудеться свято Прийдення і я впевнений, що вам буде цікаво там побувати.
    
    Щороку на головній площі розгортається величезний ярмарок, приїжджають степовики, студенти влаштовують наукові шоу та проводять змагання.
    
    Буде купа смаколиків, сувенірів та цікавинок, тож я вважаю, що це буде чудове закінчення твого лікування.
    """

    show dottore street 1

    "Його слова звучать як щось неможливе. Ви з братом і мріяти не могли побувати на Прийденні, а цей чоловік ще й пропонує вирішити всі твої проблеми наче помахом магічної палички."

    GG "Що я маю дати взамін? У нас не так багато грошей, якщо казати відверто."

    DT street 2 "Тільки взяти участь у моєму експерименті. Це все." 

    GG "І все?"

    show dottore street 3

    DT "Так. Гроші на дослідження видає Академія, кімнатою та харчуванням вона також забезпечить."

    DT "Найкраща нагорода для лікаря – здоровий пацієнт."

    show dottore street 1

    menu: 
        "Ти вагаєшся. Що робити?"

        "Написати листа":
            $ was_letter_send = True
            jump scene4_variant1

        "Не писати листа":
            $ was_letter_send = False
            jump scene4_variant2


# TODO: ЗБЕРЕГАТИ НАЗВИ СТРАВ 
label scene3_tavern_menu:
    menu: 
        T "Чого бажаєте?"

        "Ароматні м’ясні кульки":
            return
        "Грибне асорті":
            return
        "Тропічний салат":
            return
        "Курча в маслі":
            return
        "Піту":
            return

label scene3_tavern_drinks:
    menu: 
        T "Що будете пити?"

        "Чай":
            return
        "Сік":
            return
        "Молоко":
            return
        "Вино":
            return
