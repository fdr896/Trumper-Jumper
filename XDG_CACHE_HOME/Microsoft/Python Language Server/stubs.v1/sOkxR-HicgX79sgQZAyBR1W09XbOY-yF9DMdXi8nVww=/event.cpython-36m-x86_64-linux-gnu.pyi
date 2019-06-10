pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
import builtins as _mod_builtins

def Event(type, **attributes):
    'Event(type, dict) -> EventType instance\nEvent(type, **attributes) -> EventType instance\ncreate a new event object'
    pass

EventType = _mod_builtins.Event
_PYGAME_C_API = _mod_builtins.PyCapsule()
__doc__ = 'pygame module for interacting with events and queues'
__file__ = '/home/fed/.local/lib/python3.6/site-packages/pygame/event.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pygame.event'
__package__ = 'pygame'
def clear(typelist):
    'clear() -> None\nclear(type) -> None\nclear(typelist) -> None\nremove all events from the queue'
    pass

def event_name(type):
    'event_name(type) -> string\nget the string name from and event id'
    return ''

def get(typelist):
    'get() -> Eventlist\nget(type) -> Eventlist\nget(typelist) -> Eventlist\nget events from the queue'
    pass

def get_blocked(type):
    'get_blocked(type) -> bool\ntest if a type of event is blocked from the queue'
    return True

def get_grab():
    'get_grab() -> bool\ntest if the program is sharing input devices'
    return True

def peek(typelist):
    'peek(type) -> bool\npeek(typelist) -> bool\ntest if event types are waiting on the queue'
    return True

def poll():
    'poll() -> EventType instance\nget a single event from the queue'
    pass

def post(Event):
    'post(Event) -> None\nplace a new event on the queue'
    pass

def pump():
    'pump() -> None\ninternally process pygame event handlers'
    pass

def set_allowed(typelist):
    'set_allowed(type) -> None\nset_allowed(typelist) -> None\nset_allowed(None) -> None\ncontrol which events are allowed on the queue'
    pass

def set_blocked(typelist):
    'set_blocked(type) -> None\nset_blocked(typelist) -> None\nset_blocked(None) -> None\ncontrol which events are allowed on the queue'
    pass

def set_grab(bool):
    'set_grab(bool) -> None\ncontrol the sharing of input devices with other applications'
    pass

def wait():
    'wait() -> EventType instance\nwait for a single event from the queue'
    pass

