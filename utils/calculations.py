'''
Simple calculations abstracted from the code to allow for easy updating
and fast referencing. 
'''
import math
import doctest

def translate_hr_sla(SLA, Rate):
    '''
    Calculate how many items are expected to arrive within the SLA timeframe
    Given we know the items arriving within a 1 hour period

    >>> translate_hr_sla(30, 60)
    30.0
    '''
    return SLA/60 * Rate

def calc_worker_throughput(SLA, AHT):
    '''
    Calculate how many tasks a worker can do within a given SLA period.

    Ie. Given the SLA period is 60 mins with an average handling time (AHT)
    of 20 mins the worker can be expected to complete 3 tasks in each SLA period

    >>> calc_worker_throughput(60, 20)
    3.0
    '''
    return SLA/AHT


def calc_workers_required(ArrivalRate, Throughput):
    '''
    Calculate the required workers to manage the amount of work arriving based on
    the amount of throughput each worker can achieve.
    Returns partial and whole worker counts

    >>> calc_workers_required(23, 10)
    (2.3, 3)
    '''
    partial_workers = ArrivalRate/Throughput
    whole_workers = math.ceil(partial_workers)
    return partial_workers, whole_workers

def calc_clear_queue(Work, Throughput):
    '''
    Calculate amount of workers required to clear the current queue
    
    >>> calc_clear_queue(60, 10)
    6.0
    '''
    return round(Work/Throughput, 2)

def calc_max_queue_len(Workers, Throughput, SLA):
    '''
    Calculate the maximum amount of queue items expected to process in SLA based on the amount of workers. 

    >>> calc_max_queue_len(10, 1, 30)
    (10, 20.0)
    '''
    per_sla = Workers * Throughput
    per_hr = per_sla/SLA * 60
    return per_sla, per_hr


doctest.testmod()