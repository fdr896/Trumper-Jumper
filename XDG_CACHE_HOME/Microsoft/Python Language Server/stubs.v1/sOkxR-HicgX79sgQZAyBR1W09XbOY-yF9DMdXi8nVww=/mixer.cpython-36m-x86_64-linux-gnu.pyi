pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
import builtins as _mod_builtins

def Channel(id):
    'Channel(id) -> Channel\nCreate a Channel object for controlling playback'
    pass

ChannelType = _mod_builtins.Channel
Sound = _mod_builtins.Sound
SoundType = _mod_builtins.Sound
_PYGAME_C_API = _mod_builtins.PyCapsule()
def __PYGAMEinit__():
    'auto initialize for mixer'
    pass

__doc__ = 'pygame module for loading and playing sounds'
__file__ = '/home/fed/.local/lib/python3.6/site-packages/pygame/mixer.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pygame.mixer'
__package__ = 'pygame'
def fadeout(time):
    'fadeout(time) -> None\nfade out the volume on all sounds before stopping'
    pass

def find_channel(force=False):
    'find_channel(force=False) -> Channel\nfind an unused channel'
    pass

def get_busy():
    'get_busy() -> bool\ntest if any sound is being mixed'
    return True

def get_init():
    'get_init() -> (frequency, format, channels)\ntest if the mixer is initialized'
    return tuple()

def get_num_channels():
    'get_num_channels() -> count\nget the total number of playback channels'
    pass

def init(frequency=22050, size=-16, channels=2, buffer=4096):
    'init(frequency=22050, size=-16, channels=2, buffer=4096) -> None\ninitialize the mixer module'
    pass

def pause():
    'pause() -> None\ntemporarily stop playback of all sound channels'
    pass

def pre_init(frequency=22050, size=-16, channels=2, buffersize=4096):
    'pre_init(frequency=22050, size=-16, channels=2, buffersize=4096) -> None\npreset the mixer init arguments'
    pass

def quit():
    'quit() -> None\nuninitialize the mixer'
    pass

def set_num_channels(count):
    'set_num_channels(count) -> None\nset the total number of playback channels'
    pass

def set_reserved(count):
    'set_reserved(count) -> None\nreserve channels from being automatically used'
    pass

def stop():
    'stop() -> None\nstop playback of all sound channels'
    pass

def unpause():
    'unpause() -> None\nresume paused playback of sound channels'
    pass

