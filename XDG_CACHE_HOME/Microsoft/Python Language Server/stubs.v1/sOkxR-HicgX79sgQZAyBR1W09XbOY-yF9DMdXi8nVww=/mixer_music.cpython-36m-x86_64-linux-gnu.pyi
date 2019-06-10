pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
import builtins as _mod_builtins

_MUSIC_POINTER = _mod_builtins.PyCapsule()
_QUEUE_POINTER = _mod_builtins.PyCapsule()
__doc__ = 'pygame module for controlling streamed audio'
__file__ = '/home/fed/.local/lib/python3.6/site-packages/pygame/mixer_music.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pygame.mixer_music'
__package__ = 'pygame'
def fadeout(time):
    'fadeout(time) -> None\nstop music playback after fading out'
    pass

def get_busy():
    'get_busy() -> bool\ncheck if the music stream is playing'
    return True

def get_endevent():
    'get_endevent() -> type\nget the event a channel sends when playback stops'
    pass

def get_pos():
    'get_pos() -> time\nget the music play time'
    pass

def get_volume():
    'get_volume() -> value\nget the music volume'
    pass

def load(filename):
    'load(filename) -> None\nload(object) -> None\nLoad a music file for playback'
    pass

def pause():
    'pause() -> None\ntemporarily stop music playback'
    pass

def play(loops=0, start=0.0):
    'play(loops=0, start=0.0) -> None\nStart the playback of the music stream'
    pass

def queue(filename):
    'queue(filename) -> None\nqueue a music file to follow the current'
    pass

def rewind():
    'rewind() -> None\nrestart music'
    pass

def set_endevent(type):
    'set_endevent() -> None\nset_endevent(type) -> None\nhave the music send an event when playback stops'
    pass

def set_pos(pos):
    'set_pos(pos) -> None\nset position to play from'
    pass

def set_volume(value):
    'set_volume(value) -> None\nset the music volume'
    pass

def stop():
    'stop() -> None\nstop the music playback'
    pass

def unpause():
    'unpause() -> None\nresume paused music'
    pass

