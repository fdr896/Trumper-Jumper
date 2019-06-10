pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
__doc__ = 'pygame module to work with the mouse'
__file__ = '/home/fed/.local/lib/python3.6/site-packages/pygame/mouse.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pygame.mouse'
__package__ = 'pygame'
def get_cursor():
    'get_cursor() -> (size, hotspot, xormasks, andmasks)\nget the image for the system mouse cursor'
    return tuple()

def get_focused():
    'get_focused() -> bool\ncheck if the display is receiving mouse input'
    return True

def get_pos():
    'get_pos() -> (x, y)\nget the mouse cursor position'
    return tuple()

def get_pressed():
    'get_pressed() -> (button1, button2, button3)\nget the state of the mouse buttons'
    return tuple()

def get_rel():
    'get_rel() -> (x, y)\nget the amount of mouse movement'
    return tuple()

def set_cursor(size, hotspot, xormasks, andmasks):
    'set_cursor(size, hotspot, xormasks, andmasks) -> None\nset the image for the system mouse cursor'
    pass

def set_pos(x=None, y=None):
    'set_pos([x, y]) -> None\nset the mouse cursor position'
    pass

def set_visible(bool):
    'set_visible(bool) -> bool\nhide or show the mouse cursor'
    return True

