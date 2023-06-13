from django.db import models


class CalculatorTask(models.Model):
    class Status(models.IntegerChoices):
        NEW = 0
        RUNNING = 1
        FINISHED = 2
        FAILED = 3

    filename = models.CharField(max_length=255)
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.NEW,
        db_index=True
    )


class CalculatorResult(models.Model):
    task = models.ForeignKey(
        CalculatorTask,
        related_name='results',
        on_delete=models.CASCADE
    )
    column = models.IntegerField()
    result = models.IntegerField()
