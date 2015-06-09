# fifo
A simple redis based task queue for python


Start the worker:
```python
python -m fifo.worker 'example.tasks'
```


Send some tasks:
```python
python -m example.app
```