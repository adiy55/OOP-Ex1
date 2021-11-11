class Elevator:
    def __init__(self, dict):
        self._id = dict["_id"]
        self._speed = dict['_speed']
        self._minFloor = dict['_minFloor']
        self._maxFloor = dict['_maxFloor']
        self._closeTime = dict['_closeTime']
        self._openTime = dict['_openTime']
        self._startTime = dict['_startTime']
        self._stopTime = dict['_stopTime']

        self._callList = []  # calls for elevator
        self._timeToFinishAllCalls = 0

    def get_time_to_finish(self):
        return self._timeToFinishAllCalls

    def get_call_list(self):
        return self._callList

    def get_id(self):
        return self._id

    def get_speed(self):
        return self._speed

    def get_min_floor(self):
        return self._minFloor

    def get_max_floor(self):
        return self._maxFloor

    def get_close_time(self):
        return self._closeTime

    def get_open_time(self):
        return self._openTime

    def get_start_time(self):
        return self._startTime

    def get_stop_time(self):
        return self._stopTime
