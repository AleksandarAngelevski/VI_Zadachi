import bisect
from enum import Enum
"""
Defining a class for the problem structure that we will solve with a search.
The Problem class is an abstract class from which we make inheritance to define the basic
characteristics of every problem we want to solve
"""


class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        """Given a state, return a dictionary of {action : state} pairs reachable
        from this state. If there are many successors, consider an iterator
        that yields the successors one at a time, rather than building them
        all at once.

        :param state: given state
        :return:  dictionary of {action : state} pairs reachable
                  from this stateSnake
        :rtype: dict
        """
        raise NotImplementedError

    def actions(self, state):
        """Given a state, return a list of all actions possible
        from that state

        :param state: given state
        :return: list of actions
        :rtype: list
        """
        raise NotImplementedError

    def result(self, state, action):
        """Given a state and action, return the resulting state

        :param state: given state
        :param action: given action
        :return: resulting state
        """
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares
        the state to self.goal, as specified in the constructor. Implement
        this method if checking against a single self.goal is not enough.

        :param state: given state
        :return: is the given state a goal state
        :rtype: bool
        """
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from state1
        via action, assuming cost c to get up to state1. If the problem is such
        that the path doesn't matter, this function will only look at state2.
        If the path does matter, it will consider c and maybe state1 and action.
        The default method costs 1 for every step in the path.

        :param c: cost of the path to get up to state1
        :param state1: given current state
        :param action: action that needs to be done
        :param state2: state to arrive to
        :return: cost of the path after executing the action
        :rtype: float
        """
        return c + 1

    def value(self):
        """For optimization problems, each state has a value.
        Hill-climbing and related algorithms try to maximize this value.

        :return: state value
        :rtype: float
        """
        raise NotImplementedError


"""
Definition of the class for node structure of the search.
The class Node is not inherited
"""


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create node from the search tree,  obtained from the parent by
        taking the action

        :param state: current state
        :param parent: parent state
        :param action: action
        :param path_cost: path cost
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0  # search depth
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node.

        :param problem: given problem
        :return: list of available nodes in one step
        :rtype: list(Node)
        """
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """Return a child node from this node

        :param problem: given problem
        :param action: given action
        :return: available node  according to the given action
        :rtype: Node
        """
        next_state = problem.result(self.state, action)
        return Node(next_state, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next_state))

    def solution(self):
        """Return the sequence of actions to go from the root to this node.

        :return: sequence of actions
        :rtype: list
        """
        return [node.action for node in self.path()[1:]]

    def solve(self):
        """Return the sequence of states to go from the root to this node.

        :return: list of states
        :rtype: list
        """
        return [node.state for node in self.path()[0:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node.

        :return: list of states from the path
        :rtype: list(Node)
        """
        x, result = self, []
        while x:
            result.append(x)
            x = x.parent
        result.reverse()
        return result

    """We want the queue of nodes at breadth_first_search or
    astar_search to not contain states-duplicates, so the nodes that
    contain the same condition we treat as the same. [Problem: this can
    not be desirable in other situations.]"""

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


"""
Definitions of helper structures for storing the list of generated, but not checked nodes
"""


class Queue:
    """Queue is an abstract class/interface. There are three types:
        Stack(): Last In First Out Queue (stack).
        FIFOQueue(): First In First Out Queue.
        PriorityQueue(order, f): Queue in sorted order (default min-first).
    """

    def __init__(self):
        raise NotImplementedError

    def append(self, item):
        """Adds the item into the queue

        :param item: given element
        :return: None
        """
        raise NotImplementedError

    def extend(self, items):
        """Adds the items into the queue

        :param items: given elements
        :return: None
        """
        raise NotImplementedError

    def pop(self):
        """Returns the first element of the queue

        :return: first element
        """
        raise NotImplementedError

    def __len__(self):
        """Returns the number of elements in the queue

        :return: number of elements in the queue
        :rtype: int
        """
        raise NotImplementedError

    def __contains__(self, item):
        """Check if the queue contains the element item

        :param item: given element
        :return: whether the queue contains the item
        :rtype: bool
        """
        raise NotImplementedError


class Stack(Queue):
    """Last-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class FIFOQueue(Queue):
    """First-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class PriorityQueue(Queue):
    """A queue in which the minimum (or maximum) element is returned first
     (as determined by f and order). This structure is used in
     informed search"""

    def __init__(self, order=min, f=lambda x: x):
        """
        :param order: sorting function, if order is min, returns the element
                      with minimal f (x); if the order is max, then returns the
                      element with maximum f (x).
        :param f: function f(x)
        """
        assert order in [min, max]
        self.data = []
        self.order = order
        self.f = f

    def append(self, item):
        bisect.insort_right(self.data, (self.f(item), item))

    def extend(self, items):
        for item in items:
            bisect.insort_right(self.data, (self.f(item), item))

    def pop(self):
        if self.order == min:
            return self.data.pop(0)[1]
        return self.data.pop()[1]

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.data)

    def __getitem__(self, key):
        for _, item in self.data:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.data):
            if item == key:
                self.data.pop(i)


"""
Uninformed graph search
The main difference is that here we do not allow loops,
i.e. repetition of states
"""


def graph_search(problem, fringe):
    """Search through the successors of a problem to find a goal.
     If two paths reach a state, only use the best one.

    :param problem: given problem
    :param fringe: empty queue
    :return: Node
    """
    closed = {}
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node
        if node.state not in closed:
            closed[node.state] = True
            fringe.extend(node.expand(problem))
    return None


def breadth_first_graph_search(problem):
    """Search the shallowest nodes in the search tree first.

    :param problem: given problem
    :return: Node
    """
    return graph_search(problem, FIFOQueue())
class Directions(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT =4
class Change(Enum):
    UP = (0,1)
    RIGHT = (1,0)
    DOWN =(0,-1)
    LEFT=(-1,0)


#continue straight
def move_straight(state):
    head = state[0][-1]
    if(state[1] == Directions.DOWN):
        new_state = list(state)
        new_state[0] = list(new_state[0])
        new_state[0].append((head[0]+Change.DOWN.value[0],head[1]+Change.DOWN.value[1]))
        new_state[0] = tuple(new_state[0])
        new_state = tuple(new_state)    
        
        return new_state
    if(state[1] == Directions.RIGHT):
        new_state = list(state)
        new_state[0] = list(new_state[0])
        new_state[0].append((head[0]+Change.RIGHT.value[0],head[1]+Change.RIGHT.value[1]))
        new_state[0] = tuple(new_state[0])
        new_state = tuple(new_state)
        return new_state
    if(state[1] == Directions.UP):
        new_state = list(state)
        new_state[0] = list(new_state[0])
        new_state[0].append((head[0]+Change.UP.value[0],head[1]+Change.UP.value[1]))
        new_state[0] = tuple(new_state[0])
        new_state = tuple(new_state)
        return new_state
    if(state[1] == Directions.LEFT):
        new_state = list(state)
        new_state[0] = list(new_state[0])
        new_state[0].append((head[0]+Change.LEFT.value[0],head[1]+Change.LEFT.value[1]))
        new_state[0] = tuple(new_state[0])
        new_state = tuple(new_state)
        return new_state
def move_left(state):
    if(state[1] == Directions.DOWN):
        new_state = list(state)
        new_state[0] = list(new_state[0])
        new_state[0].append((new_state[0][-1][0]+Change.RIGHT.value[0],new_state[0][-1][1]+Change.RIGHT.value[1]))
        new_state[0] = tuple(new_state[0])
        new_state[1] = Directions.RIGHT
        new_state = tuple(new_state)
        return new_state
    if(state[1] == Directions.RIGHT):
        new_state = list(state)
        new_state[0] = list(new_state[0])
        new_state[0].append((new_state[0][-1][0]+Change.UP.value[0],new_state[0][-1][1]+Change.UP.value[1]))
        new_state[0] = tuple(new_state[0])
        new_state[1] = Directions.UP
        new_state = tuple(new_state)
        return new_state
    if(state[1] == Directions.UP):
        new_state = list(state)
        new_state[0] = list(new_state[0])
        new_state[0].append((new_state[0][-1][0]+Change.LEFT.value[0],new_state[0][-1][1]+Change.LEFT.value[1]))
        new_state[0] = tuple(new_state[0])
        new_state[1] = Directions.LEFT
        new_state = tuple(new_state)
        return new_state
    if(state[1] == Directions.LEFT):
        new_state = list(state)
        new_state[0] = list(new_state[0])
        new_state[0].append((new_state[0][-1][0]+Change.DOWN.value[0],new_state[0][-1][1]+Change.DOWN.value[1]))
        new_state[0] = tuple(new_state[0])
        new_state[1] = Directions.DOWN
        new_state = tuple(new_state)
        return new_state
def move_right(state):
    if(state[1] == Directions.DOWN):
        new_state = list(state)
        new_state[0] = list(new_state[0])
        new_state[0].append((new_state[0][-1][0]+Change.LEFT.value[0],new_state[0][-1][1]+Change.LEFT.value[1]))
        new_state[0] = tuple(new_state[0])
        new_state[1] = Directions.LEFT
        new_state = tuple(new_state)
        return new_state
    if(state[1] == Directions.RIGHT):
        new_state = list(state)
        new_state[0] = list(new_state[0])
        new_state[0].append((new_state[0][-1][0]+Change.DOWN.value[0],new_state[0][-1][1]+Change.DOWN.value[1]))
        new_state[0] = tuple(new_state[0])
        new_state[1] = Directions.DOWN
        new_state = tuple(new_state)
        return new_state
    if(state[1] == Directions.UP):
        new_state = list(state)
        new_state[0] = list(new_state[0])
        new_state[0].append((new_state[0][-1][0]+Change.RIGHT.value[0],new_state[0][-1][1]+Change.RIGHT.value[1]))
        new_state[0] = tuple(new_state[0])
        new_state[1] = Directions.RIGHT
        new_state = tuple(new_state)
        return new_state
    if(state[1] == Directions.LEFT):
        new_state = list(state)
        new_state[0] = list(new_state[0])
        new_state[0].append((new_state[0][-1][0]+Change.UP.value[0],new_state[0][-1][1]+Change.UP.value[1]))
        new_state[0] = tuple(new_state[0])
        new_state[1] = Directions.UP
        new_state = tuple(new_state)
        return new_state
class Snake(Problem):
    def __init__(self, initial,g_a,r_a,size, goal=None):
        super().__init__(initial, goal)
        self.green_apples = g_a
        self.red_apples = r_a
        self.size = size
    def goal_test(self, state):
        
        return len(state[-1])==0
    def actions(self, state):
        return self.successor(state).keys()
    def result(self,state,action):
        return self.successor(state)[action]
    def valid(self,head):
        if head<0 or head>=self.size or head<0 or head>=self.size:
            return False
        if head in self.red_apples:
            return False
        if head in body:
            return False
        
        return True
    def valid_move(self,state):
        head = state[0][-1]
        if head[0]<0 or head[0]>=self.size or head[1]<0 or head[1]>=self.size:
            return False
        if head in self.red_apples:
            return False
        body = state[0][0:-1]
        
        
        if head in body:
            return False
        

        return True
    def on_apple(self,state):
        apples = state[2]
        body = state[0]
        if body[-1] not in apples:
            body = body[1:] 
        else:
            apples = list(apples)
            body = list(body)
            apples.remove(state[0][-1])
            apples = tuple(apples)
            body = tuple(body)
        
        
        return (body,state[1],apples)
    def successor(self, state):
        succ =dict()
        akcii = ["ProdolzhiPravo","SvrtiLevo","SvrtiDesno",]   
        head = state[0][-1]
        direction = state[1]
        for action in akcii:
            new_state = []
            if(action == "ProdolzhiPravo" ):
                new_state = move_straight(state)
            if(action == "SvrtiDesno"):
                new_state = move_right(state)
            if(action == "SvrtiLevo"):
                new_state = move_left(state)
            
            if(self.valid_move(new_state)):
                new_state= self.on_apple(new_state)    
                succ[action] = tuple(new_state)
        return succ

if __name__ == '__main__':
    num_green_apples = int(input())
    green_apples_positions = list()
    for i in range(num_green_apples):
        green_apples_positions.append(tuple(map(int,input().split(','))))
    num_red_apples = int(input())
    red_apples_positions = list()
    for i in range(num_red_apples):
        red_apples_positions.append(tuple(map(int,input().split(','))))
    size =10
    green_apples_positions= tuple(green_apples_positions)
    #direction = UP RIGHT DOWN LEFT
    # (((0,9),(0,8),(0,7)),DOWN) Initial snake state
    snake_state = (((0,9),(0,8),(0,7)),Directions.DOWN,green_apples_positions)
    problem = Snake(snake_state,green_apples_positions,red_apples_positions,size)
    sol = breadth_first_graph_search(problem)
    print(sol.solution())
