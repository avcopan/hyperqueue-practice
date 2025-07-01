import os
from pathlib import Path

from hyperqueue import Job, Client

HOME = Path(os.environ["HOME"])
HQ_PATH = HOME / ".hq-server" / "hq-current"

client = Client(HQ_PATH)

job = Job()

# Add a task that executes `ls` to the job
job.program(["./test.sh"])

# Submit the job
submitted = client.submit(job)

# Wait until the job completes
client.wait_for_jobs([submitted])
