import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from io_utils import SafeFileOpen, safe_file_open
from decorators import time_measure, retry_handler

# Using the class SafeFileOpen
print("=== Test SafeFileOpen (class) ===")
with SafeFileOpen("data/shopping_behavior.csv") as f:
    conteudo = f.read()
    print(conteudo[:200])

print("\n=== Test safe_file_open (decorator) ===")
# Using decorator @contextmanager
with safe_file_open("data/shopping_behavior.csv") as f:
    lines = 0
    for linha in f:
        lines += 1
        if lines <= 3:
            print(linha.strip())
    print(f"Total de linhas: {lines}")

# Test decoradores
print("\n=== Test @time_measure ===")
@time_measure
def process_file():
    with safe_file_open("data/shopping_behavior.csv") as f:
        return len(f.readlines())

result = process_file()
print(f"Arquivo processado: {result} linhas")

print("\n=== Test @retry_handler ===")
attempt_count = 0

@retry_handler(retries=3, delay=0.75)
def unreliable_operation():
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise Exception("Simulated failure")
    return "Success!"

try:
    resultado = unreliable_operation()
    print(f"Resultado: {resultado}")
except Exception as e:
    print(f"Erro: {e}")
