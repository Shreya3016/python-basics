class Event:
    - events = []
    + events = {}
    
	def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location
    
	def add_event(self):
        - self.events.append(self)
        + if self.id not in self.events:
        +    self.events[self.id] = self
		
    - def get_all_events(self):
    +@classmethod
    -    return self.events
    
	+def get_all_events(cls):
    +    return cls.events.values()
    
	- def get_event(self, id):
    + @classmethod
    -    for event in self.events:
    
	+ def get_event(cls, id):
    -        if event.id == id:
    +    return cls.events.get(id, None)
    -            return event
    -    return None
