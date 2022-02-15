from typing import Any, List, Type
from concurrent.futures import ThreadPoolExecutor, as_completed
from nornir.plugins.runners import ThreadedRunner
from nornir.core.task import Task, AggregatedResult
from nornir.core.inventory import Host
from tqdm import tqdm
import pdb

class ProgressBarRunner(ThreadedRunner):
    """
    ProgressBarRunner runs the task over each host using threads.
    Prints a cute progress bar.
    Arguments:
        num_workers: number of threads to use
    """

    def run(self, task: Task, hosts: List[Host]) -> AggregatedResult:
        result = AggregatedResult(task.name)
        pdb.set_trace()
        with ThreadPoolExecutor(self.num_workers) as executor:
            executions = executor.map(task.copy().start, hosts)
            pdb.set_trace()
            for index, execution in enumerate(executions):
                result[hosts[index].name] = execution
        return result
