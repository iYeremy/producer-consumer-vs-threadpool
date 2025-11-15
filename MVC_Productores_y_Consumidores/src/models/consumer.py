import time, random, queue
from src.models.shared_queue import buffer

class Consumer:
    def __init__(self, cid):
        self.id = cid

    def consume(self):
        eaten = []
        """igual que producter se usara una estructura de datos 
        para almacenar lo comido"""

        while True:
            try:
                item = buffer.get(timeout=2)
            except queue.Empty:
                break

            eaten.append(item)
            time.sleep(random.uniform(0.2, 0.4))
            buffer.task_done()

        return eaten
