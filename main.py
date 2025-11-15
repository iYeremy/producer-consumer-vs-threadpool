# main.py
import time
from src.controller.controller import Controller

def main():
    inicio = time.time()
    app = Controller()
    app.run()
    final = time.time()
    print("Tiempo total:", final - inicio)

if __name__ == "__main__":
    main()
