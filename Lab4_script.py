#!/usr/bin/python3

import os
import sys
import time
from typing import io
from typing import List
from time import sleep
from pathlib import PosixPath


def MainProcess(text: str, number_processes: int, number_iterations: int, log: io) -> None:
	child_pids: List[int] = []
	for i in range(1, number_processes + 1):
		pid = os.fork()
		if (pid != 0):
			child_pids.append(pid)
			child, _ = os.waitpid(0, os.WNOHANG)
			if child != 0:
				print(f'child with pid={child} exited with code={code}. parent with pid id={os.getpid()} exited')
				exit(2)
		else:
			parent_pid = os.getppid()
			parent_path = PosixPath(f'/proc/{parent_pid}')
			for j in range(number_iterations * i):
				if not parent_path.exists():
					print(f'parent with pid={parent_pid} exited. child with pid={os.getpid()} exited')
					exit(1)
				print(f'process = {i}\tnumber_iteration = {j}\ttext = {text}', file=log)
				sleep(1)
			exit(0)

	while True:
		child, code = os.waitpid(0, os.WNOHANG)
		if child != 0:
			print(f'child with pid={child} exited with code={code}. parent with pid id={os.getpid()} exited')
			exit(2)


def main():
	if len(sys.argv) < 4:
		print("Wrong arguments entered or the number of them is incorrect!")
		return
	log = open("log.txt", "w")
	text = sys.argv[1]
	number_processes  = int(sys.argv[2])
	number_iterations = int(sys.argv[3])
	MainProcess(text, number_processes, number_iterations, log)


if __name__ == "__main__":
	main()
