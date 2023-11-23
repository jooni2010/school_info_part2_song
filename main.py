def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

music.set_volume(255)

def on_forever():
    pass
basic.forever(on_forever)
