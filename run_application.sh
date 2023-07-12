#!/usr/bin/env bash
# Filename: run_application.sh
dir=$(/usr/bin/pwd)

cd $dir/backend

start "worker.sh"

echo $$
