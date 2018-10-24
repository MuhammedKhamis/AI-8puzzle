from agent import Agent
from state import State
from manhatten import Manhatten
from euclidean import Euclidean
from agent import Agent
from state import State
from heapq import heappush, nsmallest

class AStar(Agent):

    def __init__(self, initial_arr, heuristic):
        self.__inital_state = State(initial_arr, None, heuristic)


    def search(self):
        states_heap = []
        heappush(states_heap, self.__inital_state)

        while len(states_heap):
            # break tie by FIFO criteria
            current_explored_state = nsmallest(states_heap, key=lambda x, y: x.cost < y.cost)
            if current_explored_state.is_goal():
                break

            if current_explored_state not in self.__vis:
                self.__vis.add(current_explored_state)
                self.expand()
