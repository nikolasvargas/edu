import curses

def run(stdsrc: 'curses._CursesWindow') -> int:
    while True:
        stdsrc.addstr(0, 0, 'hello')
        char = stdsrc.get_wch()
        break
    return 0


def main() -> int:
    return curses.wrapper(run)


if __name__ == '__main__':
    exit(main())
