#!/bin/bash

../manage.py dumpdata --indent=2 > ./everything.json
../manage.py dumpdata --indent=2 menu > ./admin_tools_menu.json
../manage.py dumpdata --indent=2 dashboard > ./admin_tools_dashboard.json
../manage.py dumpdata --indent=2 licenses > ./licenses.json
../manage.py dumpdata --indent=2 localboats > ./localboats.json
../manage.py dumpdata --indent=2 events > ./localboats_events.json
../manage.py dumpdata --indent=2 news > ./localboats_news.json
../manage.py dumpdata --indent=2 sale > ./localboats_sale.json
../manage.py dumpdata --indent=2 photologue > ./photologue.json
