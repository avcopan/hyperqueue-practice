from hyperqueue import Job, Client

client = Client("/home/avcopan/.hq-server/hq-current")

job = Job()

# Add a task that executes `ls` to the job
job.program(["./test.sh"])

# Submit the job
submitted = client.submit(job)

# Wait until the job completes
client.wait_for_jobs([submitted])
