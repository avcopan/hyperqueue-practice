# hyperqueue-practice

## Installing HyperQueue

If you have `$HOME/bin` in your path, you can install the HyperQueue executable as follows:
```
wget https://github.com/It4innovations/hyperqueue/releases/download/v0.22.0/hq-v0.22.0-linux-x64.tar.gz
tar -zxvf hq-v0.22.0-linux-x64.tar.gz -C ~/bin
```

## Using HyperQueue

### Starting the Server

You can start the server using:
```
hq server start &
```

### Allocating a Queue

You can then add an allocation queue to the server as follows.
```
hq alloc add slurm --time-limit 1h -- --partition=<partition name> --mem=10G --ntasks=1
```
To check that the queue was successfully allocated, use the following.
```
hq alloc list
```

### Executing a Workflow

If you have started the server and allocated a queue, you are now ready to execute a
workflow with hyperqueue.
To get started, you can test out the examples:
1. [Simple](examples/0simple): A minimal workflow without dependencies
2. [Dependency](examples/1dependency): A minimal workflow with a dependency
