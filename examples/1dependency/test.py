from hyperqueue import Job, Client

client = Client("/home/avcopan/.hq-server/hq-current")

job = Job()

# Add tasks
task1 = job.program(["./task1.sh"])
task2 = job.program(["./task2.sh"], deps=[task1])

# Submit the job
submitted = client.submit(job)

# Wait until the job completes
client.wait_for_jobs([submitted])
