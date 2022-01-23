from pynput import keyboard

# The event listener will be running in this block

while True:
    with keyboard.Events() as events:
        # Block at most one second
        event = events.get(0.25)
        if event is None:
            pass  # print('You did not press a key within one second')
        else:
            print('Received event {}'.format(event))
