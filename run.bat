@echo off
:: Navigate to project directory
cd C:\Users\KITS\PycharmProjects\ecommerceproject

:: Activate virtual environment
call C:\Users\KITS\PycharmProjects\ecommerceproject\venv\Scripts\activate.bat

:: Run your Python or pytest commands
:: pytest -m sanity testCases
pytest -m regression testCases
pause

