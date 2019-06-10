pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
__doc__ = 'pygame module to work with the keyboard'
__file__ = '/home/fed/.local/lib/python3.6/site-packages/pygame/key.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pygame.key'
__package__ = 'pygame'
def get_focused():
    'get_focused() -> bool\ntrue if the display is receiving keyboard input from the system'
    return True

def get_mods():
    'get_mods() -> int\ndetermine which modifier keys are being held'
    return 1

def get_pressed():
    'get_pressed() -> bools\nget the state of all keyboard buttons'
    return True

def get_repeat():
    'get_repeat() -> (delay, interval)\nsee how held keys are repeated'
    return tuple()

def name(key):
    'name(key) -> string\nget the name of a key identifier'
    return ''

def set_mods(int):
    'set_mods(int) -> None\ntemporarily set which modifier keys are pressed'
    pass

def set_repeat(delay, interval):
    'set_repeat() -> None\nset_repeat(delay, interval) -> None\ncontrol how held keys are repeated'
    pass

