import os,sqlite3

class SQL:
   def __init__(self,name):
      self.con = sqlite3.connect(f'{name}.db')
      self.cur = self.con.cursor()
   def execute(self,code,add = (),commit = True):
      data = ""
      if add != ():
         data = self.cur.execute(code,add)
      elif add == ():
         data = self.cur.execute(code)
      if commit:
         self.commit()
      return data
   def commit(self):
      self.con.commit()
   def close(self):
      self.con.close()
   def getid(self,table,idpos = 0):
      ids = []
      for i in self.execute("SELECT * FROM {} ORDER BY id".format(table)):
         ids.append(i)
      if len(ids) >= 1:
         return int(ids[-1][idpos]) + 1
      return 1

def ToString(ls):
    ret = ""
    for i in ls:
        if type(i) in [str,int,float,bool]:
            ret += str(i)
        


def extract(ls,index,depth):
    #args [[1,2],[3,[4,5]]] and 1 and 1
    #returns [2,[4,5]]

    #args [2,[4,5]] and 1 and 1
    #returns [2,5]

    #args º and 1 and 2
    #returns [2,5]]

    def __substract__(ls,index):
        ret = []
        for i in ls:
            if type(i) == list:
                ret.append(i[index])
            else:
                ret.append(i)
        return ret

    if depth == 1:
        return __substract__(ls,index)
    elif depth > 1:
        ret = __substract__(ls,index)
        for i in range(depth):
            ret = __substract__(ret,index)
        return ret
