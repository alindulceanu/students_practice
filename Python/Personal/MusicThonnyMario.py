from scamp import *

s = Session()

piano = s.new_part("piano")

text = "jjj fj o  3  641 4631 14 69 58 4 353"

for char in text:
    if char == " ":
        wait(0.05)
    elif char.isalnum():
        piano.play_note(ord(char) - 20, 1, 0.25)
    else:
        wait(0.2)
        piano.play_note(ord(char), 0.8, 0.06)
        wait(0.2)