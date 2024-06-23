#!/bin/bash

echo "reading_node.service: ## Starting ##" | systemd-cat -p info

install_location=__INSTALL_LOCATION__

source "${install_location}/.venv/bin/activate"

python "${install_location}/reading_node.py" -n office
