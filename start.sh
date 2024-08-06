#!/bin/sh

# Loop until /python/plato.py is found
while [ ! -f /python/plato.py ]; do
  sleep 2
done
cd /python
python -m plato
