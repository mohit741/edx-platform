#!/bin/bash
cd /edx/app/edxapp/edx-platform/
source /edx/app/edxapp/edxapp_env
python manage.py lms crontab run  902a0ccde02d36d2f2e31650cc80767a
python manage.py lms update_index
