class Node(object):
    def __init__(self, d, r=None): #constructor that declares all the variables that you will need for the getter setter methods. you will need the data variable for the node data. you will need the next variable for the next node.
        self.data = d
        self.next = r
    def get_next(self):
        return self.next
    def set_next(self, n):
        self.next = n
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d


class Solution(object):
    def __init__(self, r=None):  # Constructor
        self.root = None
        self.size = 0  # declaring variables in the constructor. that is what the constructor is for. you define variables that you will be using in the subsequent functions

    def mergeTwoLists(self, l1, l2):
        l1 = l1.root
        l2 = l2.root
        while l2.next:
            if l1.next:
                while l1.next:
                    if l2.get_data() <= l1.get_data():
                        l2.set_next(l1.get_next())
                        l1.set_next(l2)
                        l1 = l1.next
                    else:
                        l1 = l1.next
                return l1.data
            else:
                break
            l2 = l2.next
            self.displayNode(l1)



class LinkedList(object):
    def __init__(self, r=None):  # Constructor
        self.root = None
        self.size = 0  # declaring variables in the constructor. that is what the constructor is for. you define variables that you will be using in the subsequent functions

    def get_size(self, n):
        return self.size

    def addNode(self, d):
        new_node = Node(d, self.root) #create a new node of the type Node
        self.root = new_node          #make the new node the root node
        self.size += 1                #increment the size of the linked list by 1

    def removeNode(self, d):
        this_node = self.root       #to remove a node. you need to remove the link from previous node and link it to the next node of the current node
        prev_node = None            #hence this_node and prev_node

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()

    def find(self, d):
        this_node = self.root
        while (this_node):
            if this_node.get_data() == d:
                return
            else:
                this_node = this_node.get_next()
        return False

    def displayNode(self, n):
        temp = n.root
        while temp!=None:
            if(temp.get_next()!=None):
                print (str (temp.get_data())+ " ->"),
                temp = temp.get_next()
            else:
                print (str(temp.get_data()))
                temp = None
                return

    def insertNodeAtPosition(self, d, position):
        this_node = self.root
        prev_node = None
        if position > self.size:
            print "Can`'t insert the value at " +str(position)+ "th position. Out of range."
        elif position == 1:
            print "Inserting " + str(d) + " at 1st position."
            new_node = Node(d, self.root)  # create a new node of the type Node
            self.root = new_node  # make the new node the root node
            self.size += 1
        else:
            print "Inserting " + str(d) + " at " + str(position) + "th position."
            if position==0:
                print "Choose a valid position starting from 1."
            elif position>self.size:
                print "Range out of bounds. Enter a valid position."
            elif position>=1:
                while position-1>1:
                    this_node = this_node.get_next()
                    position-=1
                new_node = Node(d, self.root)
                self.size += 1
                new_node.set_next(this_node.get_next())
                this_node.set_next(new_node)

    def insertNodeAfterValue(self, d, value):
            this_node = self.root
            new_node = Node(d, self.root)
            while this_node!=None:
                if this_node.get_data()==value:
                    print "Inserting " + str(d) + " after " + str(value) + "."
                    new_node.set_next(this_node.get_next())
                    this_node.set_next(new_node)
                    self.size += 1
                    return
                this_node = this_node.get_next()

    def reverseSinglyLinkedList(self, list):
        this_node = list.root
        prev_node = None
        while this_node!=None:
            self.next = this_node.get_next()
            this_node.set_next(prev_node)
            prev_node = this_node
            this_node = self.next
        self.root = prev_node
        return str(prev_node.get_data())

    def removeDuplicates(self):
        this_node = self.root
        print "Removing duplicates"
        while this_node is not None and this_node.get_next() is not None:
            if this_node.data == this_node.next.data:
                this_node.next = this_node.next.next
            else:
                this_node = this_node.next
        return this_node.get_data()


    def mergeTwoLists1(self, l1, l2):
            temp = cur = Node(0)
            l1 = l1.root
            l2=l2.root
            while l1 and l2:
                if l1.data < l2.data:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2

            while temp != None:
                if (temp.get_next() != None):
                    print (str(temp.get_data()) + " ->"),
                    temp = temp.get_next()
                else:
                    print (str(temp.get_data()))
                    temp = None
                    return

    # def reverseLinkedList(self, head):
    #     slow = head.root
    #     fast = head.root.next
    #
    #     arr = []
    #     while head:
    #         if

    def hasCycle(self, list):
        list = list.root
        slow = list
        fast = list.next
        while slow!=fast:
            if fast == None or fast.next == None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True

    def isPalindrome(self, head):
        head = head.root
        pal = []
        while head!=None:
            pal.append(head.data)
            head = head.next
        return pal == pal[::-1]

    def removeElements(self, head, val):
        head = head.root
        temp = Node(-1)
        temp.next = head
        prev = temp
        curr = temp.next

        while curr:
            if curr.data == val:
                prev.next = curr.next
                curr = curr.next
                continue
            prev = prev.next
            curr = curr.next
        return temp.next


def main():
    myList1 = LinkedList()
    s = Solution()

    myList1.addNode(1)
    myList1.addNode(1)


    print "----------------------------------"
    myList1.displayNode(myList1)

    myList1.removeElements(myList1, 1)

    print "----------------------------------"
    myList1.displayNode(myList1)

if __name__ == "__main__":
    main()

