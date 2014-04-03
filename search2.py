# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

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
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  """ 
  import node
  import sys

  fringe = util.Stack((node.Node(problem.getStartState(),None ,None, 0)))
  expanded = []
  while True:
    if util.Stack.isEmpty(fringe): return sys.exit('Failure: no solution')
    n = fringe.pop()
    expanded.append(n)
    for state, action, cost in problem.getSuccessors(n.state):
        ns = node.Node(state, n, action, cost)
        #print ns
        #y = raw_input("continure")
        if not ns.contains(expanded) and not ns.contains(fringe):
            if problem.isGoalState(ns.state):
                return ns.path()
            fringe.append(ns)
   
    
  #util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  import node
  import sys

  fringe = [node.Node(problem.getStartState(),None ,None, 0)]
  expanded = []
  while True:
    if len(fringe) == 0: return sys.exit('Failure: no solution')
    n = fringe.pop(0)
    expanded.append(n)
    for state, action, cost in problem.getSuccessors(n.state):
        ns = node.Node(state, n, action, cost)
        #print ns
        #y = raw_input("continure")
        if not ns.contains(expanded) and not ns.contains(fringe):
            if problem.isGoalState(ns.state):
                return ns.path()
            fringe.append(ns)
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  import node
  import sys

  fringe = [node.Node(problem.getStartState(),None ,None, 0)]
  expanded = []
  while True:
    if len(fringe) == 0: return sys.exit('Failure: no solution')
    n = fringe.pop()
    if problem.isGoalState(n.state): return n.path()
    expanded.append(n)
    for state, action, cost in problem.getSuccessors(n.state):
        ns = node.Node(state, n, action, cost)
        #print ns
        #y = raw_input("continure")
        if not ns.contains(expanded) and not ns.contains(fringe):
            fringe.append(ns)
        elif ns.isBetter(fringe):
            ns.replace(fringe)

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
