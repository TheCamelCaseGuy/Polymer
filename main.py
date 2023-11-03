import polymer
import threading

runner = True
config = {"defaultWaitTime": 1}

def alwaysWait():
    while runner:
        polymer.Shell.wait(config["defaultWaitTime"])

def echo(parameters):
    print(" ".join(parameters[1:]))

threading.Thread(target=alwaysWait).start()

polymer.Shell.new("echo", echo)

# Your Code Here -->

polymer.Shell.start()
runner = False
