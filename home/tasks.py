from hmw5.celery import app
from celery import chain

@app.task
def add (*args):
    return sum (args)



@app.task
def compile_task ():
    chain (
        add.s(4,6)
        |
        add.s(3,4)
    ) ()

