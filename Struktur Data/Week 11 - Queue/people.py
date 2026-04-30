# Classes for ticket counter simulation participants.
class Passenger:
    def __init__(self, arrival_time):
        """Create a passenger who arrives at arrival_time."""
        self._arrival_time = arrival_time
        self._service_time = 0

    def get_arrival_time(self):
        """Return the arrival time of the passenger."""
        return self._arrival_time

    def get_wait_time(self, current_time):
        """Return the wait time for the passenger."""
        return current_time - self._arrival_time

    def set_service_time(self, service_time):
        """Set the service time for the passenger."""
        self._service_time = service_time

    def get_service_time(self):
        """Return the service time for the passenger."""
        return self._service_time


class TicketAgent:
    def __init__(self, agent_id):
        """Create a ticket agent with the given agent_id."""
        self._agent_id = agent_id
        self._is_busy = False
        self._time_free = 0
        self._current_passenger = None

    def get_id(self):
        """Return the agent's id."""
        return self._agent_id

    def is_busy(self):
        """Return True if the agent is currently busy."""
        return self._is_busy

    def set_busy(self, busy=True):
        """Set the agent's busy status."""
        self._is_busy = busy

    def set_service_time(self, service_time, current_time):
        """Set when the agent will be free."""
        self._time_free = current_time + service_time

    def get_free_time(self):
        """Return the time when the agent will be free."""
        return self._time_free

    def set_passenger(self, passenger):
        """Set the current passenger being served."""
        self._current_passenger = passenger

    def get_passenger(self):
        """Return the current passenger being served."""
        return self._current_passenger
