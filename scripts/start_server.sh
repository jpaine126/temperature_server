#!/usr/bin/env bash
#  start django server

this_file=$( dirname $( realpath $0 ) )
project_root=$( dirname $this_file )

server_root="${project_root}/tutorial"
manage="${server_root}/manage.py"
echo $server_root
# python $manage runserver 0.0.0.0:8000

cd $server_root
gunicorn \
--log-level debug \
--timeout 90 \
-b "0.0.0.0:8000" \
tutorial.wsgi:application
