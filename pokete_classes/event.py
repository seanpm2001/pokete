import logging
"""Contains event var"""


class Event:
    """Event class to enable dependency injection
    ARGS:
        _ev: Initial char"""

    def __init__(self, event=""):
        self._ev = event
        self.emit_fn = None

    def get(self):
        """Getter
        RETURNS:
            Current char"""
        return self._ev

    def set(self, event):
        """Setter
        ARGS:
            _ev: New char"""
        self._ev = event
        self.emit_fn()

    def clear(self):
        """Clears the event"""
        self._ev = ""

    def set_emit_fn(self, emit_fn):
        self.emit_fn = emit_fn


_ev = Event()
