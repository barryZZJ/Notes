@echo off
git add .
git commit -m "%date:~0,10%_%time:~0,8%"
git pull
git push