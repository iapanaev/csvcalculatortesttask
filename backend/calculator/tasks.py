import os
import time
import pandas
from celery import shared_task
from django.conf import settings
from .models import CalculatorTask, CalculatorResult


@shared_task
def process_calculator_task(task_id):
    try:
        task = CalculatorTask.objects.get(pk=task_id)
    except CalculatorTask.DoesNotExist:
        return
    if task.status == CalculatorTask.Status.FINISHED:
        return
    filepath = os.path.join(settings.CSV_FILES_PATH, task.filename)
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        task.status = CalculatorTask.Status.FAILED
        task.save()
        return
    task.status = CalculatorTask.Status.RUNNING
    task.save()
    dataframe = pandas.read_csv(filepath, delimiter=';', header=0)
    dataframe.sum()
    for index, columnname in enumerate(dataframe.columns, start=1):
        if index % 2 == 0:
            result = CalculatorResult(task=task, column=index)
            result.result = dataframe[columnname].sum()
            result.save()
    task.status = CalculatorTask.Status.FINISHED
    task.save()
