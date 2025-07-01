import os
import time
import subprocess
from pathlib import Path

from hyperqueue import Job, Client
from hyperqueue.task.function import PythonEnv

def pixi_activation_hook() -> str:
    """Get pixi activation hook."""
    return subprocess.check_output(["pixi", "shell-hook"], text=True)

HOME = Path(os.environ["HOME"])
HQ_PATH = HOME / ".hq-server" / "hq-current"

py_env = PythonEnv(prologue=pixi_activation_hook())
client = Client(HQ_PATH, python_env=py_env)

job = Job()

def task1_fn():
    print("Task 1 running!")
    time.sleep(5)
    print("Task 1 done!")

def task2_fn():
    print("Task 2 running!")
    time.sleep(5)
    print("Task 2 done!")

# Add tasks
task1 = job.function(fn=task1_fn)
task2 = job.function(fn=task2_fn, deps=[task1])

# Submit the job
submitted = client.submit(job)

# Wait until the job completes
client.wait_for_jobs([submitted])
