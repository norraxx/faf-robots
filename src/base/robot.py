from typing import Iterable

from utils.db import db_con


class Base:
    """
    Base for robots, defines interface, first implement `get_data`, then `process_data`, and run `run()`
    """
    def __init__(self):
        self.db_con = db_con

    def get_data(self) -> Iterable:
        raise NotImplementedError()

    def process_data(self, data) -> None:
        raise NotImplementedError()

    def run(self):
        for row in self.get_data():
            self.process_data(row)
