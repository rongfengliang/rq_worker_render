#!/bin/bash
set -e
nohup  python app.py & 
rq worker-pool -n 2 -u $REDIS_URL beijing
