#!/usr/bin/env python
import subprocess 

bashCommand = "rabbitmq-server -detached"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

print 'Server started'
