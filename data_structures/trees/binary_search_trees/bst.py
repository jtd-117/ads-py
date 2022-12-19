# @file     bst.py
# @brief    A file for implementing a binary search tree (BST)
# @author   Jude Thaddeau Data
# @note     GitHub: https://github.com/jtd-117
# ---------------------------------------------------------------------------- #

class BSTNode(object):
    """
    A NODE for a binary search tree (BST).
    """

    def __init__(self, key):
        self._key = key
        self._p = None
        self._rc = None
        self._lc = None
  
    @property
    def key(self):
        """
        The INFORMATION associated with the BST node.
        """
        return self._key
    
    @key.setter
    def key(self, newKey):
        self._key = newKey

    @key.deleter
    def key(self):
        del self._key

    @property
    def p(self):
        """
        The PARENT node of the current BST node.
        """
        return self._p

    @p.setter
    def p(self, new_parent):

        # STEP 1: Ensure `new_parent` is of type `BSTNode` or `None`
        if (isinstance(new_parent, BSTNode) or (new_parent is None)):
            self._p = new_parent
            return
        
        # STEP 2: `new_parent` is an INAPPROPRIATE type
        raise TypeError("`new_parent` must be of TYPE `BSTNode` or `None`")
    
    @p.deleter
    def p(self):
        del self._p

    @property
    def rc(self):
        """
        The RIGHT CHILD of the BST node: has a key GREATER or EQUAL to the 
        parent key.
        """
        return self._rc
    
    @rc.setter
    def rc(self, rc):

        # STEP 1: Ensure `rc` is of type `BSTNode` or `None`
        if (isinstance(rc, BSTNode) or (rc is None)):
            self._rc = rc
            return
        
        # STEP 2: `rc` is an INAPPROPRIATE type
        raise TypeError("`rc` must be of TYPE `BSTNode` or `None`")
    
    @rc.deleter
    def rc(self):
        del self._rc

    @property
    def lc(self):
        """
        The LEFT CHILD of the BST node: has a key LESS than the parent key.
        """
        return self._lc
    
    @lc.setter
    def lc(self, lc):

        # STEP 1: Ensure `lc` is of type `BSTNode` or `None`
        if (isinstance(lc, BSTNode) or (lc is None)):
            self._lc = lc
            return
        
        # STEP 2: `lc` is an INAPPROPRIATE type
        raise TypeError("`lc` must be of TYPE `BSTNode` or `None`")

    @lc.deleter
    def lc(self):
        del self._lc   

# ---------------------------------------------------------------------------- #

class BST(object):
    """
    An INTERFACE for a binary search tree (BST).
    """

    # CLASS ATTRIBUTES:
    cmp_greater = 1
    cmp_equal = 0
    cmp_less = -1

    def __init__(self, cmp_fn):

        # STEP 1: Ensure `cmp_fn` is a function
        if (not callable(cmp_fn)):
            raise TypeError("`cmp_fn` must be of TYPE 'function'")

        # STEP 2: Assign BST attributes
        self._cmp_fn = cmp_fn
        self._root = None

    @property
    def cmp_fn(self):
        """
        A custom function for COMPARING `BSTNode` keys.

        :Parameters:
            - 'v1': The 1st variable for comparison
            - 'v2': The 2nd variable for comparison

        :Return:
            - `1`: if `v1` is GREATER than `v2` 
            - `0`: if `v1` & `v2` are EQUAL
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
        The TOP or FIRST node in the BST.
        """
        return self._root
    
    @root.setter
    def root(self, new_root):

        # STEP 1: Ensure `new_root` is of type `BSTNode` or `None`
        if (isinstance(new_root, BSTNode) or (new_root is None)):
            self._root = new_root
            return
        
        # STEP 2: `new_root` is an INAPPROPRIATE type
        raise TypeError("`new_root` must be of TYPE `BSTNode` or `None`")

    @root.deleter
    def root(self):
        del self._root

    def __iterative_insert(self, new_node):
        """
        INSERTS a new BST node ITERATIVELY.

        :Parameters:
            - `new_node`: the node to be inserted into the BST
        
        :Return:
            A POINTER to the newly inserted BST node
        """
        
        # STEP 1: Initialise the new BST node & pointers
        prev = None
        curr = self.root

        # STEP 2: Traverse the BST to an empty slot
        while (curr):
            prev = curr

            # CASE 2A: Traverse LEFT child, key is LESS
            if (self.cmp_fn(new_node.key, curr.key) == self.cmp_less):
                curr = curr.lc

            # CASE 2B: Traverse RIGHT child, key is GREATER than or EQUAL
            else:
                curr = curr.rc

        # STEP 3: Found a spot to insert into the BST, assign parent node
        new_node.p = prev

        # STEP 4A: BST is EMPTY, insert at the ROOT
        if (prev is None):
            self._root = new_node

        # STEP 4B: Inserted node's key is LESS
        elif (self.cmp_fn(new_node.key, prev.key) == self.cmp_less):
            prev.lc = new_node

        # STEP 4C: Inserted node'skey is GREATER than or EQUAL to
        else:
            prev.rc = new_node
        return new_node

    def __recursive_insert(self, new_node, root, root_parent = None):
        """
        INSERTS a new BST node RECURSIVELY.

        :Parameters:
            - `new_node`: The node to be inserted into the BST
            - `root`: The 1st node in the BST
            - `root_parent` (optional): The PARENT node of `root`
        
        :Return:
            A POINTER to the newly inserted BST node
        """
        
        # BASE CASE: Traversed into an EMPTY slot in the BST
        if (root is None):
            new_node.p = root_parent
            return new_node
        
        # RECURSIVE CASE 1: Traverse LEFT
        if (self.cmp_fn(new_node.key, root.key) == self.cmp_less):
            root.lc = self.__recursive_insert(new_node, root.lc, root)
        
        # RECURSIVE CASE 2: Traverse RIGHT
        else:
            root.rc = self.__recursive_insert(new_node, root.rc, root)
        return root

    def insert_node(self, new_key, mode = 'i'):
        """
        INSERTS a new BST node.

        :Parameters:
            - `new_key`: the KEY of the new BST node to be inserted
            - `mode`(optional): a SINGLE character `str` that indicates if  
              the SLL search is conducted iteratively 'i' (default), or 
              recursively 'r'

        :Return:
            A POINTER to the newly inserted BST node
        """
        
        # STEP 1: Initialise the NEW node to be inserted into the BST
        new_node = BSTNode(new_key)

        # CASE A: `mode` is an inappropriate TYPE
        if (not isinstance(mode, str)):
            raise TypeError("`mode` must of TYPE `str`")

        # CASE B: Use the ITERATIVE search method
        elif (mode == 'i'):
            return self.__iterative_insert(new_node)

        # CASE C: Use the RECURSIVE search method
        elif (mode == 'r'):
            self.root = self.__recursive_insert(new_node, self.root)
            return new_node

        # CASE D: Mode is an INAPPROPRIATE value
        else:
            raise ValueError("`mode` must be of VALUE 'i' or 'r'")

    def min_node(self, root):
        """
        RETRIEVES the BST node with the SMALLEST key value.

        :Paramters:
            - `root`: is the ROOT node of the entire BST or subtree

        :Return:
            A POINTER to the BST node with the SMALLEST key value
        """

        # STEP 1: Ensure the `root` is a valid BST node
        if (not isinstance(root, BSTNode)):
            raise TypeError("`root` must be of TYPE `BSTNode`")
        
        # STEP 2: Keep traversing the LEFT-most child provided one exists
        curr_node = root
        while (curr_node.lc != None):
            curr_node = curr_node.lc
        return curr_node

    def max_node(self, root):
        """
        RETRIEVES the BST node with the LARGEST key value.

        :Paramters:
            - `root`: is the ROOT node of the entire BST or subtree

        :Return:
            A POINTER to the BST node with the LARGEST key value
        """
        
        # STEP 1: Ensure the `root` is a valid BST node
        if (not isinstance(root, BSTNode)):
            raise TypeError("`root` must be of TYPE `BSTNode`")

        # STEP 2: Keep traversing the RIGHT-most child provided one exists
        curr_node = root
        while(curr_node.rc != None):
            curr_node = curr_node.rc
        return curr_node

    def predecessor_node(self, node):
        """
        FINDS the BST node whose key comes BEFORE the current `node`.

        :Parameters:
            - `node`: the BST node to find the PREDECESSOR of

        :Return:
            - A POINTER to the PREDECESSOR BST node of parameter `node`, OR
            - `None`: if NO predecessor exists
        """
        
        # STEP 1: Ensure `node` is of TYPE `BSTNode`
        if ((not isinstance(node, BSTNode)) or (node is None)):
            raise TypeError("`node` must be of TYPE `BSTNode`")

        # CASE A: Predecessor is one of the CHILD nodes of `node`
        if (node.lc != None):
            return self.max_node(node.lc)

        # CASE B: Predecessor is one of the PARENT nodes of `node`
        predecessor = node.p
        while ((predecessor != None) and (node is predecessor.lc)):
            node = predecessor
            predecessor = predecessor.p
        return predecessor

    def successor_node(self, node):
        """
        FINDS the BST node whose key comes AFTER the current `node`.

        :Parameters:
            - `node`: the BST node to find the SUCCESSOR of

        :Return:
            - A POINTER to the SUCCESSOR BST node of parameter `node`, OR
            - `None`: if NO successor exists
        """

        # STEP 1: Ensure `node` is of TYPE `BSTNode`
        if ((not isinstance(node, BSTNode)) or (node is None)):
            raise TypeError("`node` must be of TYPE `BSTNode`")
        
        # CASE A: Successor is one of the CHILD nodes of `node`
        if (node.rc != None):
            return self.min_node(node.rc)

        # CASE B: Successor is one of the PARENT nodes of `node`
        successor = node.p
        while ((successor != None) and (node is successor.rc)):
            node = successor
            successor = successor.p
        return successor

    def __transplant_node(self, node1, node2):
        """
        MOVES a subtree rooted at `node1` & REPLACES it with a (LEFT or RIGHT) 
        child subtree `node2`.

        :Parameters:
            - `node1`: the node to be REPLACED & is shifted as a new LEFT 
              or RIGHT child
            - `node2`: the BST node to REPLACE the position of `node1`
        """
        
        # CASE A: Transplanting from the ROOT node
        if (node1.p is None):
            self.root = node2
        
        # CASE B: Transplanting from the LEFT subtree
        elif (node1 is node1.p.lc):
            node1.p.lc = node2

        # CASE C: Transplanting from the RIGHT subtree
        else:
            node1.p.rc = node2
        
        # STEP 2: If `node2` replaced `node1` both have the SAME parent
        if (node2 != None):
            node2.p = node1.p

    def delete_node(self, node):
        """
        DELETES a given BST `node`.

        :Parameters:
            - `node`: the BST node to be deleted
        """

        # STEP 1: Ensure `node` is of type `BSTNode`
        if (not isinstance(node, BSTNode)):
            raise TypeError("`node` must be of TYPE `BSTNode`")
        
        # CASE A: `node` has ZERO child nodes (i.e. LEAF node)
        elif (node.lc is None):
            self.__transplant_node(node, node.rc)

        # CASE B: `node` has ONE child node
        elif (node.rc is None):
            self.__transplant_node(node, node.lc)

        # CASE C: `node` has TWO child nodes
        else:

            # STEP CI: Get the node to REPLACE the position of `node`
            min_node = self.min_node(node.rc)

            # STEP CII: Swap the position of `min_node` & it's parent node
            if (min_node.p != node):
                self.__transplant_node(min_node, min_node.rc)
                min_node.rc = node.rc
                min_node.rc.p = min_node
            
            # STEP CIII: Replace `node` with `min_node`
            self.__transplant_node(node, min_node)
            min_node.lc = node.lc
            min_node.lc.p = min_node

    def inorder_walk(self, root, operation = print):
        """
        Performs an ALL-tree TRAVERSAL in the following order:
        1. LEFT subtree
        2. ROOT node
        3. RIGHT subtree

        :Parameters:
            - `root`: the ROOT node of the BST
            - `operation`: a function (default `print`) that specifies the 
              ACTION to be performed on the KEY of every visited BST node
        """

        # Ensure the root exists to continue traversals
        if root:
            self.inorder_walk(root.lc)
            operation(root.key)
            self.inorder_walk(root.rc)

    def preorder_walk(self, root, operation = print):
        """
        Performs an ALL-tree TRAVERSAL in the following order:
        1. ROOT node
        2. LEFT subtree
        3. RIGHT subtree

        :Parameters:
            - `root`: the ROOT node of the BST
            - `operation`: a function (default `print`) that specifies the 
              ACTION to be performed on the KEY of every visited BST node
        """

        # Ensure the root exists to continue traversals
        if root:
            operation(root.key)
            self.preorder_walk(root.lc)
            self.preorder_walk(root.rc)

    def postorder_walk(self, root, operation = print):
        """
        Performs an ALL-tree TRAVERSAL in the following order:
        1. LEFT subtree
        2. RIGHT subtree
        3. ROOT node

        :Parameters:
            - `root`: the ROOT node of the BST
            - `operation`: a function (default `print`) that specifies the 
              ACTION to be performed on the KEY of every visited BST node
        """

        # Ensure the root exists to continue traversals
        if root:
            self.postorder_walk(root.lc)
            self.postorder_walk(root.rc)
            operation(root.key)

    def __iterative_search(self, target_key):
        """
        ITERATIVELY searches the BST for a node with `target_key`.

        :Parameters:
            - `target_key`: the INFORMATION to search for in the BST

        :Return:
            - A POINTER to the BST node that MATCHES the `target_key`, OR
            - `None`: if NO match was found
        """

        # STEP 1: Initialise the ROOT node
        root = self.root
        while (root != None):

            # CASE 1A: Traverse towards the LEFT child node
            if (self.cmp_fn(target_key, root.key) == self.cmp_less):
                root = root.lc

            # CASE 1B: Traverse towards the RIGHT child node
            elif (self.cmp_fn(target_key, root.key) == self.cmp_greater):
                root = root.rc

            # CASE 1C: Found a node with the SAME `target_key`
            else:
                return root

        # STEP 2: `target_key` does not exist in the BST
        return None

    def __recursive_search(self, root, target_key):
        """
        RECURSIVELY searches the BST for a node with `target_key`.

        :Parameters:
            - `root`: the 1st node the BST
            - `target_key`: the INFORMATION to search for in the BST

        :Return:
            - A POINTER to the BST node that MATCHES the `target_key`, OR
            - `None`: if NO match was found
        """

        # BASE CASE 1: `target_key` is NOT in the BST
        if (root is None):
            return None
        
        # BASE CASE 2: `target_key` has been FOUND
        elif (self.cmp_fn(root.key, target_key) == self.cmp_equal):
            return root
        
        # RECURSIVE CASE 1: Traverse to RIGHT child
        elif (self.cmp_fn(root.key, root.key) == self.cmp_greater):
            return self.__recursive_search(root.rc, target_key)
        
        # RECURSIVE CASE 2: Traverse to LEFT child
        else:
            return self.__recursive_search(root.lc, target_key)

    def search(self, target_key, mode = 'i'):
        """
        SEARCHES the BST for a node with `target_key`.

        :Parameters:
            - `target_key`: the INFORMATION to search for in the BST
            - `mode`(optional): a SINGLE character `str` that indicates if  
              the BST search is conducted iteratively 'i' (default), or 
              recursively 'r'

        :Return:
            - A POINTER to the BST node that MATCHES the `target_key`, OR
            - `None`: if NO match was found
        """

        # CASE A: Mode is an INAPPROPRIATE type
        if (not isinstance(mode, str)):
            raise TypeError("`mode` must of TYPE `str`")
        
        # CASE B:
        elif (mode == 'i'):
            return self.__iterative_search(target_key)

        # CASE C: 
        elif (mode == 'r'):
            return self.__recursive_search(self.root, target_key)

        # CASE D: Mode is an INAPPROPRIATE value
        else:
            raise ValueError("`mode` must be of VALUE 'i' or 'r'")