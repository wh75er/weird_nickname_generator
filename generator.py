import os
import random
import sys, termios, tty

class Buffer:
    def __init__(self):
        self.buf = ["None"]
        self.pointer = 0
    def push(self, value):
        self.buf.append(value)
        self.pointer += 1
    def back(self):
        if self.pointer > 0:
            self.pointer -= 1
    def forward(self):
        if self.pointer < len(self.buf):
            self.pointer += 1
    def show(self):
        return self.buf[self.pointer]
    def showPrev(self):
        if self.pointer > 0:
            return self.buf[self.pointer-1]
        return "None"
    def showNext(self):
        if self.pointer < len(self.buf)-1:
            return self.buf[self.pointer+1]
        return "None"
    def last(self):
        if self.pointer == len(self.buf)-1:
            return True
        return False

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def getNickname(d, p):
    return random.choice(p).format(**{k:random.sample(v, 5) for k, v in d.items()})

def generate(d, p):
    buf = Buffer()
    while True:
        os.system("clear")
        print("Nickname:\n{}".format(buf.show()))
        print("\nPrevious: {}".format(buf.showPrev()))
        print("Next: {}".format(buf.showNext()))
        char = getch()
        if char == 'q':
            print("Exiting...")
            break
        if char == 'n':
            if buf.last():
                nickname = getNickname(d, p)
                buf.push(nickname)
            else:
                buf.forward()
        if char == 'p':
            buf.back()

if __name__ == "__main__":
    print("hello world")
    buf = Buffer()

    print("example {}".format(buf.show()))
