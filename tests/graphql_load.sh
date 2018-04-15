#!/bin/bash
source ../venv/bin/activate
locust -f graphql_load.py --host=http://127.0.0.1:5000 --csv=graphql --no-reset-stats --no-web -n10 -c1 --num-request=10
deactivate
