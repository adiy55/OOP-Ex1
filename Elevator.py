class Elevator:
    def __init__(self, dictionary):
        self._id = dictionary["_id"]
        self._speed = dictionary['_speed']
        self._minFloor = dictionary['_minFloor']
        self._maxFloor = dictionary['_maxFloor']
        self._closeTime = dictionary['_closeTime']
        self._openTime = dictionary['_openTime']
        self._startTime = dictionary['_startTime']
        self._stopTime = dictionary['_stopTime']
        self._norm_speed = 0

    def get_norm_speed(self):
        """:returns the normalized speed of the elevator"""
        return self._norm_speed

    def set_norm_speed(self, norm_speed):
        """
        sets the normalized speed of the elevator
        :param norm_speed: calculated normalized speed
        :return: none
        """
        self._norm_speed = norm_speed

    def get_id(self):
        """:return elevator ID"""
        return self._id

    def get_speed(self):
        """:return elevator speed"""
        return self._speed
