import json

from Elevator import Elevator


def read_json(filepath) -> dict:
    file = open(filepath)
    building = json.loads(file.read())
    file.close()
    return building


class Building:
    def __init__(self, filepath: str):
        self.building = read_json(filepath)
        self.elevators = self.init_elevators()

    def get_min_floor(self) -> int:
        """:returns lowest building floor"""
        return self.building["_minFloor"]

    def get_max_floor(self) -> int:
        """:returns highest building floor"""
        return self.building["_maxFloor"]

    def init_elevators(self) -> list:
        """:returns initialized list of elevators"""
        lst = []
        for i in range(len(self.building["_elevators"])):
            curr_elevator = self.building["_elevators"][i]
            lst.append(Elevator(curr_elevator))
        return lst

    def get_elevators(self):
        """:returns list of elevators"""
        return self.elevators
