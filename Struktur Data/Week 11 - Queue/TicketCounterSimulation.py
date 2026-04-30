# Implementation of the main simulation class.
from custom_array import Array
from llistqueue import Queue
from people import TicketAgent, Passenger

class TicketCounterSimulation :
    # Create a simulation object.
    def __init__( self, numAgents, numSeconds, betweenTime, serviceTime ):
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numSeconds = numSeconds

        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array( numAgents )
        for i in range( numAgents ):
            self._theAgents[i] = TicketAgent(i+1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # Run the simulation using the parameters supplied earlier.
    def run( self ):
        for curTime in range(self._numSeconds + 1):
            self._handleArrival( curTime )
            self.handleBeginService( curTime )
            self.handleEndService( curTime )

    # Print the simulation results.
    def printResults( self ):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float( self._totalWaitTime ) / numServed
        print( "" )
        print( "Number of passengers served = ", numServed )
        print( "Number of passengers remaining in line = %d" %
               len(self._passengerQ) )
        print( "The average wait time was %4.2f seconds." % avgWait )

    # Handle the arrival of a new passenger.
    def _handleArrival( self, curTime ):
        import random
        if random.random() < self._arriveProb:
            passenger = Passenger( curTime )
            self._passengerQ.enqueue( passenger )
            self._numPassengers += 1

    # Handle the beginning of a service for a waiting passenger.
    def handleBeginService( self, curTime ):
        for i in range( len(self._theAgents) ):
            agent = self._theAgents[i]
            if not agent.is_busy() and not self._passengerQ.is_empty():
                passenger = self._passengerQ.dequeue()
                agent.set_busy()
                agent.set_passenger( passenger )
                agent.set_service_time( self._serviceTime, curTime )

    # Handle the end of a service for an agent.
    def handleEndService( self, curTime ):
        for i in range( len(self._theAgents) ):
            agent = self._theAgents[i]
            if agent.is_busy() and curTime >= agent.get_free_time():
                passenger = agent.get_passenger()
                wait_time = passenger.get_wait_time( curTime )
                self._totalWaitTime += wait_time
                agent.set_busy( False )
                agent.set_passenger( None )

# Test the Queue implementation
# if __name__ == "__main__":
    # values = Queue()
    # for i in range(16):
    #     if i % 3 == 0:
    #         values.enqueue(i)
    
    # print("Queue contents:", list(values))
    # print("Queue size:", len(values))   
    # values = Queue() 
    # for i in range(16):     
    #     if i % 3 == 0: 
    #         values.enqueue(i)     
    #     elif i % 4 == 0: 
    #         values.dequeue()
    # print("Queue contents:", list(values))
    # print("Queue size:", len(values))
