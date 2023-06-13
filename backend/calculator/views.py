from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CalculatorTask
from .serializers import CalculatorTaskSerializer
from .tasks import process_calculator_task


class CalculatorTaskViewSet(
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = CalculatorTask.objects.all().prefetch_related('results')
    serializer_class = CalculatorTaskSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        process_calculator_task.delay(serializer.instance.pk)

    @action(detail=False)
    def running_tasks_count(self, request):
        running = CalculatorTask.objects.filter(
            status=CalculatorTask.Status.RUNNING
        ).count()
        queued = CalculatorTask.objects.filter(
            status=CalculatorTask.Status.NEW
        ).count()
        return Response({
            'running': running,
            'queued': queued
        })
