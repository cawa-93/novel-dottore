label scene11_1:
    call day(_("День 17"))
    play music "<from 0 to 170>the end.mp3"
    scene bg laboratory
    show dottore lab angry 2
    with fade

    DT "Який же цей елеазар живучий! Його ліквідували разом з частинами тіла, а він почав рости на шиї і грудях."
    """
    Яка різниця, де він росте?
    """
    show dottore lab smile 10
    DT "Хм… Цікавий випадок."
    GG "Ти ненормальний!"
    show dottore lab smile 4
    DT "Мені вже це казали."
    GG "Відпусти мене. Хочу додому."
    DT smile 3 "Як же ти підеш додому, м-м-м?"
    show dottore lab smile 6

    menu:
        "ВІДПУСТИ!":
            $ False

    DT "Не кричи ти так."
    camera:
        blur 0
        linear 0.5 blur 30
        linear 1.0 blur 0

    GG "НЕ ТОРКАЙСЯ МЕНЕ!"

    show dottore lab angry
    DT "Тиша в лабораторії!"
    """
    У тебе більше немає сил терпіти біль та знущання Дотторе.
    
    Це неможливо. Ніхто не може витримати те, що чверить цей покидьок.
    
    Архонти, чому він взагалі існує?
    """
    show dottore lab
    DT "Будемо експериментувати далі. Не все в житті вдається з першого разу."

    camera:
        blur 0
        linear 0.5 blur 30
        linear 1.0 blur 0


    GG "НІ! ДОСИТЬ!"

    menu:
        "Закричати":
            play sound screem

    show dottore lab angry 2
    DT "Та замовкни ж ти!"

    if was_letter_send:
        call .with_letter
    else:
        call .without_letter

    if tried_to_escape_counter >= 2:
        jump .tried_to_escape
    else:
        jump .tried_to_rest




label .with_letter:
    show dottore lab smile 10
    DT "Сподіваюсь, твій брат буде себе вести набагато тихіше, аніж ти. Я не можу працювати в такій атмосфері!"
    GG "Брат?.."
    GG "Ні..."
    show dottore lab smile 9
    GG "Ти не можеш..."
    GG "Не чіпай його!"
    GG "Бо інакше я…"
    show dottore lab smile 4
    DT "І що ти зробиш?"
    return

label .without_letter:
    GG "Прибери свої руки від мене!"
    DT "Обов’язково. Тільки нас попереду чекає перевірка ще кількох гіпотез, тож готуйся."
    GG "…"
    GG "Я більше не можу."
    return

label .tried_to_escape:
    """
    Він не зупиниться. Не зупиниться доти, поки твоє і без того слабке дихання не зупиниться на його жахливій кушетці.
    
    Цей монстр робить з тобою все, що приходить в його збочений мозок.
    
    Сил терпіти ці катування більше нема.
    
    Потрібно щось зробити. Зламати всі його плани.
    
    …
    """
    hide dottore lab smile 4
    with dissolve
    """
    Дотторе як зазвичай відходить від тебе, щоб знайти потрібні йому медичні інструменти.
    
    Якщо щось робити, то зараз саме час.
    
    Зараз.
    """



    menu:
        "Сильно вкусити себе за язика":
            show blood 1:
                alpha 0.5

    camera:
        blur 0
        linear 0.5 blur 50
        linear 1.0 blur 0       

    """
    Знову біль.
    
    Твій друг останніх кількох… тижнів? Місяців? Років?
    """
    
    menu:
        "Сильно вкусити себе за язика":
            show blood 1:
                alpha 1
  
    camera:
        blur 0
        linear 0.5 blur 50
        linear 1.0 blur 0   

    """
    Ти відчуваєш металевий присмак крові, але цього все ще недостатньо.
    """
    menu:
        "Сильно вкусити себе за язика":
            hide blood 1
            show blood 2:
                alpha 0.5
    
    camera:
        blur 0
        linear 0.5 blur 50
        linear 1.0 blur 0   

    """
    Боляче так, що хочеться блювати.
    """
    menu:
        "Сильно вкусити себе за язика":
            show blood 2:
                alpha 1
    
    camera:
        blur 0
        linear 0.5 blur 50
        linear 1.0 blur 0   
    """
    Ти не маєш права навіть застогнати, щоб не привертати увагу цього покидька.
    """
    menu:
        "ВІДКУСИТИ ЯЗИКА":
            show blood 3:
                alpha 0.5
    """
    Кров ллється з твого рота на підборіддя, заляпуючи бинти на твоїх грудях та животі.
    """
    DT "Тобі цікаво, що я робитиму сьогодні?"
    """
    Вже нічого, тварюко.
    """
    menu:
        "ВІДКУСИТИ ЯЗИКА":
            show blood 3:
                alpha 1
    """
    Це виявляється важче, ніж тобі видавалось раніше.
    
    Краплі крові потрапляють тобі у горло, примушуючи закашлятись.
    """
    DT "Щурик сьогодні не в настрої розмовляти?"
    "Кров’ю залите все навколо. Хоча, можливо, так було і раніше?"
    show black:
        alpha 0.3
   
    show dottore lab angry
    DT "Гей? Що ти робиш?!"

    show black:
        alpha 0.6
    """
    Те, що потрібно було зробити у перший же день.
    """
    scene black with Dissolve(3)
    """
    Так добре.
    
    Нарешті.
    
    Свобода.
    """

    jump end


label .tried_to_rest:
    
    menu:
        "Засміятись":
            $ False

    camera:
        blur 0
        linear 0.5 blur 20
        linear 1.0 blur 0   
    
    show dottore lab smile 10
    DT "Ти чого?"
    
    menu:
        "Засміятись":
            $ False

    camera:
        blur 0
        linear 0.5 blur 30
        linear 1.0 blur 0   

    show dottore lab
    DT "…"
    """
    Ти перестаєш розуміти, де і з ким знаходишся.
    
    Це все нереально, не може бути реальним.
    
    В світі не повинно існувати таких, як Дотторе. Просто не може існувати.
    """
    menu:
        "Закричати":
            play sound screem

    camera:
        blur 0
        linear 0.5 blur 40
        linear 1.0 blur 0   
   
   
    show dottore lab smile 5
    DT "Де у мене лежить заспокійливе?"
    GG "Ненавиджу тебе!"
    GG "НЕНАВИДЖУ!"
    """
    Відчуття нереальності наростає з кожною секундою. І чи не вперше воно рятує, а не лякає тебе.
    """
    GG "Чому я тут?"
    show dottore lab smile 4
    DT "Для лікування елеазару."
    menu:
        "Засміятись":
            $ False
    
    camera:
        blur 0
        linear 0.5 blur 50
        linear 1.0 blur 0
    
    GG "Я не хворію."
    GG "…я..."
    GG "…де я..."
    show dottore lab smile 8
    DT "…"
    DT "І цей пацієнт не витримав."
    DT "Так і запишемо."
    GG "…я лікуюсь?.."
    camera:
        blur 0
        linear 0.5 blur 50
        linear 1.0 blur 0
    GG "Чому?"
    DT "Втім, не важливо. Отже, сьогодні у нас за планом наступна схема…"
    show dottore lab smile 9
    menu:
        "Засміятись":
            $ False
   
    show dottore lab smile 7
    """
    Тобі все одно, хто ця людина і що вона робитиме.
    
    Тобі все одно, один він, чи таких псевдовчених багато.
    
    Тобі все одно, де ти.
    
    Тобі все одно, хто ти.
    
    
    Ти… хто ти?
    """
    GG "Хто я?"
    show dottore lab smile 4
    DT "Просто ще один мій пацієнт."
    scene black with Dissolve(3)


    jump end
