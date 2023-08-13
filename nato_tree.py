from linked_list import LinkedList
# Our NATO Phonetic Alphabet tree uses a Node with data - but we don't need an extra nato attribute
# Our data will be a character (String)
class Node(object):  # One part of the Morse Tree. character is none if it isn't a decode Node, or hasn't been populated yet
    def __init__(self, character, natoKey):  # Constructor
        self.character = character  # The data object for this Node
        self.left = None  # the left child
        self.right = None  # the right child
        # Using NATO alphabet like a nato
        self.natoKey = natoKey

    def __str__(self):
        return str(self.character)

class NatoTree(object):  # a  binary search tree for NATO

    def __init__(self):  # Constructor
        self.__root = None    # root node in

    # add (aka insert)
    # this function does NOT keep the tree balanced
    # Rules for data struct functions:
    # 1. before function is called, we have a valid data structure (BST)
    # 2. update all attributes (root, size, left and right of Nodes)
    # 3. on the way out, the function must leave the data structure valid
    def add(self, character, natoKey): # we decided that adding is log(N) (LOG BASE 2)
        nodeToAdd = Node(character, natoKey) # QoL improvement, hide Nodes from user
        cur = self.__root  # the current Node we are looking at

        if cur is None:  # For empty trees, insert new node at root
            self.__root = nodeToAdd  # root of tree
        else:
            # we at least have a root already
            lookingForSpot = True

            while lookingForSpot:

                if natoKey < cur.natoKey:  # updated for nato. If new data is less cur's data, go left
                    if cur.left is None:  # if there is a open spot
                        cur.left = nodeToAdd
                        lookingForSpot = False
                    else:
                        cur = cur.left  # equivalent of cur = cur.next in LL. Meaning keeping going
                else:  # Otherwise >= look right
                    if cur.right is None:
                        cur.right = nodeToAdd
                        lookingForSpot = False
                    else:
                        cur = cur.right  # equivalent of cur = cur.next in LL. Meaning keeping going


# return the Object (data) if found, or None
    def find(self, natoToFind): # takes nato key, NOT a Node. Also O(log(N))
        nodeWeFound = None

        cur = self.__root  # the current Node we are looking at

        if cur is not None:
            # we at least have a root already
            lookingForSpot = True

            while lookingForSpot:
                if natoToFind < cur.natoKey:  # updated for nato. If new data is less cur's data, go left
                    if cur.left is None:  # if there isn't a left, we aren't gonna find it
                        lookingForSpot = False
                    else:
                        cur = cur.left  # equivalent of cur = cur.next in LL. Meaning keeping going
                elif natoToFind > cur.natoKey:  # Otherwise > look right
                    if cur.right is None: # if there isn't a right, we aren't gonna find it
                        lookingForSpot = False
                    else:
                        cur = cur.right
                else: # we found it!
                    nodeWeFound = cur
                    lookingForSpot = False
        return nodeWeFound

    def __str__(self):
        return self.inorderTraversal()

    # does this need updating for Morse Tree??
    def inorderTraversal(self):
        message = ""
        message = self.inorderTraversalHelper(self.__root)
        return message

    def inorderTraversalHelper(self, cur):

        if cur is None:
            return ""

        message = self.inorderTraversalHelper(cur.left) # this is tricky (being = )
        message += f"{cur}, "
        message += self.inorderTraversalHelper(cur.right)
        return message
