
import random

def rm():
	return random.random()

class model:
	def __init__(self,n):
		self.ns = n
		self.n_len = len(self.ns)
		self.n_sum = sum(n)
		self.w = [[[random.random(),[random.random() for c in range(n[a+1])]] for b in range(n[a])] for a in range(len(n)-1)]
		self.b = [random.random()*random.randint(0,1)	 for i in range(self.n_len-1)]
		self.go = [[0 for j in range(n[i])] for i in range(self.n_len)]

	def forward(self,cins):
		go = [i.copy() for i in self.go]
		go[0] = cins
		for i in range(self.n_len-1):
			for a in range(self.ns[i]):
				for b in range(self.ns[i+1]):
					go[i+1][b] += go[i][a]*self.w[i][a][0]*self.w[i][a][1][b]
			for c in range(self.ns[i+1]):
				go[i+1][c] += self.b[i]
		go[-1] = [i+b for i in go[-1]]
		self.go2 = go
		return go[-1]

	def test(self,cins,outs):
		e = sum([abs(self.sum_abs(self.forward(cins[i]),outs[i])) for i in range(len(outs))])/len(cins)
		self.test_num = e
		return e

	def sum_abs(self,lst1,lst2):
		return sum([abs(lst1[i]-lst2[i]) for i in range(len(lst1))])


class models:
	def __init__(self,ns,n,geto=2,yb=True,bc=10,lc=2):
		self.mdn = [model(n) for i in range(ns)]
		self.n_len = len(n)
		self.epochs = 0
		self.geto = geto
		self.gets = self.ogets(ns)
		self.ns = ns
		self.n = n
		self.yb = self.oyb(yb)
		self.m = [1/(bc+i) for i in range(self.gets)]
		self.lc = self.olc(lc)
	def go(self,cins,outs,gets=True):
		if (gets==True):
			gets = self.gets
		self.gets = gets
		gets = min(gets,self.n_len)
		self.test_number = [[self.mdn[i].test(cins,outs),i] for i in range(len(self.mdn))]
		self.jl = self.test_number
		#for i in range(len(self.test_number)-1):
		#	for j in range(i,len(self.test_number)-1):
		#		if (self.test_number[j][0]>self.test_number[j+1][0]):
		#		#if (self.test_number[j][0]<self.test_number[j+1][0]):
		#			self.test_number[j],self.test_number[j+1] = self.test_number[j+1],self.test_number[j]
		self.test_number = sorted(self.test_number)
		tesnumb = self.test_number[0:gets]
		self.get_list = [i[1] for i in tesnumb]
		#self.gent()
		self.gent2()

	def gent(self):
		for i in range(len(self.get_list)-1):
			num = [self.mdn[i] for i in self.get_list]
			for a in range(len(num)):
				be_num = self.n/self.geto
				if (be_num!=int(be_num)):
					be_num = [int(be_num) for i in range(len(num))]
					be_num[-1] += self.n-sum(be_num)
				for i in range(self.geto):
					float("inf")
			i+=self.geto-1

	def gent2(self):
		for i in range(len(self.get_list)-1):
			num = [self.mdn[i] for i in self.get_list]
			self.new_mdn = [model(self.n) for i in range(self.ns)]
			for a in range(len(num)):
				if (a+1>=len(num)):
					break
				#rn = self.rand(len(num))
				rn = random.randint(0,len(num)-1)
				#[[print(i) for i in num[a].w[n]] for n in range(self.n_len)]	
				#b1,b2 = [[i[1][0:len(i[1])//2] for i in num[a].w[n]] for n in range(self.n_len)],[[i[1][len(i[1])//2:len(i[1])] for i in num[a].w[n]] for n in range(self.n_len)]
				#c1,c2 = [[i[1][0:len(i[1])//2] for i in num[rn].w[n]] for n in range(self.n_len)],[[i[1][len(i[1])//2:len(i[1])] for i in num[rn].w[n]] for n in range(self.n_len)]
				b1,b2 = self.mdn[self.get_list[a]].w[0:self.yb],self.mdn[self.get_list[a]].w[self.yb:self.n_len]
				c1,c2=self.mdn[self.get_list[rn]].w[0:self.yb],self.mdn[self.get_list[rn]].w[self.yb:self.n_len]
				self.new_mdn[self.get_list[a]].w = b1+c2
				self.new_mdn[self.get_list[rn]].w = c1+b2
				self.new_mdn[self.get_list[a]].b = self.mdn[self.get_list[a]].b
				self.new_mdn[self.get_list[rn]].b = self.mdn[self.get_list[rn]].b
				if (random.random() >= 0.9 and self.mdn[self.get_list[a]].test_num > 0.1):
					self.new_mdn[self.get_list[a]].w[random.randint(1,self.n_len-1)-1][0][0] = random.random()
				if (random.random() >= 0.9 and self.mdn[self.get_list[rn]].test_num > 0.1):
					self.new_mdn[self.get_list[rn]].w[random.randint(1,self.n_len-1)-1][0][0] = random.random()
				if (random.random() >= 0.9 and self.mdn[self.get_list[a]].test_num > 0.1):
					self.new_mdn[self.get_list[a]].b[random.randint(1,self.n_len-1)-1] = random.randint(-1,1)*random.random()
				if (random.random() >= 0.9 and self.mdn[self.get_list[rn]].test_num > 0.1):
					self.new_mdn[self.get_list[rn]].b[random.randint(1,self.n_len-1)-1] = random.randint(-1,1)*random.random()
				i+=1
			for i in range(self.lc):
				self.new_mdn[self.ns-1-i] = self.mdn[self.get_list[i]]
		self.mdn = self.new_mdn

	def ogets(self,goto):
		if (goto%self.geto==0):
			return goto//self.geto
		if (goto-1<=0):
			raise ValueError(f"You need ask your num divide by {self.geto}")
		return (goto-1)//self.geto

	def oyb(self,yb):
		if (yb==True):
			yb = self.ns//2
		return min(max(yb,1),self.ns)

	def rand(self,number):
		m = self.m.copy()
		while (1):
			for i in range(number):
				m[i]+=random.random()/10
				if (m[i]>=1):
					return i
	
	def olc(self,lc):
		if (lc<self.gets):
			return lc
		return self.gets-1

	def print_test(self,getnum=1):
		for i in self.test_number[0:getnum]:
			print(f"{i[1]}:{i[0]}",end=' ')
		print("\n")

#You can simulate most functions with it
mds = models(500,[1,20,20,1],lc=3) 
for i in range(200):
	got1 = random.random()
	got2 = got1*2+1 #function
	mds.go([[got1]],[[got2]])
	mds.print_test(100)
print(mds.mdn[mds.test_number[0][1]].w)
a = random.random()
print(a)
print(mds.mdn[mds.test_number[0][1]].forward([a])) #Actual Output
print(a*2+1) #Expected Output
#print(mds.mdn[0].test([[0.5]],[0.5]))
