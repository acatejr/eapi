#!/bin/bash

docker exec -it eapiapp python commands.py load_wgew_raingages
docker exec -it eapiapp alembic upgrade head
docker exec -it eapiapp python commands.py load_wgew_raingages
docker exec -it eapiapp python commands.py load_srer_raingages
docker exec -it eapiapp python commands.py load_srer_precipevents
docker exec -it eapiapp python commands.py load_wgew_precipevents