#!/usr/bin/env bash

this_folder=$( dirname $( realpath $0 ) )

# setup installation location
install_location=/home/jpaine/test/

#remove from systemctl
sudo systemctl stop reading_node
sudo systemctl disable reading_node

sudo rm "/etc/systemd/system/reading_node.service" 

sudo systemctl daemon-reload

# clean up
sudo rm /usr/local/bin/reading_node.sh
rm -rf "${install_location}"
