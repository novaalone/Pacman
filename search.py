# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    "*** Initialize a frontier stack ***"
    frontier = util.Stack()
    "*** Initialize an explored set ***"
    explored_set = set()
    
    "*** Is the start a goal? ***"
    if problem.isGoalState(problem.getStartState()):
        
        return []
    "*** Push start state into the stack , initialize the action***"
    
    frontier.push((problem.getStartState(),[]))
    

    "*** Do the loop while frontier is not empty***"
    while not frontier.isEmpty():
        "*** pop the node to be explored***"
        node = frontier.pop()
        
        "*** is this node a goal? ***"
        if problem.isGoalState(node[0]):
            return node[1]


        "*** make sure the node has not been explored ***"
        if not node[0] in explored_set:
            "*** get the successors of the node ***"
            successors = problem.getSuccessors(node[0])
            "*** put the node into the explored_set ***"
            explored_set.add(node[0])
            
            for x in successors:
                "*** make sure the successors have not been explored ***"
                if x[0] not in explored_set:
                    "*** push x into the stack ,record the action***"
                    frontier.push((x[0],node[1]+[x[1]]))
    
    return []
    util.raiseNotDefined()
        
        
        
    

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    frontier = util.Queue()
    explored_set = set()
    
    
    if problem.isGoalState(problem.getStartState()):
        return []
    frontier.push((problem.getStartState(),[]))
    while not frontier.isEmpty():
        node = frontier.pop()
        
        if problem.isGoalState(node[0]):
            return node[1]
        if not node[0] in explored_set:
            successors = problem.getSuccessors(node[0])
            explored_set.add(node[0])
            for x in successors:
                if x[0] not in explored_set:
                    frontier.push((x[0],node[1]+[x[1]]))
                    
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    explored_set = set()
    
    cost=0
    if problem.isGoalState(problem.getStartState()):
        return []
    "*** record the cost as well as the state and action***"
    frontier.push((problem.getStartState(),[],cost),cost)
    while not frontier.isEmpty():
        node = frontier.pop()
        
        if problem.isGoalState(node[0]):
            return node[1]
        
        if node[0] not in explored_set:
            successors = problem.getSuccessors(node[0])
            explored_set.add(node[0])
            for x in successors:
                if x[0] not in explored_set:
                    "*** add the previous total cost to successor's cost***"
                    cost = node[2]+x[2]
                    frontier.push((x[0],node[1]+[x[1]],cost),cost)
                  
   
    return []
        
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    explored_set = set()
    cost = 0
    orders = cost+heuristic(problem.getStartState(),problem)
   
    if problem.isGoalState(problem.getStartState()):
        return []
    frontier.push((problem.getStartState(),[],cost,orders),orders)
    while not frontier.isEmpty():
        node = frontier.pop()
        
        if problem.isGoalState(node[0]):
            return node[1]
      
        if node[0] not in explored_set:
            successors = problem.getSuccessors(node[0])
            explored_set.add(node[0])
            for x in successors:
                if x[0] not in explored_set:
                    cost = node[2]+x[2]
                    orders = cost+heuristic(x[0],problem)
                    frontier.push((x[0],node[1]+[x[1]],cost,orders),orders)
                  
    return []
        
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
