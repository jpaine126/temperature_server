#!/usr/bin/env bash

this_folder=$( dirname $( realpath $0 ) )

# setup installation location
install_location=/home/jpaine/test/

mkdir -p $install_location

cp -r . $install_location

python -m venv "${install_location}/.venv"
source "${install_location}/.venv/bin/activate"
pip install -r "${install_location}/requirements.txt"

sed -i "s/__INSTALL_LOCATION__/${install_location}/g" "${install_location}/reading_node.sh"

# setup executable
cp "${this_folder}/reading_node.sh" /usr/local/bin/
chmod +x /usr/local/bin/reading_node.sh

# setup systemd files
sudo cp "${this_folder}/reading_node.service" /etc/systemd/system/
sudo chmod 640 /etc/systemd/system/reading_node.service
sudo systemctl daemon-reload
sudo systemctl enable reading_node
sudo systemctl start reading_node
