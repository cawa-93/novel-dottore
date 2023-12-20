define openeyes = ImageDissolve("imagedisolve openeyes.png", 2.0, 8, reverse=True)

label scene7_1:

    scene black

    DT "Агов! Ти мене чуєш? Аго-о-ов!"
    "Перше, що ти відчуваєш – пекельний біль у руках та ногах. Він схожий на біль опіків від вогню, з якими стикався чи не кожен житель лісу Сумеру."
    GG "Болить…"
    DT "Подивись на мене."
    DT "Відкрий очі."

    scene bg laboratory
    show dottore
    with openeyes

    DT "Я вже подумав, що ти помреш."
    "Ти розсіяно дивишся навколо."
    "Ти лежиш на підлозі на якомусь брудному матраці. Здається, до тебе тут вже побувало багато «пацієнтів» Дотторе, адже вся поверхня покрита багряними плямами."
    "Гидота"
    "Ти сіпаєш рукою і без здивування виявляєш, що тебе знову прив’язали, цього разу – до металевої труби, яка проходить вздовж стіни."
    DT "Пробач, але я не можу дозволити тобі розгулювати по лабораторії. У мене тут багато інструментів, до яких не повинні торкатись іншу люди."
    "В іншому, я зробив все, що планував. Весь елеазар знято, тож залишається лише наглядати за загоєнням."
    "Ти опускаєш очі і бачиш, що твої ноги обмотані бинтами, які дуже дивно пахнуть."
    "Руки теж в бинтах по лікоть і вже просякли кров’ю та іншими рідинами."
    GG "Хочу пити…"
    DT "Вода в мисці зліва від тебе. Суп там же, але він мабуть вже встиг охолонути. Відро з іншої сторони."
    DT "Я іду відпочивати і тобі раджу."
    DT "Кричати не має сенсу."
    DT "Завтра побачимось і подивимось на перші результати."
    "Дотторе встає і, наспівуючи якусь пісеньку, іде з підвалу, не забуваючи замкнути двері на ключ."

    scene bg laboratory

    "Ти обережно сідаєш і оглядаєш своє тіло. Вчений вирішив не завдавати собі зайвого клопоту і не надягнув на тебе навіть спідню білизну."
    "Страшенно болить. Тобі хочеться здерти з себе бинти, але ти вирішуєш цього не робити. Хто знає, яку коросту можна підхопити на цьому матраці."
    "Світло потрапляє до лабораторії лише крізь невелике віконце під стелею. Навіть якщо тебе не прив’язали б, пролізти у нього не вийшло."
    "Ти зітхаєш. Що робити?"

    $ tried_to_escape_counter = 0;

    menu:
        "Поїсти та відпочити":
            $ False
        "Спробувати звільнитись":
            $ tried_to_escape_counter += 1
            "Ти сідаєш зручніше і роздивляєшся кайданки, якими Дотторе прикував тебе до труби. Металева конструкція виглядає міцною та надійною і здається, без ключа їх не відкрити."
            "Ти намагаєшся висковзнути крізь кільце, що схопило тебе за набряклу кисть, проте нічого не виходить."

    "Ти їси холодний суп, який залишив тобі вчений. Що ж, це краще, ніж нічого."
    "Відставивши тарілку ти вкладаєшся на брудному матраці і провалюєшся у тривожний неглибокий сон."


    # jump scene8


    "TODO !!! dotore_mad: [dotore_mad]"
    "DEBUGG !!! dotore_mad: [dotore_mad]"
    "DEBUGG !!! dotore_mad: [dotore_mad]"
    "DEBUGG !!! dotore_mad: [dotore_mad]"