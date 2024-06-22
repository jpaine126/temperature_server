#!/usr/bin/env bash
#  build docker image

this_file=$( dirname $( realpath $0 ) )

project_root=$( dirname $this_file )

sudo docker build \
-f "${project_root}/server.Dockerfile" \
-t server \
"${project_root}"
