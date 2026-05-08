@echo off
echo ============================================================
echo  CodeMemory - Servidor Web
echo ============================================================
echo.
echo  Verificando dependencias...
python -m pip install -q -r requirements.txt

echo.
echo  Iniciando servidor...
echo  Acesse: http://localhost:5000
echo.
python app.py
pause
