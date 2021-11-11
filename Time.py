import Elevator
import CallForElevator


def time_for_call(elevator: Elevator, call: CallForElevator) -> float:
    """Returns the time it will take the elevator to finish this call"""
    calls_list = elevator.get_call_list()
    last_call = calls_list[-1]  # [len(calls_list) - 1]
    last_floor = last_call.get_dest()
    floors_to_travel = abs(last_floor - call.get_src) + abs(call.get_src - call.get_dest)

    total_time_for_call = 2 * (elevator.get_open_time() + elevator.get_close_time() + elevator.get_start_time() +
                               elevator.get_stop_time()) + (floors_to_travel * elevator.get_speed())
    return total_time_for_call


def get_new_call_time(elevator: Elevator, call: CallForElevator) -> float:
    """Returns the time it will take the elevator to finish all its calls (dependent on previously calculated)"""
    curr_time_to_finish = elevator.get_time_to_finish()
    total_time_for_call = time_for_call(elevator, call)
    return total_time_for_call + curr_time_to_finish


def call_falls_in_range(elevator: Elevator, call: CallForElevator) -> bool:
    """Returns boolean value to specify if a call should be added to the list of calls for this elevator
    (in regards to time differences)"""
    call_list_elev = elevator.get_call_list()
    potential_call_time = call.get_time()  # time of call of the query call
    last_call = call_list_elev[-1]  # [len(calls_list) - 1]
    last_call_time = last_call.get_time()  # time of the last call of the elevator

    floors_to_travel = abs(last_call.get_dest() - call.get_src())
    total_time_for_to_reach = (elevator.get_open_time() + elevator.get_close_time() + elevator.get_start_time() +
                               elevator.get_stop_time()) + (floors_to_travel * elevator.get_speed())

    return total_time_for_to_reach + last_call_time > potential_call_time
