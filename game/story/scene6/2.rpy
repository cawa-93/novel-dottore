label scene6_2:


    show dottore lab test_tube

    DT "Втім, ніхто з попередніх пацієнтів не обирав ні голки, ні ножі, ні пилки. Всі чомусь вважать, що рідини менш… небезпечні та болючі."
    GG "…"
    GG "Що у пробірці?"
    show dottore lab smile 6
    DT "Радий, що тобі цікаво"
    DT "Це моя власна розробка. Я довго досліджував елеазар і дійшов висновку, що кожна лусочка містить у собі 90%% кальцію."
    show dottore lab smile 4
    DT "Кальцій це такий елемент, з якого складаються наші кістки, зуби та деякі інші тверді частини нашого тіла. Саме тому елеазар такий міцний і при розростанні не дозволяє суглобам нормально рухатись."
    DT "Отож я подумав, що якщо вивести кальцій з організму, то елеазар має зникнути сам собою. Ну знаєш, як зникають прищі з обличчя, якщо перестати їсти солодке."
    show dottore lab smile 5
    GG "…"
    GG "Це не зовсім так працює."
    DT "Можливо я не майстер аналогій, проте деякі речі мені краще знати."
    show dottore lab test_tube
    DT "Тому я введу тобі цю речовину в організм і ми подивимось, як поведе себе захворювання."

    menu:
        "Чи не стануть кістки крихкими?":
            $ False
        "Це боляче?":
            $ False

    DT "Побачимо. В будь-якому випадку, я цей препарат ще ні на кому не тестував."
    DT "Але впевнений, що все вийде. Не бачу жодної причини, чому б не мало вийти."
    GG "Скільки часу це займе?"
    DT "Кілька днів. Припускаю, через тиждень ми побачимо результат."

    "Ти сумніваєшся у методі, який тобі, ну нехай буде, пропонує Дотторе"

    DT "Давай починати."

    menu:
        "Прибрав руки від мене!":
            $ dotore_mad += 10
            pause

            show dottore smile:
                yalign 0.8
                zoom 1.08
            with move
            pause

            show dottore smile 3:
                yalign 0.6
                zoom 1.16
            with move
            pause

            show dottore smile 2:
                yalign 0.4
                zoom 1.24
            with move
            pause



        "Промовчати":
            $ dotore_mad -=10 

    show dottore ukol

    """
    Вчений бере зі столика скляний шприц, у який набирає невідому речовину з пробірки. Повільно, приділяючи цьому процесу максимальну увагу.
    Тобі страшно, але ти не можеш сказати жодного слова. Язик прилип до піднебіння та занімів, що є твоєю типовою реакцією на стресову ситуацію.
    """
    DT @ smile 3 "Потерпи трохи, можливо, буде трохи боляче. Не знаю, не тестував на собі."
    DT "Ось так."

    window hide
    with None
    show half_black 
    show ukol
    with dissolve

    """
    Ти відчуваєш легкий, майже безболісний укол у руку.
   
    Ніби не все так погано, як здавалось на перший погляд.
    
    Ти швидко оглядаєш себе, але нічого дивного не помічаєш. Елеазар не почав осипатись, шкіра не покрилась пухирями, руки не перетворились на мацаки абощо. Навіть нігті не відпали.
   
    Ти полегшено зітхаєш. Можливо, Дотторе помилився у своїх дослідженнях і нічого не станеться?

    Не те, що елеазар став тобі рідним, але лікувати його такими методами тобі не хотілось би.

    """

    GG "А що далі?"

    hide ukol 
    hide half_black
    with dissolve

    window auto

    DT "Очікуємо кілька днів, а потім будемо діяти за ситуацією. А поки поспи."

    """
    Ти хочеш заперечити, адже спати тобі зовсім не хочеться, але раптом відчуваєш, як втома охоплює тіло.
    
    Дивно, адже не пройшло і години після твого пробудження.    

    Ти мимоволі позіхаєш.
    """

    GG "Ти мені знову вколов…"

    show black with fade

    GG "…чому…"
    DT "Ось так, молодець."

    jump scene7_2