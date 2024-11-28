#!/bin/sh
cd "$(dirname "$0")" || exit
git add .
git commit -m "auto upload by shell"
git pull
git push