#!/usr/bin/python3

import os
import sys
import threading
from time import sleep


def MainProcess(text: str, number_processes: int, number_iterations: int) -> None:
    pid = None
    for i in range(number_processes):
        pid = os.fork()
        if pid == 0:
            for j in range(number_iterations):
                sleep(number_iterations * j)
                lock = threading.Lock()
                with lock:
                    print(text, j * i)

    if pid != 0:
        p, _ = os.waitpid(-1, 0)
        while p:
            try:
                p, _ = os.waitpid(-1, 0)
            except ChildProcessError:
                return


def main():
    if len(sys.argv) < 4:
        print("Wrong arguments entered or the number of them is incorrect!")
        return
    text = sys.argv[1]
    number_processes  = int(sys.argv[2])
    number_iterations = int(sys.argv[3])
    MainProcess(text, number_processes, number_iterations)


if __name__ == '__main__':
    main()
