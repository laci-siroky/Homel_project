music.play_melody("C5 B A G D F C C ", 120)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.pause(100)
    basic.show_string("Hello!")
basic.forever(on_forever)
