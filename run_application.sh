#!/usr/bin/env bash
# Filename: run_application.sh
dir=$(/usr/bin/pwd)

cd $dir/frontend

start "react.sh"

cd ..
cd backend

start "django.sh"

start "worker.sh"

echo $$
