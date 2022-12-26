# @file     slls.py
# @brief    A file for implementing a singly linked-list (SLLS)
# @author   Jude Thaddeau Data
# @note     GitHub: https://github.com/jtd-117
# ---------------------------------------------------------------------------- #

from enum import Enum

# ---------------------------------------------------------------------------- #

class SLLS(object):
    """
    An INTERFACE for a singly linked-list stack (SLLS).
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

    class Node(object):
        """
        A Singly Linked-List (SLL) node.
        """

        def __init__(self, key):
            self._key = key
            self._next = None

        @property
        def key(self):
            """
            Contains the DATA associated with an SLL node.
            """
            return self._key

        @key.setter
        def key(self, new_key):
            self._key = new_key
        
        @key.deleter
        def key(self):
            del self._key
        
        @property
        def next(self):
            """
            A POINTER to an SLL successor node.
            """
            return self._next

        @next.setter
        def next(self, new_next):

            # STEP 1: Ensure the `new_next` is of TYPE `SLLS.Node` or `None`
            if (isinstance(new_next, SLLS.Node) or (new_next is None)):
                self._next = new_next
                return
            
            # STEP 2: `new_next` is an INAPPROPRIATE type
            raise TypeError("`new_next` must be of TYPE `SLLS.Node` or `None`")
        
        @next.deleter
        def next(self):
            del self._next

    def __init__(self, cmp_fn):

        # STEP 1: Ensure `cmp_fn` is a function
        if (not callable(cmp_fn)):
            raise TypeError("`cmp_fn` must be of TYPE 'function'")

        # STEP 2: Assign class attributes
        self._cmp_fn = cmp_fn
        self._head = None
        self._tail = None

    @property
    def cmp_fn(self):
        """
        A custom function for COMPARING `SLLS.Node` keys.

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
    def head(self):
        """
        The FIRST node in the SLLQ.
        """
        return self._head
    
    @head.setter
    def head(self, new_head):

        # STEP 1: Ensure the `new_head` is of TYPE `SLLS.Node` or `None`
        if (isinstance(new_head, SLLS.Node) or (new_head is None)):
            self._head = new_head
            return
        
        # STEP 2: `new_head` is an INAPPROPRIATE type
        raise TypeError("`new_head` must be of TYPE `SLLS.Node` or `None`")
    
    @head.deleter
    def head(self):
        del self._head

    @property
    def tail(self):
        """
        The LAST node in the SLLQ.
        """
        return self._tail
    
    @tail.setter
    def tail(self, new_tail):

        # STEP 1: Ensure the `new_tail` is of TYPE `SLLS.Node` or `None`
        if (isinstance(new_tail, SLLS.Node) or (new_tail is None)):
            self._tail = new_tail
            return
        
        # STEP 2: `new_tail` is an INAPPROPRIATE type
        raise TypeError("`new_tail` must be of TYPE `SLLS.Node` or `None`")
    
    @tail.deleter
    def tail(self):
        del self._tail

    def is_empty(self):
        """
        CHECKS if the SLLQ is empty.

        :Return: 
            - `True`: if the SLLQ is empty
            - `False`: if the SLLQ is NOT empty
        """
        return ((self.head == None) and (self.tail == None))

    def push(self, new_key):
        """
        INSERTS a new TAIL (i.e. END) node in the SLLS.

        :Parameters:
            - `new_key`: the INFORMATION to be associated with the new 
              TAIL SLLS node

        :Return: 
            A POINTER to the newly added SLLS TAIL node
        """
        
        # STEP 1: Initialise the new TAIL node & POINTER variables
        new_tail = SLLS.Node(new_key)

        # CASE A: 1st insertion into the SLLS
        if (self.tail == None):
            self.head = self.tail = new_tail

        # CASE B: NOT the 1st insertion into the SLLS
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        
        # STEP 2: Return the newly added TAIL node
        return self.tail
    
    def pop(self):
        """
        DELETES the TAIL (i.e. END) node of the SLLS.

        :Return:
            - A POINTER to the new SLLS TAIL node, OR
            - `None`: if the SLLS has NO nodes to delete
        """
        
        # STEP 1: Initialise the POINTER variables
        tmp = self.head

        # CASE A: ZERO nodes in the SLLS
        if (tmp == None):
            return

        # CASE B: Only ONE node is the SLLS remaining
        elif (tmp.next == None):
            self.head = self.tail = None

        # CASE C: At least TWO nodes in the SLLS
        else:

            # STEP BI: Iterate the 2nd last node
            while (tmp.next.next):
                tmp = tmp.next

            # STEP BII: Adjust the pointers of the NEW tail
            tmp.next = None
            self.tail = tmp

        # STEP 2: Return the new SLLS TAIL node
        return self.tail

    def __iterative_search(self, target_key):
        """
        ITERATIVELY searches the SLLS & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the SLLS

        :Return: 
            - A POINTER to the node that MATCHES the target search data, OR
            - `None`: to indicate that NO matches were found
        """

        # STEP 1: ZERO nodes remain
        if (not self.head):
            return None

        # STEP 2: Linear search the SLLS up to TAIL node
        curr = self.head
        while (curr):

            # STEP 3: Check if the current node's key MATCHES the target key
            if (self.cmp_fn(curr.key, target_key) == SLLS.CMPValues.EQUAL.value):
                return curr

            # STEP 4: Move to the next node
            curr = curr.next

        # STEP 5: Indicate that NO matches were detected
        return curr

    def __recursive_search(self, target_key, self_head):
        """
        RECURSIVELY searches the SLLS & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the SLLS
            - `self_head`: is the CURRENT instance's head node (i.e. self.head)

        :Return: 
            - A POINTER to the node that MATCHES the target search data, OR
            - `None`: to indicate that NO matches were found
        """
        
        # BASE CASE 1: Went beyond the TAIL node OR ZERO nodes remain
        if (not self_head):
            return None
        
        # BASE CASE 2: Found a match
        if (self.cmp_fn(self_head.key, target_key) == SLLS.CMPValues.EQUAL.value):
            return self_head

        # RECURSIVE CASE: Still more SLL nodes to search
        return self.__recursive_search(target_key, self_head.next)

    def search(self, target_key, mode = 'i'):
        """
        SEARCHES the SLLS & returns the 1st instance of a SLLS node who's key 
        MATCHES the target search key.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the SLLS
            - `mode` (optional): a SINGLE character `str` that indicates if  
              the SLLS search is conducted iteratively 'i' (default), or 
              recursively 'r'

        :Return: 
            - A POINTER to the node that MATCHES the target search data, OR
            - `None`: to indicate that NO matches were found
        """

        # CASE A: Mode is an INAPPROPRIATE type
        if (not isinstance(mode, str)):
            raise TypeError("`mode` must of TYPE `str`")

        # CASE B: Use the ITERATIVE search method
        elif (mode == 'i'):
            return self.__iterative_search(target_key)

        # CASE C: Use the RECURSIVE search method
        elif (mode == 'r'):
            return self.__recursive_search(target_key, self.head)

        # CASE D: Mode is an INAPPROPRIATE value
        else:
            raise ValueError("`mode` must be of VALUE 'i' or 'r'")