#!/bin/bash
set -o allexport; source .env; set +o allexport
scp $SSH:$FOLDER/config/$1 .
