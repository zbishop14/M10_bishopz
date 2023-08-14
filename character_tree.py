# Our natoCodeWord tree uses a Node with data - but we don't need an extra nato attribute
# Our data will be a NATO code word (String)
class Node(object):  # One part of the Morse Tree. natoCodeWord is none if it isn't a decode Node, or hasn't been populated yet
    def __init__(self, natoCodeWord, character):  # Constructor
        self.natoCodeWord = natoCodeWord  # The data object for this Node
        self.left = None  # the left child
        self.right = None  # the right child
        # Using NATO alphabet like a nato
        self.character = character

    def __str__(self):
        return str(self.natoCodeWord)


class CharacterTree(object):  # a  binary search tree for NATO

    def __init__(self):  # Constructor
        self.__root = None  # root node in

    # add (aka insert)
    # this function does NOT keep the tree balanced
    # Rules for data struct functions:
    # 1. before function is called, we have a valid data structure (BST)
    # 2. update all attributes (root, size, left and right of Nodes)
    # 3. on the way out, the function must leave the data structure valid
    def add(self, natoCodeWord, character):  # we decided that adding is log(N) (LOG BASE 2)
        nodeToAdd = Node(natoCodeWord, character)  # QoL improvement, hide Nodes from user
        cur = self.__root  # the current Node we are looking at

        if cur is None:  # For empty trees, insert new node at root
            self.__root = nodeToAdd  # root of tree
        else:
            # we at least have a root already
            lookingForSpot = True

            while lookingForSpot:

                if character < cur.character:  # updated for character. If new data is less cur's data, go left
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
    def find(self, characterToFind):  # takes character key, NOT a Node. Also O(log(N))
        nodeWeFound = None

        cur = self.__root  # the current Node we are looking at

        if cur is not None:
            # we at least have a root already
            lookingForSpot = True

            while lookingForSpot:
                if characterToFind < cur.character:  # updated for nato. If new data is less cur's data, go left
                    if cur.left is None:  # if there isn't a left, we aren't gonna find it
                        lookingForSpot = False
                    else:
                        cur = cur.left  # equivalent of cur = cur.next in LL. Meaning keeping going
                elif characterToFind > cur.character:  # Otherwise > look right
                    if cur.right is None:  # if there isn't a right, we aren't gonna find it
                        lookingForSpot = False
                    else:
                        cur = cur.right
                else:  # we found it!
                    nodeWeFound = cur
                    lookingForSpot = False
        return nodeWeFound

    def Encode(self, natoToEncode):
        natoCodeWord = self.find(natoToEncode)
        return natoCodeWord

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

        message = self.inorderTraversalHelper(cur.left)  # this is tricky (being = )
        message += f"{cur}, "
        message += self.inorderTraversalHelper(cur.right)
        return message
