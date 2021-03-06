# Nome: Victor Domiciano Mendonca
# nUSP: 8641963

# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    def getPredecessor(st):
        if st[1] == 'North':
            return (st[0][0], st[0][1] - 1)
        if st[1] == 'South':
            return (st[0][0], st[0][1] + 1)
        if st[1] == 'East':
            return (st[0][0] - 1, st[0][1])
        if st[1] == 'West':
            return (st[0][0] + 1, st[0][1])
        else:
            if st[1][3] == '-':
                return st[1][2]
            else:
                return st[1][2:4]

    def pushStack(state):
        util.Stack.push(stack, state[0])
        dirlist = list(coord.get(getPredecessor(state)))
        dirlist.append(state[1])
        coord[state[0]] = dirlist

    stack = util.Stack()
    util.Stack.push(stack, problem.getStartState())
    visited = []
    coord = {}
    coord[problem.getStartState()] = []

    while (1):
        state = util.Stack.pop(stack)
        if problem.isGoalState(state):
            goal = state
            break
        visited.append(state)
        successors = problem.getSuccessors(state)
        for st in successors:
            if st[0] not in visited:
                pushStack(st)

    return coord.get(goal)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    def getPredecessor(st):
        if st[1] == 'North':
            return (st[0][0], st[0][1] - 1)
        if st[1] == 'South':
            return (st[0][0], st[0][1] + 1)
        if st[1] == 'East':
            return (st[0][0] - 1, st[0][1])
        if st[1] == 'West':
            return (st[0][0] + 1, st[0][1])
        else:
            if st[1][3] == '-':
                return st[1][2]
            else:
                return st[1][2:4]

    def pushQueue(state):
        util.Queue.push(queue, state[0])
        dirlist = list(coord.get(getPredecessor(state)))
        dirlist.append(state[1])
        coord[state[0]] = dirlist

    queue = util.Queue()
    util.Queue.push(queue, problem.getStartState())
    visited = []
    coord = {}
    coord[problem.getStartState()] = []

    while (1):
        state = util.Queue.pop(queue)
        if problem.isGoalState(state):
            goal = state
            break
        visited.append(state)
        successors = problem.getSuccessors(state)
        for st in successors:
            if st[0] not in visited:
                pushQueue(st)
                visited.append(st[0])

    return coord.get(goal)

def iterativeDeepeningSearch(problem):
    """
    Start with depth = 0.
    Search the deepest nodes in the search tree first up to a given depth.
    If solution not found, increment depth limit and start over.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """

    def getPredecessor(st):
        if st[1] == 'North':
            return (st[0][0], st[0][1] - 1)
        if st[1] == 'South':
            return (st[0][0], st[0][1] + 1)
        if st[1] == 'East':
            return (st[0][0] - 1, st[0][1])
        if st[1] == 'West':
            return (st[0][0] + 1, st[0][1])
        else:
            if st[1][3] == '-':
                return st[1][2]
            else:
                return st[1][2:4]

    def pushStack(state):
        dirlist = list(coord.get(getPredecessor(state)))
        dirlist.append(state[1])
        if coord.get(state[0]) == None:
            coord[state[0]] = dirlist
        if len(dirlist) <= depth:
            util.Stack.push(stack, state[0])

    depth = 0
    goal = ()
    coord = {}
    coord[problem.getStartState()] = []
    stack = util.Stack()

    while (goal == ()):
        util.Stack.push(stack, problem.getStartState())
        visited = []
        while (not util.Stack.isEmpty(stack)):
            state = util.Stack.pop(stack)
            if problem.isGoalState(state):
                goal = state
                break
            visited.append(state)
            successors = problem.getSuccessors(state)
            for st in successors:
                if st[0] not in visited:
                    pushStack(st)
        depth += 1

    return coord.get(goal)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    pQueue = util.PriorityQueue()
    util.PriorityQueue.update(pQueue, problem.getStartState(), heuristic(problem.getStartState(), problem))
    visited = []
    coord = {}
    coord[problem.getStartState()] = []
    cost = {}
    cost[problem.getStartState()] = 0

    while (1):
        state = util.PriorityQueue.pop(pQueue)
        if problem.isGoalState(state):
            goal = state
            break
        visited.append(state)
        successors = problem.getSuccessors(state)
        for st in successors:
            combinedCost = cost.get(state) + st[2]
            dirlist = list(coord.get(state))
            dirlist.append(st[1])
            if st[0] not in visited:
                cost[st[0]] = combinedCost
                coord[st[0]] = dirlist
                util.PriorityQueue.update(pQueue, st[0], combinedCost + heuristic(st[0], problem))
                visited.append(st[0])
            elif combinedCost < cost.get(st[0]):
                cost[st[0]] = combinedCost
                coord[st[0]] = dirlist
                util.PriorityQueue.update(pQueue, st[0], combinedCost + heuristic(st[0], problem))

    return coord.get(goal)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
