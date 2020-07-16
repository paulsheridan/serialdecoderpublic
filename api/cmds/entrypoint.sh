#!/bin/bash

cd /opt/api

./cmds/wait-for-it.sh db:5432 -s -- printf "Database Successfully Started\n"

# Execute main run command
exec "$@"
exit
