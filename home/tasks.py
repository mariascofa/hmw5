from hmw5.celery import app
from celery import chain, shared_task

@shared_task
def add (*args):
    return sum (args)



@shared_task
def compile_task ():
    chain (
        add.s(4,6)
        |
        add.s(3,4)
    ) ()

