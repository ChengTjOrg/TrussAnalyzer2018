class Element:
    pass

class Node:
    """
    编写结点类信息
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.constraint = [0,0]	#	0 自由， 1 约束
		self.globalDof = [-1,-1]
	
	def SetConstraint(self,constraint):
		self.constraint = constraint

class Truss(Element):
	"""
	编写单元类信息
	"""
	def __init__(self, node1, node2):
		self.node1 = node1
		self.node2 = node2
		self.EA = 0
		self.length = 0
		self.Ke = None
		slef.Pe = None
		
	def SetEA(self, EA):
		self.EA = EA
		
	def SetNodes(self, node1, node2):
		self.node1 = node1
		self.node2 = node2

	def CalculateLength(self):
		dx = node2.x - node1.x
		dy = node2.y - node1.y
		self.length = sqrt(dx*dx + dy*dy)	# sqrt可能需要import
		
	def Length():
		return self.length
		
	def EA():
		return self.EA
		
	def CalculateTrussStiffMatrix(self):
		pass

class ElementLoad():
	pass
	
class NodalLoad():
	"""
	编写结点荷载类信息
	"""
	def __init__(self, node, f1, f2):	# 全局或局部坐标
		self.node = node
		self.f1 = f1
		self.f2 = f2

class Application():
	"""
	编写应用类信息
	"""
	def __init__(self, appName):
		self.appName = appName
		self.num_node = 0
		self.num_truss = 0
		self.num_load = 0
		self.nodes = []
		self.trusses = []
		self.loads = []
		self.K = None
		self.P = None
		# .....
		
	def AddNode(self, newNode):
	"""
	注释函数介绍，功能？入口参数，返回参数，用法
	"""
		self.nodes.append(newNode)
	## 
	def AddTruss(self, newTruss):
		pass
	def AddLoad(self, newLoad):
		pass
	def CalculateStiffMatrix(self):
		pass
	def CalculateLoadVector(self):
		pass