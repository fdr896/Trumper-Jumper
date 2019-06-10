pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
def Event(type, **attributes):
    'Event(type, dict) -> EventType instance\nEvent(type, **attributes) -> EventType instance\ncreate a new event object'
    pass

__doc__ = "pygame.fastevent is a wrapper for Bob Pendleton's fastevent\nlibrary.  It provides fast events for use in multithreaded\nenvironments.  When using pygame.fastevent, you can not use\nany of the pump, wait, poll, post, get, peek, etc. functions\nfrom pygame.event, but you should use the Event objects.\n"
__file__ = '/home/fed/.local/lib/python3.6/site-packages/pygame/fastevent.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pygame.fastevent'
__package__ = 'pygame'
def event_name(type):
    'event_name(type) -> string\nget the string name from and event id'
    return ''

def get():
    'pygame.fastevent.get() -> list of Events\nget all events from the queue\n'
    return list()

def init():
    'pygame.fastevent.init() -> None\ninitialize pygame.fastevent.\n'
    pass

def poll():
    'pygame.fastevent.poll() -> Event\nget an available event\n\nReturns next event on queue. If there is no event waiting on the\nqueue, this will return an event with type NOEVENT.\n'
    pass

def post():
    "pygame.fastevent.post(Event) -> None\nplace an event on the queue\n\nThis will post your own event objects onto the event queue.\nYou can past any event type you want, but some care must be\ntaken. For example, if you post a MOUSEBUTTONDOWN event to the\nqueue, it is likely any code receiving the event will expect\nthe standard MOUSEBUTTONDOWN attributes to be available, like\n'pos' and 'button'.\n\nBecause pygame.fastevent.post() may have to wait for the queue\nto empty, you can get into a dead lock if you try to append an\nevent on to a full queue from the thread that processes events.\nFor that reason I do not recommend using this function in the\nmain thread of an SDL program.\n"
    pass

def pump():
    'pygame.fastevent.pump() -> None\nupdate the internal messages\n\nFor each frame of your game, you will need to make some sort\nof call to the event queue. This ensures your program can internally\ninteract with the rest of the operating system. If you are not using\nother event functions in your game, you should call pump() to allow\npygame to handle internal actions.\n\nThere are important things that must be dealt with internally in the\nevent queue. The main window may need to be repainted. Certain joysticks\nmust be polled for their values. If you fail to make a call to the event\nqueue for too long, the system may decide your program has locked up.\n'
    pass

def wait():
    "pygame.fastevent.wait() -> Event\nwait for an event\n\nReturns the current event on the queue. If there are no messages\nwaiting on the queue, this will not return until one is\navailable. Sometimes it is important to use this wait to get\nevents from the queue, it will allow your application to idle\nwhen the user isn't doing anything with it.\n"
    pass

