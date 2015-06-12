from fifo import FifoWorker


worker = FifoWorker('redis://localhost:6379/0', 'example.tasks')
worker.run()
