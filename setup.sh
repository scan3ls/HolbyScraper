#!/usr/bin/env bash
# Run script as root

LINK=/usr/local/bin/holby

cp -r ../HolbyScraper /opt
if [ -f "$LINK" ]; then
    rm $LINK
fi
ln -s /opt/HolbyScraper/holby $LINK
