#!/bin/bash

# usage: ./serve.sh
# should be executed from the project directory

sudo darkhttpd ./out --timeout 5 --no-keepalive --port 80 --addr 127.0.0.1 --header 'Cache-Control: no-store'
