#!/bin/bash

# Remove ports from docker-compose.yml
cp docker-compose.yml .docker-compose.no-ports.yml
sed -i '/\(^\s*ports\:\)/d' .docker-compose.no-ports.yml
sed -i '/\(^\s*- \"[0-9]\{4\}\:[0-9]\{4\}\"\)/d' .docker-compose.no-ports.yml
