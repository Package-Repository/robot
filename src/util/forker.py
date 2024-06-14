#!/usr/bin/env python3

import subprocess
import signal
import os

def fork_processes(scripts):
    return [subprocess.Popen([script]) for script in scripts]

def terminate_processes(processes):
    for process in processes:
        if process.poll() is None:
            process.kill()
    print("All child processes terminated.")

def signal_handler(signum, frame):
    print("Received signal to terminate. Cleaning up...")
    terminate_processes(Forker.processes)
    os._exit(0)

class Forker:
    processes = []

    @staticmethod
    def run_scripts(scripts):
        Forker.processes = fork_processes(scripts)
        signal.signal(signal.SIGINT, signal_handler)
        for process in Forker.processes:
            process.wait()

if __name__ == "__main__":
    Forker.run_scripts([
        "unity_srv.py",
        "speak_srv.py",
        "ar_srv.py"
    ])
