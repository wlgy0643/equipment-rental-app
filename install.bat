@echo off
cd /d "%~dp0"
python --version >nul 2>&1
if errorlevel 1 goto no_python
if not exist ".venv\Scripts\python.exe" python -m venv .venv
if not exist ".venv\Scripts\python.exe" goto failed
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto failed
echo Installation complete. Double-click run.bat.
pause
exit /b 0
:no_python
echo Python was not found. Install Python and enable "Add python.exe to PATH".
pause
exit /b 1
:failed
echo Installation failed. Check the error above and your internet connection.
pause
exit /b 1
