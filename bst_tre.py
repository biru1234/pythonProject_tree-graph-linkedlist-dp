'''
isko linked list jaisa 2 class se nahi kar sake since waha starting head se joa node ka part nahi hai
and tree mai node se since satrt root se joa ek node hai
'''

'''
hint: yaha sabkuch self hi hai traveal bhi karn hai toa self se satrt kar and jab phir se iss node
se dusre iske ledt mai aye toa toa self.left se method ko call karao
'''


def max1(a,b):
    return a if a>b else b
class bst:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def create_child(self,data):
        if self.data==data:
            return
        if self.data>data:
            if self.left:
                self.left.create_child(data)
            else:
                self.left=bst(data)
        else:
            if self.right:
                self.right.create_child(data)
            else:
                self.right=bst(data)

    #break must hai since last mai value add hoga and woa kabhi end nahi kareg and woa infinite loop banandegga

    def created_child_my(self,data):
        itr = self
        while itr:
            if itr.data>data:
                if itr.left:
                    itr=itr.left
                else:
                    itr.left=bst(data)
                    break
            else:
                if itr.right:
                    itr=itr.right
                else:
                    itr.right=bst(data)
                    break

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        #print(self)
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)

    def find_min(self):
        if self.left:
            self.left.find_min()
        else:
            return self.data


    def deleting(self,data):#can't use prev kahe ki ye bus ek var type ka kaam karega yaha object ka nahi hai
        if self.data>data:
            if self.left:
                self.left=self.left.deleting(data)
            else:
                return None
        elif self.data<data:
            if self.right:
                self.right=self.right.deleting(data)
            else:
                return None
        else:
            if ((self.left is None) and (self.right is None)):
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data=min_val
            self.right=self.right.deleting(min_val)
        return self# last ka jiska delete karn hai woa apna return kar hi raha hai and uske pahele wale jisea se call
        #hua hai wahi return kar doa easy ---

    def height1(self):
        if self is None:
            return 0
        left1 =0
        right1 = 0
        if self.left is not None:
            left1 = self.left.height1()
        if self.right is not None:
            right1 = self.right.height1()
        return 1+max1(left1,right1)

    def leaf(self):
        if self.left is not None:
            self.left.leaf()
        if self.left is None and self.right is None:
            print(self.data)
        if self.right is not None:
            self.right.leaf()



if __name__=='__main__':
    root=bst(50)
    '''root.create_child(30)
    root.create_child(70)
    root.create_child(40)
    root.create_child(60)
    root.create_child(25)'''
    #root.inorder()
    # inorder = 25 30 40 50 60 70
    #root.preorder()
    #pre= 50 30 25 40 70 60
    #root.postorder()
    #post = 25 40 30 60 70 50
    #root.testing()
    root.created_child_my(30)
    root.created_child_my(70)
    root.created_child_my(40)
    root.created_child_my(60)
    root.created_child_my(25)
    #root.inorder()
    #root.deleting(40)
    #print("after dellete")
    root.inorder()
    print("height of tree")
    print(root.height1())
    print("leaf nodes are")
    root.leaf()



