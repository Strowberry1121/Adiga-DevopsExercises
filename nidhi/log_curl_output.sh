#!/bin/bash

# Log the curl output into build_log.txt
curl $(minikube ip):31008 > /app/build_log.txt 2>&1
