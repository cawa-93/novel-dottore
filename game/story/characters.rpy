define GG = Character("player_name", dynamic=True)
define DT = Character(name=_("Дотторе"), image="dottore")

label day(label, time=3):
    scene bg black with fade

    image big_text = ParameterizedText(xalign=0.5, yalign=0.5, size=120)

    show big_text label with Dissolve(time)

    pause

    hide big_text with Dissolve(time/3)

    return