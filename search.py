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
import node
import sys
import searchAgents

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

def treeSearch(problem):
    """
    Search algorithm using tree structure
    """    
    fringe = [node.Node(problem.getStartState(), None, None, 0)]
    
    while True:
        if len(fringe) <= 0: sys.exit('failure')
        n = fringe.pop()
        print n
        for state, action, cost in problem.getSuccessors(n.state):
            ns = node.Node(state, n, action, n.pathcost+cost)
            fringe.append(ns)

def depthFirstSearchList(problem):
  """
  Search the deepest nodes in the search graph first. Using a list as fringe.
  """  
  fringe = [node.Node(problem.getStartState(), None, None, 0)]
  expanded = {}
  
  while True:
    if len(fringe) <= 0: sys.exit('failure')
    n = fringe.pop()
    expanded[n.state] = ['E', n]
    print n
    for state, action, cost in problem.getSuccessors(n.state):
        ns = node.Node(state, n, action, n.pathcost+cost)         
        if ns not in fringe and ns.state not in expanded.keys(): 
            if problem.isGoalState(ns.state): 
                return ns.path() 
            expanded[ns.state] = ['F', n]
            fringe.append(ns)

def depthFirstSearchStack(problem):
  """
  Search the deepest nodes in the search graph first. Using a Stack as fringe.
  """
  fringe = util.Stack(node.Node(problem.getStartState(), None, None, 0))
  expanded = {}
  
  while True:
    if fringe.isEmpty(): sys.exit('failure')
    n = fringe.pop()
    expanded[n.state] = ['E', n]
    print n
    for state, action, cost in problem.getSuccessors(n.state):
        ns = node.Node(state, n, action, n.pathcost+cost)         
        if ns.state not in expanded.keys() and ns not in fringe:
            if problem.isGoalState(ns.state): 
                return ns.path() 
            expanded[ns.state] = ['F', n]
            fringe.push(ns)
                        
def depthFirstSearchTree(problem):
  """
  Search the deepest nodes in the search tree first. Using a stack as fringe.
  """
  fringe = util.Stack(node.Node(problem.getStartState(), None, None, 0))
  
  while True:
    if fringe.isEmpty(): sys.exit('failure')
    n = fringe.pop()
    print n
    for state, action, cost in problem.getSuccessors(n.state):
        ns = node.Node(state, n, action, n.pathcost+cost)         
        if ns not in fringe:
            if problem.isGoalState(ns.state): 
                return ns.path() 
            fringe.push(ns)
            
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search graph first
    """
    fringe = util.Stack(node.Node(problem.getStartState(), None, None, 0))
    return graphSearch(problem, fringe)
        
def breadthFirstSearchList(problem):
  """
  Search the shallowest nodes in the search tree first. 
  """
  fringe = [node.Node(problem.getStartState(), None, None, 0)]
  expanded = {}
  
  while True:
    if len(fringe) <= 0: sys.exit('failure')
    n = fringe.pop(0)
    expanded[n.state] = ['E', n]
    print n
    for state, action, cost in problem.getSuccessors(n.state):
        ns = node.Node(state, n, action, n.pathcost+cost)         
        if ns.state not in expanded.keys() and ns not in fringe: 
            if problem.isGoalState(ns.state): 
                return ns.path() 
            expanded[ns.state] = ['F', n]
            fringe.append(ns)

def breadthFirstSearchQueue(problem):
  """
  Search the shallowest nodes in the search tree first.
  """  
  fringe = util.Queue(node.Node(problem.getStartState(), None, None, 0))  
  expanded = {}
  
  while True:
    if fringe.isEmpty(): sys.exit('failure')
    n = fringe.pop()
    expanded[n.state] = ['E', n]
    for state, action, cost in problem.getSuccessors(n.state):
        ns = node.Node(state, n, action, n.pathcost+cost)         
        if ns.state not in expanded.keys() and ns not in fringe: 
            if problem.isGoalState(ns.state): 
                return ns.path() 
            expanded[ns.state] = ['F', n]
            fringe.push(ns)

def breadthFirstSearchTree(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    fringe = util.Queue(node.Node(problem.getStartState(), None, None, 0))
    while True:
        if fringe.isEmpty(): sys.exit('failure')
        n = fringe.pop()
        print n
        for state, action, cost in problem.getSuccessors(n.state):
            ns = node.Node(state, n, action, n.pathcost+cost)
            if ns not in fringe:
                if problem.isGoalState(ns.state):
                    return ns.path()
                fringe.push(ns)      
                
def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  """
  fringe = util.Queue(node.Node(problem.getStartState(), None, None, 0))
  return graphSearch(problem, fringe)  

def depthLimitedSearchTree(problem,limit=1000):
    """
        limit: how deep is the algorithm, the max distance between the food and the tartState  
    commetns
    """
    #fringe = [node.Node(problem.getStartState(), None, None, 0)]
    fringe = util.Queue(node.Node(problem.getStartState(), None, None, 0))
    cut = False
    
    while True:
        if fringe.isEmpty():
        #if len(fringe) <= 0:  
            if cut: return "cut"          
        n = fringe.pop()
        if n.pathcost == limit: cut = True
        else:
            for state, action, cost in problem.getSuccessors(n.state):
                ns = node.Node(state, n, action, n.pathcost+cost)         
                if ns not in fringe: 
                    if problem.isGoalState(ns.state): return ns.path() 
                    fringe.push(ns) 
                    
def depthLimitedSearch(problem,limit=1000):
    """
        limit: how deep is the algorithm, the max distance between the food and the tartState  
    commetns
    """
    fringe = util.Queue(node.Node(problem.getStartState(), None, None, 0))
    expanded = {}
    cut = False
    
    while True:
        if fringe.isEmpty(): 
            if cut: return "cut"          
        n = fringe.pop()
        expanded[n.state] = ['E', n]
        if n.pathcost == limit: cut = True
        else:
            for state, action, cost in problem.getSuccessors(n.state):
                ns = node.Node(state, n, action, n.pathcost+cost)         
                if ns.state not in expanded.keys() and ns not in fringe: 
                    if problem.isGoalState(ns.state): return ns.path() 
                    expanded[ns.state] = ['F', n]
                    fringe.push(ns) 

def iterativeDepeningSearchTree(problem):
    """
    Iterative Depening Search, that calls depthLimitedSearch with an increasing limit till find a solution
    """
    found = False
    iteration = 0
    
    while (not found):
        result = depthLimitedSearchTree(problem,iteration)
        if result != "cut": return result
        iteration+=1

def iterativeDepeningSearch(problem):
    """
    Iterative Depening Search, that calls depthLimitedSearch with an increasing limit till find a solution
    """
    found = False
    iteration = 0
    
    while (not found):
        result = depthLimitedSearch(problem,iteration)
        if result != "cut": return result
        iteration+=1

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def manhattanHeuristic(state, problem):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem. Using the manhattan distance betwen this 2 points
    """
    return searchAgents.manhattanHeuristic(state, problem)

def h1(state, problem):
    """
    Simple heurisitic that return the product between the given state coordinates  
    """
    
    x,y = state
    return   x+y

def h2(state, problem):
    """
    Simple heurisitic that return the product between the given state coordinates  
    """
    
    x,y = state
    return   x*y
    
def uniformCostSearchPriority(problem):
  """
  Search the node of least total cost first.
  """
  fringe = util.PriorityQueue(node.Node(problem.getStartState(), None, None, 0),0)
  expanded = {}
  
  while True:
    if fringe.isEmpty(): sys.exit('failure')
    n = fringe.pop()
    if problem.isGoalState(n.state): return n.path()    
    expanded[n.state] = ['E', n]
    for state, action, cost in problem.getSuccessors(n.state):
        ns = node.Node(state, n, action, n.pathcost+cost)         
        if ns.state not in expanded.keys(): 
            fringe.push(ns,ns.pathcost)
            expanded[ns.state] = ['F', n]
        elif ns.state in expanded.keys() and ns.pathcost < expanded.get(ns.state)[1].pathcost :
            fringe.push(ns,ns.pathcost)
            expanded[ns.state] = ['E', n]
                                
def uniformCostSearch(problem):
    """
    Search the node of least total cost first. 
    """
    return aStarSearch(problem,nullHeuristic)

def aStarSearch(problem, heur=manhattanHeuristic, greedyFlag=1):
  """
      heur: heurisitc given to solve the problem, default manhattanHeuristic
      greedyFlag: flag to know if we use the pathcost also to sort the node on fringe
      
  Search the node that has the lowest combined cost and heuristic first."
  """ 
  heuristica = heur(problem.getStartState(), problem)
  fringe = util.PriorityQueue(node.Node(problem.getStartState(), None, None, 0),heur)  
  expanded = {}
  
  while True:
    if fringe.isEmpty(): sys.exit('failure')
    n = fringe.pop()
    if problem.isGoalState(n.state): return n.path()
    expanded[n.state] = ['E', n]
    for state, action, cost in problem.getSuccessors(n.state):
        heuristica = heur(state, problem)
        ns = node.Node(state, n, action, n.pathcost+cost)         
        if ns.state not in expanded.keys(): 
            fringe.push(ns,(greedyFlag*ns.pathcost)+heuristica)
            expanded[ns.state] = ['F', n]
        elif ns.state in expanded.keys() and ns.pathcost < expanded.get(ns.state)[1].pathcost :
            fringe.push(ns,(greedyFlag*ns.pathcost)+heuristica)
            expanded[ns.state] = ['E', n]

def greedySearchPriority(problem, heur=manhattanHeuristic):
  """
      heur: heurisitc given to solve the problem, default manhattanHeuristic
      
  Search the node that has the lowest heuristic first with.
  """
  fringe = util.PriorityQueue(node.Node(problem.getStartState(), None, None, 0),heur)  
  expanded = {}
  
  while True:
    if fringe.isEmpty(): sys.exit('failure')
    n = fringe.pop()
    if problem.isGoalState(n.state): return n.path()
    expanded[n.state] = ['E', n]
    for state, action, cost in problem.getSuccessors(n.state):
        heuristica = heur(state, problem)
        ns = node.Node(state, n, action, cost)         
        if ns.state not in expanded.keys(): 
            fringe.push(ns,heuristica)
            expanded[ns.state] = ['F', n]
        elif ns.state in expanded.keys() and ns.pathcost < expanded.get(ns.state)[1].pathcost :
            fringe.push(ns,heuristica)
            expanded[ns.state] = ['E', n]
            
def greedySearch(problem, heur=manhattanHeuristic):
  """"
      h1 : heurisitic
      
  Search the node that has the lowest heuristic first.
  Calling the aStarSearch function with the last parameter 0 because
  we want to use only the heurisitc to order the fringe priority queue.  
  """
  return aStarSearch(problem,heur,0)

def graphSearch(problem, fringe):
    """
        fringe: the different kind of container, like queue, stack or priority queue.
    
    Search algorithm using graph structure and the given fringe.
    """
    expanded = {}
    
    while True:
        if fringe.isEmpty(): sys.exit('failure')
        n = fringe.pop()
        expanded[n.state] = ['E', n]
        for state, action, cost in problem.getSuccessors(n.state):
            ns = node.Node(state, n, action, n.pathcost+cost)
            if ns.state not in expanded.keys() and ns not in fringe:
                if problem.isGoalState(ns.state):
                    return ns.path()
                expanded[ns.state] = ['F', n]
                fringe.push(ns)
                

# Abbreviations

ids = iterativeDepeningSearch
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
dls = depthLimitedSearch
greedy = greedySearch