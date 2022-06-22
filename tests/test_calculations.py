import unittest
from utils.calculations import *

class TestCalculations(unittest.TestCase):

    def test_translate_hr_sla(self):
        sla = 30
        tasks_per_hr = 40
        expect = 20.0

        tasks_per_sla = translate_hr_sla(SLA=sla, Rate=tasks_per_hr)

        self.assertEqual(tasks_per_sla, expect, f"Should be {expect}")

    def test_calc_worker_throughput(self):
        sla = 60
        aht = 20
        expect = 3.0

        throughput = calc_worker_throughput(SLA=sla, AHT=aht)
        self.assertEqual(throughput, expect, f"Should be {expect}")

    def test_calc_workers_required(self):
        arrival_rate = 23
        throughput = 10

        part, whole = calc_workers_required(ArrivalRate=arrival_rate, Throughput=throughput)
        self.assertEqual(part, 2.3, 'Should be 2.3')
        self.assertEqual(whole, 3, 'Should be 3')

    def test_clear_queue(self):
        work = 60
        throughput = 10
        expect = 6.0

        self.assertEqual(calc_clear_queue(Work=work, Throughput=throughput), expect, f"Should be {expect}")

    def test_max_queue(self):
        workers = 10
        throughput = 1
        sla = 30
        
        per_sla, per_hr = calc_max_queue_len(Workers=workers, Throughput=throughput, SLA=sla)

        self.assertEqual(per_sla, 10, 'Should be 10')
        self.assertEqual(per_hr, 20.0, 'Should be 20.0')



if __name__ == '__main__':
    unittest.main()