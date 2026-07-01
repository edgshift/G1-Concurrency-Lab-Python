import threading
import time

class SalesSummary:
    def __init__(self):
        self.processed_orders = 0
        self.total_amount =0 

    def add_order(self, amount): 
        # PROBLEMA: 
        # # Leer, calcular y escribir ocurre en varios pasos. 
        # # Varios hilos pueden interferir entre sí
        current_orders = self.processed_orders
        current_amount = self.total_amount

        time.sleep(0.00001)

        self.processed_orders = current_orders + 1
        self.total_amount = current_amount + amount

class OrderProcessor:
    def __init__(self, summary):
        self.summary = summary

    def process_oder(self, order_id, amount):
        time.sleep(0.001)
        self.summary.add_order(amount)

def main():
    number_of_orders = 1000
    amount_per_order = 10

    summary = SalesSummary()
    processor = OrderProcessor(summary)

    threads = []

    start = time.time()

    for i in range(number_of_orders):
        thread = threading.Thread(
            target=processor.process_oder,
            args=(i + 1, amount_per_order)
        )

        threads.append(thread)
        thread.start()

        for thread in threads:
            thread.join()

        end = time.time()

        expected_orders = number_of_orders
        expected_amount = number_of_orders * amount_per_order

        print(f"Ordenes esperadas: {expected_orders}")
        print(f"Ordenes reales: {summary.total_amount}")

        print(f"Monto esperado: {expected_amount}")
        print(f"Monto real:{summary.total_amount} ")

        print(f"Tiempo aproximado: {end-start:.2f} segundos.")

if __name__ == "__main__":
    main()        
