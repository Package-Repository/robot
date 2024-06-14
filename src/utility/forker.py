#!/usr/bin/env python3

import subprocess
import signal
import os


class Forker:
    def __init__(self):
        self.processes = []

    def run_scripts(self, scripts):
        self.processes = [subprocess.Popen([script]) for script in scripts]

    def run_script(self, script: str):
        process = subprocess.Popen([script])
        self.processes.append(process)

    def terminate_processes(self):
        for process in self.processes:
            if process.poll() is None:
                process.kill()
        print("All child processes terminated.")


def signal_handler(forker):
    def handler(signum, frame):
        TERMINATE_SIGNAL_MSG = "Received signal to terminate. Cleaning up..."
        print(TERMINATE_SIGNAL_MSG)
        forker.terminate_processes()
        os._exit(0)
    return handler


if __name__ == "__main__":
    forker = Forker()
    forker.run_scripts([
        "server.py"
    ])
    signal.signal(signal.SIGINT, signal_handler(forker))
    signal.pause()
