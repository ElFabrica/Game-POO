#!/bin/bash
echo "============================================================"
echo "  CodeMemory - Servidor Web"
echo "============================================================"
echo ""
echo "  Verificando dependencias..."
python3 -m pip install -q -r requirements.txt

echo ""
echo "  Iniciando servidor..."
echo "  Acesse: http://localhost:5000"
echo ""
python3 app.py
