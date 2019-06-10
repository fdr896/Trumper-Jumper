pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
import builtins as _mod_builtins

class Font(_mod_builtins.object):
    'Font(filename, size) -> Font\nFont(object, size) -> Font\ncreate a new Font object from a file'
    __class__ = Font
    def __init__(self, filename, size):
        'Font(filename, size) -> Font\nFont(object, size) -> Font\ncreate a new Font object from a file'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_ascent(self):
        'get_ascent() -> int\nget the ascent of the font'
        return 1
    
    def get_bold(self):
        'get_bold() -> bool\ncheck if text will be rendered bold'
        return True
    
    def get_descent(self):
        'get_descent() -> int\nget the descent of the font'
        return 1
    
    def get_height(self):
        'get_height() -> int\nget the height of the font'
        return 1
    
    def get_italic(self):
        'get_italic() -> bool\ncheck if the text will be rendered italic'
        return True
    
    def get_linesize(self):
        'get_linesize() -> int\nget the line space of the font text'
        return 1
    
    def get_underline(self):
        'get_underline() -> bool\ncheck if text will be rendered with an underline'
        return True
    
    def metrics(self, text):
        'metrics(text) -> list\nGets the metrics for each character in the passed string.'
        return list()
    
    def render(self, text, antialias, color, background=None):
        'render(text, antialias, color, background=None) -> Surface\ndraw text on a new Surface'
        pass
    
    def set_bold(self, bool):
        'set_bold(bool) -> None\nenable fake rendering of bold text'
        pass
    
    def set_italic(self, bool):
        'set_italic(bool) -> None\nenable fake rendering of italic text'
        pass
    
    def set_underline(self, bool):
        'set_underline(bool) -> None\ncontrol if text is rendered with an underline'
        pass
    
    def size(self, text):
        'size(text) -> (width, height)\ndetermine the amount of space needed to render text'
        return tuple()
    

FontType = Font()
def SysFont(name, size, bold, italic, constructor):
    'pygame.font.SysFont(name, size, bold=False, italic=False, constructor=None) -> Font\n       create a pygame Font from system font resources\n\n       This will search the system fonts for the given font\n       name. You can also enable bold or italic styles, and\n       the appropriate system font will be selected if available.\n\n       This will always return a valid Font object, and will\n       fallback on the builtin pygame font if the given font\n       is not found.\n\n       Name can also be a comma separated list of names, in\n       which case set of names will be searched in order. Pygame\n       uses a small set of common font aliases, if the specific\n       font you ask for is not available, a reasonable alternative\n       may be used.\n\n       if optional contructor is provided, it must be a function with\n       signature constructor(fontpath, size, bold, italic) which returns\n       a Font instance. If None, a pygame.font.Font object is created.\n    '
    pass

_PYGAME_C_API = _mod_builtins.PyCapsule()
def __PYGAMEinit__():
    'auto initialize function for font'
    pass

__doc__ = 'pygame module for loading and rendering fonts'
__file__ = '/home/fed/.local/lib/python3.6/site-packages/pygame/font.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pygame.font'
__package__ = 'pygame'
def get_default_font():
    'get_default_font() -> string\nget the filename of the default font'
    return ''

def get_fonts():
    'pygame.font.get_fonts() -> list\n       get a list of system font names\n\n       Returns the list of all found system fonts. Note that\n       the names of the fonts will be all lowercase with spaces\n       removed. This is how pygame internally stores the font\n       names for matching.\n    '
    return list()

def get_init():
    'get_init() -> bool\ntrue if the font module is initialized'
    return True

def init():
    'init() -> None\ninitialize the font module'
    pass

def match_font(name, bold, italic):
    'pygame.font.match_font(name, bold=0, italic=0) -> name\n       find the filename for the named system font\n\n       This performs the same font search as the SysFont()\n       function, only it returns the path to the TTF file\n       that would be loaded. The font name can be a comma\n       separated list of font names to try.\n\n       If no match is found, None is returned.\n    '
    pass

def quit():
    'quit() -> None\nuninitialize the font module'
    pass

