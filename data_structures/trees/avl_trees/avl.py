# @file     avl.py
# @brief    A file for implementing an AVL tree
# @author   Jude Thaddeau Data
# @note     GitHub: https://github.com/jtd-117
#           Reference: https://www.programiz.com/dsa/avl-tree
# ---------------------------------------------------------------------------- #

from enum import Enum

# ---------------------------------------------------------------------------- #

class AVL(object):
    """
    An INTERFACE for an AVL tree.
    """

    class CMPValues(Enum):
        """
        The OUTPUT values permitted by `cmp_fn`, a COMPARISON function that 
        takes 2 variables & outputs which of the variables is less than, equal 
        to, or greater than the other.
        """
        LESS = -1
        EQUAL = 0
        GREATER = 1

    class BFValues(Enum):
        """
        BALANCE FACTOR values that indicate whether the LEFT or RIGHT subtrees 
        are taller or equal in height.
        """
        RIGHT = -1
        EQUAL = 0
        LEFT = 1
    
    class Node(object):
        """
        A NODE for an AVL tree.
        """

        def __init__(self, key):
            self._key = key
            self._height = 1
            self._left_child = None
            self._right_child = None
        
        @property
        def key(self):
            """
            The INFORMATION associated with the AVL node.
            """
            return self._key

        @key.setter
        def key(self, new_key):
            self._key = new_key
        
        @key.deleter
        def key(self):
            del self._key

        @property
        def height(self):
            """
            HEIGHT is the number of nodes between a given root node & the farthest 
            lead node.
            """
            return self._height

        @height.setter
        def height(self, new_height):
            self._height = new_height

        @height.deleter
        def height(self):
            del self._height
        
        @property
        def left_child(self):
            """
            The LEFT CHILD of the AVL node: has a key LESS than the parent key.
            """
            return self._left_child
        
        @left_child.setter
        def left_child(self, new_left_child):

            # STEP 1: Ensure `new_left_child` is of type `AVL.Node` or `None`
            if (isinstance(new_left_child, AVL.Node) or (new_left_child is None)):
                self._left_child = new_left_child
                return
            
            # STEP 2: `new_left_child` is an INAPPROPRIATE type
            raise TypeError("`new_left_child` must be of TYPE `AVL.Node` or `None`")

        @left_child.deleter
        def left_child(self):
            del self._left_child

        @property
        def right_child(self):
            """
            The RIGHT CHILD of the AVL node: has a key GREATER or EQUAL to the 
            parent key.
            """
            return self._right_child
        
        @right_child.setter
        def right_child(self, new_right_child):

            # STEP 1: Ensure `new_right_child` is of type `AVL.Node` or `None`
            if (isinstance(new_right_child, AVL.Node) or (new_right_child is None)):
                self._right_child = new_right_child
                return
            
            # STEP 2: `new_right_child` is an INAPPROPRIATE type
            raise TypeError("`new_right_child` must be of TYPE `AVL.Node` or `None`")
        
        @right_child.deleter
        def right_child(self):
            del self._right_child

    def __init__(self, cmp_fn):

        # STEP 1: Ensure `cmp_fn` is a function
        if (not callable(cmp_fn)):
            raise TypeError("`cmp_fn` must be of TYPE 'function'")

        # STEP 2: Assign AVL attributes
        self._cmp_fn = cmp_fn
        self._root = None

    @property
    def cmp_fn(self):
        """
        A custom function for COMPARING `AVL.Node` keys.

        :Parameters:
            - 'v1': The 1st variable for comparison
            - 'v2': The 2nd variable for comparison

        :Return:
            - `1`: if `v1` is GREATER than `v2`, OR
            - `0`: if `v1` & `v2` are EQUAL, OR
            - `-1`: if `v1` is LESS than `v2` 
        """
        return self._cmp_fn

    @cmp_fn.setter
    def cmp_fn(self, new_cmp_fn):

        # STEP 1: Ensure `new_cmp_fn` is of type 'function'
        if (not callable(new_cmp_fn)):
            raise TypeError("`new_cmp_fn` must be of TYPE 'function'")
        
        # STEP 2: Assign the new comparison function
        self._cmp_fn = new_cmp_fn

    @cmp_fn.deleter
    def cmp_fn(self):
        del self._cmp_fn

    @property
    def root(self):
        """
        The TOP or FIRST node in the AVL.
        """
        return self._root
    
    @root.setter
    def root(self, new_root):

        # STEP 1: Ensure `new_root` is of type `AVL.Node` or `None`
        if (isinstance(new_root, AVL.Node) or (new_root is None)):
            self._root = new_root
            return
        
        # STEP 2: `new_root` is an INAPPROPRIATE type
        raise TypeError("`new_root` must be of TYPE `AVL.Node` or `None`")

    @root.deleter
    def root(self):
        del self._root

    def __node_height(self, node):
        """
        RETRIEVES the height of a given AVL `node`

        :Parameters:
            - `node`: The AVL node to retrieve it's from

        :Return:
            The HEIGHT of the AVL node
        """

        # CASE A: Nodes does not exist
        if (not node):
            return 0

        # CASE B: Node is an inappropriate type:
        elif (not isinstance(node, AVL.Node)):
            raise TypeError("`node` must be of TYPE `AVL.Node`")
    
        # CASE C: Return the height of the node
        return node.height

    def __balance_factor(self, node):
        """
        CALCULATES & returns the HEIGHT DIFFERENCE between the LEFT & RIGHT 
        subtrees for a given `node` node.

        :Parameters:
            - `node`: The AVL node to calculate the balance factor of

        :Return:
            The BALANCE FACTOR of the AVL node.
        """

        # CASE A: Node does NOT exist
        if not node:
            return 0

        # CASE B: Node is an inappropriate type:
        elif (not isinstance(node, AVL.Node)):
            raise TypeError("`node` must be of TYPE `AVL.Node`")
        
        # CASE C: Calculate the balance factor
        return (self.__node_height(node.left_child) 
                - self.__node_height(node.right_child))

    def __left_rotate(self, node):
        """
        LEFT ROTATES `node` by having it take the position of it's left child 
        & have the right child of `node` take it's original position.

        :Parameters:
            - `node`: The node to LEFT rotate

        :Return:
            A pointer to the child node that replaced the position of `node`
        """
        
        # STEP 1: INITALISE the NEW parent & right child nodes of `node`
        node_p = node.right_child
        node_rc = node_p.left_child

        # STEP 2: ASSIGN the NEW parent & right child nodes of `node`
        node_p.left_child = node
        node.right_child = node_rc

        # STEP 3: Calculate the new HEIGHTS for `node` & it's parent
        node.height = 1 + max(self.__node_height(node.left_child), 
                            self.__node_height(node.right_child))
        node_p.height = 1 + max(self.__node_height(node_p.left_child), 
                            self.__node_height(node_p.right_child))
        return node_p

    def __right_rotate(self, node):
        """
        RIGHT ROTATES `node` by having it take the position of it's right 
        child & have the left child of `node` take it's original position.

        :Parameters:
            - `node`: The node to RIGHT rotate

        :Return:
            A pointer to the child node that replaced the position of `node`
        """
        
        # STEP 1: INITALISE the NEW parent & left child nodes of `node`
        node_p = node.left_child
        node_lc = node_p.right_child

        # STEP 2: ASSIGN the NEW parent & left child nodes of `node`
        node_p.right_child = node
        node.left_child = node_lc

        # STEP 3: Calculate the new HEIGHTS for `node` & it's parent
        node.height = 1 + max(self.__node_height(node.left_child), 
                            self.__node_height(node.right_child))
        node_p.height = 1 + max(self.__node_height(node_p.left_child), 
                            self.__node_height(node_p.right_child))
        return node_p
    
    def insert_node(self, key):
        """
        WRAPPER function for inserting an AVL node recursively.

        :Paramters:
            - `key`: the key to be associated with the new node
        """

        # STEP 1: Perfrom the AVL node insertion recursively
        self.root = self.__recursive_insert(self.root, key)

    def __recursive_insert(self, root, key):
        """
        INSERTS a new AVL node RECUSIVELY.

        :Parameters:
            - `root`: The 1st node in the AVL tree
            - `key`: The KEY of the new AVL node to be inserted

        :Return:
            A POINTER to the newly inserted AVL node
        """

        # STEP 1: Find the location to insert new node & calculate it's height
        if not root:
            return AVL.Node(key)
        elif (self.cmp_fn(key, root.key) == AVL.CMPValues.LESS.value):
            root.left_child = self.__recursive_insert(root.left_child, key)
        else:
            root.right_child = self.__recursive_insert(root.right_child, key)
        root.height = 1 + max(self.__node_height(root.left_child), 
                            self.__node_height(root.right_child))

        # STEP 2: Update the balance factor of the AVL tree
        balance_factor = self.__balance_factor(root)

        # CASE 2A: Height of the LEFT subtree > RIGHT subtree
        if (balance_factor > AVL.BFValues.LEFT.value):

            # CASE 2AI: Inserted via RIGHT child (i.e. inside roation), 
            #           1 rotation needed (i.e. right rotate)
            if (key < root.left_child.key):
                return self.__right_rotate(root)

            # CASE 2AII: Inserted via RIGHT child (i.e. inside roation), 
            #            2 rotations needed (i.e. left-right rotation)
            else:
                root.left_child = self.__left_rotate(root.left_child)
                return self.__right_rotate(root)

        # CASE 2B: Height of the LEFT subtree < RIGHT subtree
        if (balance_factor < AVL.BFValues.RIGHT.value):

            # CASE 2BI: Inserted via RIGHT child (i.e. inside roation), 
            #           1 rotation needed (i.e. left rotate)
            if (key > root.right_child.key):
                return self.__left_rotate(root)

            # CASE 2BII: Inserted via RIGHT child (i.e. inside roation), 
            #            2 rotations needed (i.e. right-left rotation)
            else:
                root.right_child = self.__right_rotate(root.right_child)
                return self.__left_rotate(root)
        return root

    def min_node(self, root):
        """
        RETRIEVES the AVL node with the SMALLEST key value.

        :Paramters:
            - `root`: is the ROOT node of the entire AVL or subtree

        :Return:
            A POINTER to the AVL node with the SMALLEST key value
        """
        
        # STEP 1: Ensure the `root` is a valid AVL node
        if (not isinstance(root, AVL.Node)):
            raise TypeError("`root` must be of TYPE `AVL.Node`")
        
        # STEP 2: Keep traversing the LEFT-most child provided one exists
        curr_node = root
        while (curr_node.left_child != None):
            curr_node = curr_node.left_child
        return curr_node

    def max_node(self, root):
        """
        RETRIEVES the AVL node with the LARGEST key value.

        :Paramters:
            - `root`: is the ROOT node of the entire AVL or subtree

        :Return:
            A POINTER to the AVL node with the LARGEST key value
        """

        # STEP 1: Ensure the `root` is a valid AVL node
        if (not isinstance(root, AVL.Node)):
            raise TypeError("`root` must be of TYPE `AVL.Node`")

        # STEP 2: Keep traversing the RIGHT-most child provided one exists
        curr_node = root
        while (curr_node.right_child != None):
            curr_node = curr_node.right_child
        return curr_node

    def predecessor_node(self, node):
        """
        FINDS the AVL node whose key comes BEFORE the current `node`.

        :Parameters:
            - `node`: the AVL node to find the PREDECESSOR of

        :Return:
            - A POINTER to the PREDECESSOR AVL node of parameter `node`, OR
            - `None`: if NO predecessor exists
        """
        
        # STEP 1: AVL tree is EMPTY (i.e. no predecessor)
        if not node:
            return None

        # STEP 2: node is an inappropriate type
        if (not isinstance(node, AVL.Node)):
            raise TypeError("`node` must be of TYPE `AVL.Node`")

        # STEP 3: Initialise the root node to search
        parent_node = None
        curr_node = self.root
        while True:

            # STEP 3A: `curr_node` is NOT the predecessor upon LEFT traversal
            if (self.cmp_fn(node.key, curr_node.key) == AVL.CMPValues.LESS.value):
                curr_node = curr_node.left_child

            # STEP 3B: `curr_node` MIGHT be the predecessor upon RIGHT traversal
            elif (self.cmp_fn(node.key, curr_node.key) == AVL.CMPValues.GREATER):
                parent_node = curr_node
                curr_node = curr_node.right_child

            # STEP 3C: MATCHING keys ensures predecessor is MAX node of the 
            #          left child OR `None`
            else:
                if (curr_node.left_child != None):
                    parent_node = self.max_node(curr_node.left_child)
                break
                
            # STEP 3D: Traversed to an EMPTY node (i.e. no predecessor)
            if (curr_node is None):
                return parent_node

        # STEP 4: Return the predecessor node
        return parent_node

    def successor_node(self, node):
        """
        FINDS the AVL node whose key comes AFTER the current `node`.

        :Parameters:
            - `node`: the AVL node to find the SUCCESSOR of

        :Return:
            - A POINTER to the SUCCESSOR AVL node of parameter `node`, OR
            - `None`: if NO successor exists
        """

        # STEP 1: AVL tree is EMPTY (i.e. no successor)
        if not node:
            return None

        # STEP 2: node is an inappropriate type
        if (not isinstance(node, AVL.Node)):
            raise TypeError("`node` must be of TYPE `AVL.Node`")

        # STEP 3: Initialise the root node to search
        parent_node = None
        curr_node = self.root
        while True:

            # STEP 3A: `curr_node` MIGHT be the successor upon LEFT traversal
            if (self.cmp_fn(node.key, curr_node.key) == AVL.CMPValues.LESS.value):
                parent_node = curr_node
                curr_node = curr_node.left_child

            # STEP 3B: `curr_node` is NOT the successor upon RIGHT traversal
            elif (self.cmp_fn(node.key, curr_node.key) == AVL.CMPValues.GREATER.value):
                curr_node = curr_node

            # STEP 3C: MATCHING keys ensures successor is the MIN node of the 
            #          right child OR `None`
            else:
                if (curr_node.right_child != None):
                    parent_node = self.max_node(curr_node.right_child)
                break

            # STEP 3D: Traversed to an EMPTY node (i.e. no successor)
            if (curr_node is None):
                return parent_node
            
        # STEP 4: Return the successor node
        return parent_node

    def delete_node(self, root, key):
        """
        DELETES an AVL node RECURSIVELY.

        :Parameters:
            - `root`: The 1st node in the AVL tree
            - `key`: The node to be deleted with the same key
        """
        
        # STEP 1: Find the node to be deleted & delete it
        if (not root):
            return root

        elif (self.cmp_fn(key, root.key) == AVL.CMPValues.LESS.value):
            root.left_child = self.delete_node(root.left_child, key)

        elif (self.cmp_fn(key, root.key) == AVL.CMPValues.GREATER.value):
            root.right_child = self.delete_node(root.right_child, key)

        else:
            
            # CASE 1A: Node to be deleted has ONE child (i.e. RIGHT child)
            if (root.left_child is None):
                temp = root.right_child
                root = None
                return temp

            # CASE 1B: Node to be deleted has ONE child (i.e. LEFT child)
            elif (root.right_child is None):
                temp = root.left_child
                root = None
                return temp

            # STEP 2: Node to be deleted has TWO childrennodes
            temp = self.min_node(root.right_child)
            root.key = temp.key
            root.right_child = self.delete_node(root.right_child, temp.key)

        # STEP 3: Node to be deleted has ONE child
        if (root is None):
            return None

        # STEP 4: Update ancestor node height & get balance factor
        root.height = 1 + max(self.__node_height(root.left_child), 
                            self.__node_height(root.right_child))
        balance_factor = self.__balance_factor(root)

        # CASE 5A: Need to balance the LEFT subtree
        if (balance_factor > AVL.BFValues.LEFT.value):
            
            # CASE 5AI: LEFT subtree outside rotation
            if (self.__balance_factor(root.left_child) >= AVL.BFValues.EQUAL.value):
                return self.__right_rotate(root)

            # CASE 5AII: LEFT subtree inside rotation
            else:
                root.left_child = self.__left_rotate(root.left_child)
                return self.__right_rotate(root)

        # CASE 5B: Need to balance the RIGHT subtree
        if (balance_factor < AVL.BFValues.RIGHT.value):
            
            # CASE 5BI: RIGHT subtree outside rotation
            if (self.__balance_factor(root.right_child) <= AVL.BFValues.EQUAL.value):
                return self.__left_rotate(root)

            # CASE 5BII: RIGHT subtree inside rotation
            else:
                root.right_child = self.__right_rotate(root.right_child)
                return self.__left_rotate(root)
        return root

    def inorder_walk(self, root, operation = print):
        """
        Performs a tree TRAVERSAL in the following order:
        1. LEFT subtree
        2. ROOT node
        3. RIGHT subtree

        :Parameters:
            - `root`: the ROOT node of the AVL
            - `operation`: a function (default `print`) that specifies the 
              ACTION to be performed on the KEY of every visited AVL node
        """
        
        # STEP 1: Ensure the root is not NULL
        if root:
            self.inorder_walk(root.left_child)
            operation(root.key)
            self.inorder_walk(root.right_child)

    def preorder_walk(self, root, operation = print):
        """
        Performs a tree TRAVERSAL in the following order:
        1. ROOT node
        2. LEFT subtree
        3. RIGHT subtree

        :Parameters:
            - `root`: the ROOT node of the AVL
            - `operation`: a function (default `print`) that specifies the 
              ACTION to be performed on the KEY of every visited AVL node
        """
        
        # STEP 1: Ensure the root is not NULL
        if root:
            operation(root.key)
            self.preorder_walk(root.left_child)
            self.preorder_walk(root.right_child)

    def postorder_walk(self, root, operation = print):
        """
        Performs a tree TRAVERSAL in the following order:
        1. LEFT subtree
        2. RIGHT subtree
        3. ROOT node

        :Parameters:
            - `root`: the ROOT node of the AVL
            - `operation`: a function (default `print`) that specifies the 
              ACTION to be performed on the KEY of every visited AVL node
        """
        
        # STEP 1: Ensure the root is not NULL
        if root:
            self.postorder_walk(root.left_child)
            self.postorder_walk(root.right_child)
            operation(root.key)

    def __iterative_search(self, target_key):
        """
        ITERATIVELY searches the AVL for a node with `target_key`.

        :Parameters:
            - `target_key`: the INFORMATION to search for in the AVL

        :Return:
            - A POINTER to the AVL node that MATCHES the `target_key`, OR
            - `None`: if NO match was found
        """
        
        # STEP 1: Intialise the search at the root node & traverse
        curr = self.root
        while curr:

            # STEP 1A: `target_key` is LARGER (i.e. traverse to RIGHT)
            if (self.cmp_fn(target_key, curr.key) == AVL.CMPValues.GREATER.value):
                curr = curr.right_child

            # STEP 1B: `target_key` is SMALLER (i.e. traverse to LEFT)
            elif (self.cmp_fn(target_key, curr.key) == AVL.CMPValues.LESS.value):
                curr = curr.left_child
            
            # STEP 1C: Found a match
            else:
                return curr

        # STEP 2: No match detected
        return None

    def __recursive_search(self, root, target_key):
        """
        RECURSIVELY searches the AVL for a node with `target_key`.

        :Parameters:
            - `root`: the 1st node the AVL
            - `target_key`: the INFORMATION to search for in the AVL

        :Return:
            - A POINTER to the AVL node that MATCHES the `target_key`, OR
            - `None`: if NO match was found
        """
        
        # BASE CASE 1: No matches found
        if (root == None):
            return None

        # BASE CASE 2: Match found
        elif (self.cmp_fn(target_key, root.key) == AVL.CMPValues.EQUAL.value):
            return root

        # RECURSIVE CASE 1: `target_key` is LARGER (i.e. traverse to RIGHT)
        elif (self.cmp_fn(target_key, root.key) == AVL.CMPValues.GREATER.value):
            return self.__recursive_search(root.right_child, target_key)

        # RECURSIVE CASE 2: `target_key` is SMALLER (i.e. traverse to LEFT)
        else:
            return self.__recursive_search(root.left_child, target_key)

    def search(self, target_key, mode = 'r'):
        """
        SEARCHES the AVL for a node with `target_key`.

        :Parameters:
            - `target_key`: the INFORMATION to search for in the AVL
            - `mode`(optional): a SINGLE character `str` that indicates if  
              the AVL search is conducted iteratively 'i' (default), or 
              recursively 'r'

        :Return:
            - A POINTER to the AVL node that MATCHES the `target_key`, OR
            - `None`: if NO match was found
        """

        # CASE A: Mode is an INAPPROPRIATE type
        if (not isinstance(mode, str)):
            raise TypeError("`mode` must of TYPE `str`")
        
        # CASE B: Perform the search ITERATIVELY
        elif (mode == 'i'):
            return self.__iterative_search(target_key)

        # CASE C: Perform the search RECURSIVELY
        elif (mode == 'r'):
            return self.__recursive_search(self.root, target_key)

        # CASE D: Mode is an INAPPROPRIATE value
        else:
            raise ValueError("`mode` must be of VALUE 'i' or 'r'")