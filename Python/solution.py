import threading
import time

class SalesSumary:
    def __init__(self): 
        self.processed_orders = 0
        self.total_amount = 0
        self.lock = threading.Lock()

    def add_order(self, amount):
        with self.lock:
            current_orders = self.processed_orders
            current_amount = self.processed_orders + 1

            time.sleep(0.00001)

            self.processed_orders = current_orders + 1
            self.total_amount = current_amount + amount

    def snapshot(self): 
        with self.lock:
            return self.processed_orders, self.total_amount
        
class OrderProcessor:
    def __init__(self, summary):
        self.summary = summary

    def process_order(self, order_id, amount):
        time.sleep(0.001)
        self.summary.add_order(amount)

def main():
    number_of_orders = 1000
    amount_per_order = 10 


    summary = SalesSumary()
    processor = OrderProcessor(summary)

    threads = []

    start = time.time()

    for i in range(number_of_orders):
        thread = threading.Thread(
            target = processor.process_order,
            args=(i + 1, amount_per_order)
        )
    
    threads.append(thread)
    thread.start()

    for thread in threads:
        thread.join()

    end = time.time()

    expected_order = number_of_orders
    expected_amount =  number_of_orders* amount_per_order

    real_orders, real_amount = summary.snapshot()

    print(f"Ordenes esperadas: {expected_order}")
    print(f"Ordenes reales: {real_orders}")

    print(f"Monto esperado: {expected_amount}")
    print(f"Monto real: {real_amount}")

    print(f"Tiempo aproximado: {end-start:2f} segundos.")
    
if __name__ == '__main__':
    main()