from flask import request, jsonify
from . import events
from .models import Event
+import uuid
+
+@events.route('/<int:id>', methods=['DELETE'])
+def delete_event(id):
+    event = Event.get_event(id)
+    if event:
+        Event.events.remove(event)
+        return jsonify({'message': 'Event deleted'})
+    return ('Event not found', 404)

@events.route('/', methods=['GET'])
def get_events():
    events = Event.get_all_events()
    return jsonify({'events': [event.to_dict() for event in events]})
@events.route('/<int:id>', methods=['GET'])
def get_event(id):
    event = Event.get_event(id)
    return jsonify(event.to_dict()) if event else ('Event not found')

- @events.route('/', methods=['PST'])
+ @events.route('/', methods=['POST'])
def add_event():
-   id = len(Event.events) + 1
+    id = str(uuid.uuid4()) if Event.events else 1
+    if not request.json or not 'name' in request.json or not 'location' in request.json:
+        return jsonify({'error': 'Missing mandatory fields: name and/or location'}), 400
    name = request.json.get('name')
    location = request.json.get('location')
    event = Event(id, name, location)
-    event.add_event()
+    Event.add_event(event)
    return jsonify({'message': 'Event added', 'event': event.to_dict()}), 201
