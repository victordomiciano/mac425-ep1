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

from game import Directions
n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST

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
    return [s, s, w, s, w, w, s, w]

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

    def getPredecessor(actualState):
        if actualState[1] == 'North':
            return (actualState[0][0], actualState[0][1] - 1)
        if actualState[1] == 'South':
            return (actualState[0][0], actualState[0][1] + 1)
        if actualState[1] == 'East':
            return (actualState[0][0] - 1, actualState[0][1])
        if actualState[1] == 'West':
            return (actualState[0][0] + 1, actualState[0][1])

    def pushStack(state):
        util.Stack.push(stack, state[0])
        dirlist = list(coord.get(getPredecessor(state)))
        dirlist.append(state[1])
        coord[state[0]] = dirlist

    visited = [problem.getStartState()]
    if problem.isGoalState(visited[0]):
        return []
    stack = util.Stack()
    coord = {}
    goal = (-1, -1)

    successors = problem.getSuccessors(problem.getStartState())
    pos = problem.getStartState()
    coord[pos] = []
    valid = 1

    for i in range(len(successors)):
        pushStack(successors[i])
    while (not(util.Stack.isEmpty(stack)) and goal == (-1, -1)):
        successors = problem.getSuccessors(util.Stack.pop(stack))
        for i in range(len(successors)):
            for j in range(len(visited)):
                if visited[j] == successors[i][0]:
                    valid = 0
                    break
            if valid == 0:
                valid = 1
                continue
            visited.append(successors[i][0])
            pushStack(successors[i])
            if problem.isGoalState(successors[i][0]):
                goal = successors[i][0]
                break

    return coord.get(goal)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    def getPredecessor(actualState):
        if actualState[1] == 'North':
            return (actualState[0][0], actualState[0][1] - 1)
        if actualState[1] == 'South':
            return (actualState[0][0], actualState[0][1] + 1)
        if actualState[1] == 'East':
            return (actualState[0][0] - 1, actualState[0][1])
        if actualState[1] == 'West':
            return (actualState[0][0] + 1, actualState[0][1])

    def pushQueue(state):
        util.Queue.push(queue, state[0])
        dirlist = list(coord.get(getPredecessor(state)))
        dirlist.append(state[1])
        coord[state[0]] = dirlist

    visited = [problem.getStartState()]
    if problem.isGoalState(visited[0]):
        return []
    queue = util.Queue()
    coord = {}
    goal = (-1, -1)

    successors = problem.getSuccessors(problem.getStartState())
    pos = problem.getStartState()
    coord[pos] = []
    valid = 1

    for i in range(len(successors)):
        pushQueue(successors[i])
    while (not(util.Queue.isEmpty(queue)) and goal == (-1, -1)):
        successors = problem.getSuccessors(util.Queue.pop(queue))
        for i in range(len(successors)):
            for j in range(len(visited)):
                if visited[j] == successors[i][0]:
                    valid = 0
                    break
            if valid == 0:
                valid = 1
                continue
            visited.append(successors[i][0])
            pushQueue(successors[i])
            if problem.isGoalState(successors[i][0]):
                goal = successors[i][0]
                break

    return coord.get(goal)

def iterativeDeepeningSearch(problem):
    """
    Start with depth = 0.
    Search the deepest nodes in the search tree first up to a given depth.
    If solution not found, increment depth limit and start over.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

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
    # "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
