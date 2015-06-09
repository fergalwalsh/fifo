import argparse
from multiprocessing import Process
from fifo import FifoWorker

parser = argparse.ArgumentParser(description='Fifo Worker')
parser.add_argument('module',
                    help='the python module to process tasks from')
parser.add_argument('--broker', dest='broker',
                    default='redis://localhost:6379/0',
                    help='the redis broker url')
parser.add_argument('--multi', dest='multi',
                    default=0,
                    type=int,
                    metavar='N',
                    help='start N workers')
args = parser.parse_args()


def main():
    worker = FifoWorker(args.broker, args.module)
    worker.run()

if __name__ == '__main__':
    if args.multi:
        print("multi: %s" % args.multi)
        for i in range(args.multi):
            Process(target=main).start()
    else:
        main()
