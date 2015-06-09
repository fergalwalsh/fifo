from fifo import FifoClient

fifo = FifoClient('redis://localhost:6379/0')

# queue up a single task
task_id = fifo.queue_task('example.tasks.multiply', (6, 7),
                          max_wait=2, result_timeout=30)

# wait for result for at most 5s
result = fifo.wait(task_id, timeout=5)
print(task_id, result['body'])


# queue up many tasks in one call
tasks_args = [(x - 1, x) for x in xrange(10)]
task_ids = fifo.queue_tasks('example.tasks.multiply', tasks_args,
                            max_wait=30, result_timeout=30)

# wait for all the results for at most 5s
results = fifo.wait_for_group(task_ids, timeout=5)
for task_id, result in results.items():
    print(task_id, result['status'], result['body'])


# queue up a single task that will fail
task_id = fifo.queue_task('example.tasks.buggy', None,
                          max_wait=2, result_timeout=30)

# wait for result for at most 5s
result = fifo.wait(task_id, timeout=5)
print(task_id, result['status'], result['body'])


# queue up a single task
task_id = fifo.queue_task('example.tasks.multiply', (6, 7),
                          max_wait=2, result_timeout=0)
