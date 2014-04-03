import util
class Node:

        id = 0	
	def __init__(self, state, parent, action, pathcost):
		
		self.state = state
		self.parent = parent
		self.action = action
		self.pathcost = pathcost
		self.id = Node.id
		Node.id = Node.id + 1
    
        def __eq__(self, other):
        
            return self.id == other.id

	def __str__(self):

		if self.parent != None: idp = self.parent.id
		else: idp = None
    

		#return 'id:'+str(self.id)+' '+str(self.state)+' '+str(idp)+' '+str(self.action)+' '+str(self.pathcost) # naive
		#return " ".join([str(i) for i in ['id:',self.id,self.state,idp,self.action,self.pathcost]]) 3 join + list comprehen.
		return '[%d: %s %s %s %d' % (self.id, self.state, idp, self.action, self.pathcost)
        
        def path(self):
        
            n = self
            path = []
            while n.parent != None:
                path.append(n.action)
                n = n.parent
            path.reverse()            
            return path
        
        def pathR(self):
            n = self
            path = []
            if n.parent == None:                
                path.reverse()
                return path 
            else:
                path.append(n.action)
                pathR(n.parent)
        
        def contains(self,qeue):        
            for x in qeue:
                if self.state == x.state: return True
            return False
        
        def isBetter(self,list):        
            for x in list:
                if self.state == x.state and self.pathcost<x.pathcost: return True
            return False
        
        def replace(self,list):        
            for x in list:
                if n.state == x.state:
                    list.remove(x)
            list.append(self)
            return False    	

if __name__ == "__main__":
	
	n = Node((0,0), None, None, 0)
	
	for i in range(3):
		n = Node((n.state[0]+1,n.state[1]),n,'south'+str(i),n.pathcost+1)
        
	print n
        
        print n.path()


