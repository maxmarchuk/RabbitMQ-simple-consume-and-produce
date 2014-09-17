#!/usr/bin/env python
import subprocess 

command = "rabbitmqctl stop"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE) 

#Catch the output of the command for future usage
output = process.communicate()[0]

print 'Server stopped'
