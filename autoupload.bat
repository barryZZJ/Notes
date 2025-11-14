NET SESSION >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
	echo Running with admin privileges
) ELSE (
	echo Running without admin privileges
	echo Requesting admin privileges...
	powershell Start-Process -Verb RunAs -FilePath "%0"
	exit /B
)
cd /d %~dp0
git add .
git commit -m "%date:~0,10%_%time:~0,8%"
git pull
git push
pause