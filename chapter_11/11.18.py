from threading import Lock, Thread


class Wife(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self, person):
        dec_savings(person, 50.0)


def main():
    person = ['name', ['savings', 100.0]]
    hubby = list(person)
    wifey = person[:]
    hubby[0] = 'joe'
    wifey[0] = 'jane'
    print hubby, wifey
    inc_savings(hubby, 100.0)
    wife = Wife()
    wife.run(wifey)
    print hubby, wifey


def sync(func):
    lock = Lock()

    def wrapper_func(p, s):
        lock.acquire()
        func(p, s)
        lock.release()
    return wrapper_func


@sync
def inc_savings(person, savings):
    person[1][1] += savings


@sync
def dec_savings(person, savings):
    person[1][1] -= savings


if __name__ == '__main__':
    main()
