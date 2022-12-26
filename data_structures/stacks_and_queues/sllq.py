# @file     sllq.py
# @brief    A file for implementing a singly linked-list queue (SLLQ)
# @author   Jude Thaddeau Data
# @note     GitHub: https://github.com/jtd-117
# ---------------------------------------------------------------------------- #

from enum import Enum

# ---------------------------------------------------------------------------- #

class SLLQ(object):
    """
    An INTERFACE for a singly linked-list queue (SLLQ).
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

            # STEP 1: Ensure the `new_next` is of TYPE `SLLQ.Node` or `None`
            if (isinstance(new_next, SLLQ.Node) or (new_next is None)):
                self._next = new_next
                return
            
            # STEP 2: `new_next` is an INAPPROPRIATE type
            raise TypeError("`new_next` must be of TYPE `SLLQ.Node` or `None`")
        
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
        A custom function for COMPARING `SLLQ.Node` keys.

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

        # STEP 1: Ensure the `new_head` is of TYPE `SLLQ.Node` or `None`
        if (isinstance(new_head, SLLQ.Node) or (new_head is None)):
            self._head = new_head
            return
        
        # STEP 2: `new_head` is an INAPPROPRIATE type
        raise TypeError("`new_head` must be of TYPE `SLLQ.Node` or `None`")
    
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

        # STEP 1: Ensure the `new_tail` is of TYPE `SLLQ.Node` or `None`
        if (isinstance(new_tail, SLLQ.Node) or (new_tail is None)):
            self._tail = new_tail
            return
        
        # STEP 2: `new_tail` is an INAPPROPRIATE type
        raise TypeError("`new_tail` must be of TYPE `SLLQ.Node` or `None`")
    
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

    def enqueue(self, new_key):
        """
        INSERTS a new TAIL (i.e. END) node in the SLLQ.

        :Parameters:
            - `new_key`: the INFORMATION to be associated with the new 
              TAIL SLLQ node

        :Return: 
            A POINTER to the newly added SLLQ TAIL node
        """
        
        # STEP 1: Initialise the new TAIL node & POINTER variables
        new_tail = SLLQ.Node(new_key)

        # CASE A: 1st insertion into the SLLQ
        if (self.tail == None):
            self.head = self.tail = new_tail

        # CASE B: NOT the 1st insertion into the SLLQ
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        
        # STEP 2: Return the newly added TAIL node
        return self.tail

    def dequeue(self):
        """
        DELETES the HEAD (i.e. FIRST) node of the SLLQ.

        :Return:
            - A POINTER to the new SLLQ HEAD node, OR
            - `None`: if the SLLQ has NO nodes to delete
        """
        
        # STEP 1: Check if the SLLQ is empty
        if (self.is_empty()):
            return None

        # CASE A: Only ONE node in the SLLQ remains
        if (self.head == self.tail):
            self.head = self.tail = None

        # CASE B: At LEAST TWO nodes in the SLLQ
        else:
            self.head = self.head.next

        # STEP 2: Read the new SLLQ HEAD node
        return self.head

    def __iterative_search(self, target_key):
        """
        ITERATIVELY searches the SLLQ & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the SLLQ

        :Return: 
            - A POINTER to the node that MATCHES the target search data, OR
            - `None`: to indicate that NO matches were found
        """

        # STEP 1: ZERO nodes remain
        if (not self.head):
            return None

        # STEP 2: Linear search the SLLQ up to TAIL node
        curr = self.head
        while (curr):

            # STEP 3: Check if the current node's key MATCHES the target key
            if (self.cmp_fn(curr.key, target_key) == SLLQ.CMPValues.EQUAL.value):
                return curr

            # STEP 4: Move to the next node
            curr = curr.next

        # STEP 5: Indicate that NO matches were detected
        return None

    def __recursive_search(self, target_key, self_head):
        """
        RECURSIVELY searches the SLLQ & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the SLLQ
            - `self_head`: is the CURRENT instance's head node (i.e. self.head)

        :Return: 
            - A POINTER to the node that MATCHES the target search data, OR
            - A `None` to indicate that NO matches were found
        """
        
        # BASE CASE 1: Went beyond the TAIL node OR ZERO nodes remain
        if (not self_head):
            return None
        
        # BASE CASE 2: Found a match
        if (self.cmp_fn(self_head.key, target_key) == SLLQ.CMPValues.EQUAL.value):
            return self_head

        # RECURSIVE CASE: Still more SLL nodes to search
        return self.__recursive_search(target_key, self_head.next)

    def search(self, target_key, mode = 'i'):
        """
        SEARCHES the SLLQ & returns the 1st instance of a SLLQ node who's key 
        MATCHES the target search key.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the SLLQ
            - `mode` (optional): a SINGLE character `str` that indicates if  
              the SLLQ search is conducted iteratively 'i' (default), or 
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