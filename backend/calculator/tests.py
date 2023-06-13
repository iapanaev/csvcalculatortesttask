import os
import tempfile
from django.test import TestCase
from .models import CalculatorTask, CalculatorResult
from .tasks import process_calculator_task

DATA = b"""col0;col1;col2;col3;col4;col5;col6;col7;col8;col9;col10;col11;col12;col13;col14;col15;col16;col17;col18;col19;col20
1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21
1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21
1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21
1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21
1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21
"""

class CalculatorTaskTest(TestCase):

    def test_it_should_write_results(self):
        file = tempfile.NamedTemporaryFile()
        file.write(DATA)
        file.flush()
        task = CalculatorTask.objects.create(filename=os.path.basename(file.name))
        self.assertEqual(task.status, CalculatorTask.Status.NEW)
        with self.settings(CSV_FILES_PATH=os.path.dirname(file.name)):
            process_calculator_task(task.pk)
        task.refresh_from_db()
        self.assertEqual(task.status, CalculatorTask.Status.FINISHED)
        results = CalculatorResult.objects.filter(task=task)
        self.assertEqual(len(results), 10)
        for index, number in enumerate([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]):
            self.assertEqual(results[index].column, number)
            self.assertEqual(results[index].result, number * 5)
        file.close()
