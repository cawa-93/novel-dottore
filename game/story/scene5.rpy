image day marker = Text(_("День 1"), size=120)

transform screen_center:
    xalign .5
    yalign .5


label scene5:
    scene bg black

    show day marker at screen_center with Dissolve(3)

    pause

    hide day marker with dissolve



    "Ти прокидаєшся після глибокого сну. Голова болить так, що здається, її легше відрубати, аніж вилікувати."
    
    "Ти намагаєшся торкнутись лоба, але тобі щось заважає це зробити. Опустивши очі ти розумієш, що твої руки та ноги міцно прив’язані до медичного стільчика, який стоїть посеред кімнати."
    
    "Позаду щось шарудить, але ти не можеш сфокусуватись і подивитися, чи є хтось поруч із тобою."


    menu: 
        "Сидіти тихо і спробувати все роздивитись":
            "Ти обережно роздивляєшся приміщення з-під опущених вій. Поруч немає нічого, що могло би допомогти тобі звільнитись чи послати комусь запит про допомогу."

        "Спробувати звільнитись":
            "Ти прикладаєш немало сили, щоб розірвати шкіряні ремені, які утримують тебе на кріслі, проте вони досить міцні і всі твої зусилля виявляються марними."

        "Покликати на допомогу":
            GG "Агов? Тут є хтось?"
            GG "Допоможіть мені, будь ласка! Мене привели сюди обманом!"



    DT "О, хтось нарешті прокинувся?"







    "DEBUGG !!!"
    "DEBUGG !!!"
    "DEBUGG !!!"
    "DEBUGG !!!"