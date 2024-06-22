#!/usr/bin/env bash

this_file=$( dirname $( realpath $0 ) )
project_root=$( dirname $this_file )

server_root="${project_root}/tutorial"

cd $server_root

python3 manage.py makemigrations readings
python3 manage.py migrate
