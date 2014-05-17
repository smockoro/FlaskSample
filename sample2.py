import numpy as np
from flask import Flask, render_template

def tranceF_2(list):
    for i in range(len(list)):
        list[i] = list[i] % 2
    return list 

class G:
    #G is a generate matrix 
    def __init__(self):
        self.matrix = np.array([ [1,1,0] , [0,1,1] ])
        self.rowSize = self.matrix.shape[0]
        self.columnSize = self.matrix.shape[1]

    def getMatrix(self):
        return self.matrix
    def getRowSize(self):
        return self.rowSize
    def getColumnSize(self):
        return self.columnSize

class M:
    #M is a message vector
    def __init__(self):
        self.matrix = np.array([ [0,0],[0,1],[1,0],[1,1] ])
        self.columnSize = self.matrix.shape[1]

    def getMessage(self):
        return self.matrix
    def getColumnSize(self):
        return self.columnSize

def makeCode(G, M):
    code = []
    if G.getRowSize() != M.getColumnSize():
        return code 
    else:
        for message in M.getMessage():
            code.append(tranceF_2( np.dot( message, G.getMatrix() ) ))
        return code

class C:
    #C is a code 
    def __init__(self, G, M):
        self.code = makeCode(G, M)
        self.codeLen = len(self.code)

    def getCode(self):
        return self.code

app = Flask(__name__)

@app.route("/list")
def list():
    books = ["Rasyoumon", "KumonoIto", "Tosisyun"]
    return render_template("list.html", items=books)

@app.route("/Gmatrix")
def Gmatrix():
    g = G()
    m = M()
    c = C(g,m)

    return render_template( "Gmatrix.html", items=g.getMatrix(), code=c.getCode() )
    

    
app.debug = True
app.run()
