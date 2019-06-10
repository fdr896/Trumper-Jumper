pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
import _freetype as _mod__freetype
import builtins as _mod_builtins

BBOX_EXACT = 0
BBOX_EXACT_GRIDFIT = 1
BBOX_PIXEL = 2
BBOX_PIXEL_GRIDFIT = 3
Font = _mod__freetype.Font
STYLE_DEFAULT = 255
STYLE_NORMAL = 0
STYLE_OBLIQUE = 2
STYLE_STRONG = 1
STYLE_UNDERLINE = 4
STYLE_WIDE = 8
_PYGAME_C_API = _mod_builtins.PyCapsule()
def __PYGAMEinit__():
    'auto initialize function for _freetype'
    pass

__doc__ = 'Enhanced pygame module for loading and rendering computer fonts'
__file__ = '/home/fed/.local/lib/python3.6/site-packages/pygame/_freetype.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pygame._freetype'
__package__ = 'pygame'
def get_cache_size():
    'get_cache_size() -> long\nReturn the glyph case size'
    return 1

def get_default_font():
    'get_default_font() -> string\nGet the filename of the default font'
    return ''

def get_default_resolution():
    'get_default_resolution() -> long\nReturn the default pixel size in dots per inch'
    return 1

def get_error():
    'get_error() -> str\nReturn the latest FreeType error'
    return ''

def get_version():
    'get_version() -> (int, int, int)\nReturn the FreeType version'
    return tuple()

def init(cache_size=64, resolution=72):
    'init(cache_size=64, resolution=72)\nInitialize the underlying FreeType library.'
    pass

def quit():
    'quit()\nShut down the underlying FreeType library.'
    pass

def set_default_resolution(resolution=None):
    'set_default_resolution([resolution])\nSet the default pixel size in dots per inch for the module'
    pass

def was_init():
    'was_init() -> bool\nReturn whether the the FreeType library is initialized.'
    return True

