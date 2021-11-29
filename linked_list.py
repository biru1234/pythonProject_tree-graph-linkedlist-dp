'''
linked list ko tree jaisa ek hi class se nahi kar paa rahe hai since waha root se start hai joa khud
node hai and yaha link list mai sabkuch head se start hai joa ki ek pointer hai isliye dusra class
se easy hai
'''



class Node():
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link
# ye node ka woa address lega joa head rakh hai and insert at begining mai joa create hoga node
#uska link mai yahi dalna joa head rakha hai isliye at argumenet mai self ka head hi dal doa
#kuch or karne ka required hoga


class linkedlist():
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):

        node = Node(data, self.head)
        self.head = node

    def insert_at_last(self, data):
        node = Node(data)
        itr = self.head
        while itr.link:
            itr = itr.link
        itr.link = node

    def traveal(self):
        itr=self.head
        while itr:
            print(itr.data)
            itr=itr.link

    def insert_at_n_position(self, data,pos):
        itr = self.head
        count=1
        while itr:
            if count==pos:
                node = Node(data)
                node.link=itr.link
                itr.link = node
                break
            itr=itr.link
            count=count+1
    def delete_data(self,data):
        itr = self.head
        if itr.data==data:
            self.head=itr.link
        pre_itr=self.head
        itr = itr.link

        while itr:
            if itr.data==data:
                pre_itr.link=itr.link
                break
            pre_itr=itr
            itr = itr.link

    def middle_data(self):
        slow_itr=self.head
        fast_itr=self.head
        #slow itr ko ignore kar sakta hoa but fast_itr and fast_itr.link dono must hai
        #since even case mai hota hai fast itr end walea  mai aa jata hai and end ke link none hai and
        #none ke link try karoge toa error ayega isliye fast_itr must hai
        #and fast_itr.link ye must hai kyu ki humlog iss fast itr ko 2 increse kar rahe hai and kiska ka
        #link none nahi hai toa ek woa hoa jayega and next none hoa jayega mtlb sure hai 2 milega no error

        while slow_itr and fast_itr and fast_itr.link:
            slow_itr=slow_itr.link
            fast_itr=fast_itr.link
            fast_itr = fast_itr.link
        print(slow_itr.data)





if __name__=='__main__':
    l1=linkedlist()
    l1.insert_at_begining(9)
    l1.insert_at_begining(7)
    l1.insert_at_begining(5)
    l1.insert_at_begining(4)
    #l1.insert_at_begining(3)
    '''l1.insert_at_begining(2)
    l1.insert_at_begining(1)
    l1.insert_at_begining(11)'''
    l1.traveal()
    #print("now delete ")
    '''l1.insert_at_last(20)
    l1.insert_at_last(25)
    l1.insert_at_last(30)
    l1.traveal()
    l1.insert_at_n_position(55,2)
    l1.insert_at_n_position(44, 1)
    l1.insert_at_n_position(99, 7)
    l1.traveal()'''
    #l1.delete_data(7)
    l1.middle_data()


