# @file     dllq.py
# @brief    A file for implementing a doubly linked-list queue (DLLQ)
# @author   Jude Thaddeau Data
# @note     GitHub: https://github.com/jtd-117
# ---------------------------------------------------------------------------- #

from enum import Enum

# ---------------------------------------------------------------------------- #

class DLLQ(object):
    """
    An INTERFACE for a doubly linked-list queue (DLLQ).
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
        A Doubly Linked-List (DLL) node.
        """

        def __init__(self, key):
            self._key = key
            self._next = None
            self._prev = None

        @property
        def key(self):
            """
            Contains the DATA associated with an DLL node.
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
            A POINTER to a DLL successor node.
            """
            return self._next

        @next.setter
        def next(self, new_next):

            # STEP 1: Ensure the `new_next` is of type `DLLQ.Node` or `None`
            if (isinstance(new_next, DLLQ.Node) or (new_next is None)):
                self._next = new_next
                return
            
            # STEP 2: `new_next` is an INAPPROPRIATE type
            raise TypeError("`new_next` must be of TYPE `DLLQ.Node` or `None`")
        
        @next.deleter
        def next(self):
            del self._next
        
        @property
        def prev(self):
            """
            A POINTER to a DLL predecessor node.
            """
            return self._prev

        @prev.setter
        def prev(self, new_prev):

            # STEP 1: Ensure the `new_prev` is type `DLLQ.Node` or `None`
            if (isinstance(new_prev, DLLQ.Node) or (new_prev is None)):
                self._prev = new_prev
                return
            
            # STEP 2: `new_prev` is an INAPPROPRIATE type
            raise TypeError("`new_prev` must be of TYPE `DLLQ.Node` or `None`")
        
        @prev.deleter
        def prev(self):
            del self._prev

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
        A custom function for COMPARING `DLLQ.Node` keys.

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
        The FIRST node in the DLLQ.
        """
        return self._head
    
    @head.setter
    def head(self, new_head):

        # STEP 1: Ensure the `new_head` is of TYPE `DLLQ.Node` or `None`
        if (isinstance(new_head, DLLQ.Node) or (new_head is None)):
            self._head = new_head
            return
        
        # STEP 2: `new_head` is an INAPPROPRIATE type
        raise TypeError("`new_head` must be of TYPE `DLLQ.Node` or `None`")
    
    @head.deleter
    def head(self):
        del self._head

    @property
    def tail(self):
        """
        The LAST node in the DLLQ.
        """
        return self._tail
    
    @tail.setter
    def tail(self, new_tail):

        # STEP 1: Ensure the `new_tail` is of TYPE `DLLQ.Node` or `None`
        if (isinstance(new_tail, DLLQ.Node) or (new_tail is None)):
            self._tail = new_tail
            return
        
        # STEP 2: `new_tail` is an inappropriate type
        raise TypeError("`new_tail` must be of TYPE `DLLQ.Node` or `None`")
    
    @tail.deleter
    def tail(self):
        del self._tail

    def is_empty(self):
        """
        CHECKS if the DLLQ is empty.

        :Return: 
            - `True`: if the DLLQ is empty
            - `False`: if the DLLQ is NOT empty
        """
        return ((self.head == None) and (self.tail == None))
    
    def enqueue(self, new_key):
        """
        INSERTS a new TAIL (i.e. END) node in the DLLQ.

        :Parameters:
            - `new_key`: is the INFORMATION to be associated with the new 
              TAIL DLLQ node

        :Return:
            A POINTER to the NEWLY added DLLQ TAIL node
        """
        
        # STEP 1: Adjust the DLLQ head pointer
        new_tail = DLLQ.Node(new_key)
        new_tail.next = None
        new_tail.prev = self.tail

        # CASE A: This is the 1st DLLQ node insertion
        if (self.tail == None):
            self.head = self.tail = new_tail

        # CASE B: NOT the 1st DLLQ node insertion
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        
        # STEP 2: Return the NEWLY added DLLQ TAIL node
        return self.tail

    def dequeue(self):
        """
        DELETES the HEAD (i.e. FIRST) node of the DLLQ.

        :Return:
            - A POINTER to the new DLLQ HEAD node, OR 
            - `None`: if the DLLQ has NO nodes to delete
        """

        # STEP 1: Check if the DLLQ is empty
        if (self.is_empty()):
            return None
        
        # STEP 2: Initalise the POINTER variables
        old_head = self.head
        self.head = old_head.next

        # CASE A: The only DLLQ node got deleted
        if (self.head == None):
            self.tail = None

        # CASE B: At LEAST 2 DLLQ node remaining
        else:
            self.head.prev = None

        # STEP 3: Return the new DLLQ HEAD node
        return self.head

    def __iterative_search(self, target_key):
        """
        ITERATIVELY searches the DLLQ & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the DLLQ

        :Return:
            - A POINTER to the DLLQ node that MATCHES the target search data, OR 
            - `None`: to indicate that NO matches were found
        """
        
        # STEP 1: Linear search the DLLQ up to the TAIL node
        curr = self.head
        while (curr):

            # STEP 2: Check if a MATCH was detected
            if (self.cmp_fn(curr.key, target_key) == DLLQ.CMPValues.EQUAL.value):
                return curr

            # STEP 3: NO match detected, move to the next node
            curr = curr.next

        # STEP 4: Indicate that NO matches were detected
        return None

    def __recursive_search(self, target_key, self_head):
        """
        RECURSIVELY searches the DLLQ & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the DLLQ
            - `self_head`: is the CURRENT instance's head node (i.e. self.head)

        :Return: 
            - A POINTER to the node that MATCHES the target search data, OR
            - `None`: to indicate that NO matches were found
        """

        # BASE CASE 1: Went beyond the TAIL node OR ZERO nodes remain
        if (not self_head):
            return None
        
        # BASE CASE 2: Found a match
        if (self.cmp_fn(self_head.key, target_key) == DLLQ.CMPValues.EQUAL.value):
            return self_head

        # RECURSIVE CASE: Still more DLLQ nodes to search
        return self.__recursive_search(target_key, self_head.next)

    def search(self, target_key, mode = 'i'):
        """
        SEARCHES the DLLQ & returns the 1st instance of a DLLQ node who's key 
        MATCHES the target search key.

        :Parameters:
            - `targetKey`: is the DESIRED search data to be queried in the DLLQ
            - `mode` (optional): a SINGLE character `str` that indicates if  
              the DLLQ search is conducted iteratively 'i' (default), or 
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