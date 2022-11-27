# @file     dll.py
# @brief    A file for implementing a doubly linked-list (DLL)
# @author   Jude Thaddeau Data
# @note     GitHub: https://github.com/jtd-117
# ---------------------------------------------------------------------------- #

class DLLNode(object):
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

        # STEP 1: Ensure the `new_next` is of type `DLLNode` or `None`
        if (isinstance(new_next, DLLNode) or (new_next is None)):
            self._next = new_next
            return
        
        # STEP 2: `new_next` is an INAPPROPRIATE type
        raise TypeError("`new_next` must be of TYPE `DLLNode` or `None`")
    
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

        # STEP 1: Ensure the `new_prev` is type `DLLNode` or `None`
        if (isinstance(new_prev, DLLNode) or (new_prev is None)):
            self._prev = new_prev
            return
        
        # STEP 2: `new_prev` is an INAPPROPRIATE type
        raise TypeError("`new_prev` must be of TYPE `DLLNode` or `None`")
    
    @prev.deleter
    def prev(self):
        del self._prev

# ---------------------------------------------------------------------------- #

class DLL(object):
    """
    An INTERFACE for a doubly linked-list (DLL).
    """

    def __init__(self):
        self._head = None
        self._tail = None
    
    @property
    def head(self):
        """
        The FIRST node in the DLL.
        """
        return self._head
    
    @head.setter
    def head(self, new_head):

        # STEP 1: Ensure the `new_head` is of TYPE `DLLNode` or `None`
        if (isinstance(new_head, DLLNode) or (new_head is None)):
            self._head = new_head
            return
        
        # STEP 2: `new_head` is an INAPPROPRIATE type
        raise TypeError("`new_head` must be of TYPE `DLLNode` or `None`")
    
    @head.deleter
    def head(self):
        del self._head

    @property
    def tail(self):
        """
        The LAST node in the DLL.
        """
        return self._tail
    
    @tail.setter
    def tail(self, new_tail):

        # STEP 1: Ensure the `new_tail` is of TYPE `DLLNode` or `None`
        if (isinstance(new_tail, DLLNode) or (new_tail is None)):
            self._tail = new_tail
            return
        
        # STEP 2: `new_tail` is an inappropriate type
        raise TypeError("`new_tail` must be of TYPE `DLLNode` or `None`")
    
    @tail.deleter
    def tail(self):
        del self._tail

    def is_empty(self):
        """
        CHECKS if the DLL is empty.

        :Return: 
            - `True`: if the DLL is empty
            - `False`: if the DLL is NOT empty
        """
        return ((self.head == None) and (self.tail == None))

    def insert_head(self, new_key):
        """
        INSERTS a new HEAD (i.e. FIRST) node in the DLL.

        :Parameters:
            - `new_key`: the INFORMATION to be associated with the new HEAD 
              DLL node

        :Return:
            A POINTER to the newly added DLL HEAD node
        """
        
        # STEP 1: Initialise the POINTER variables
        new_head = DLLNode(new_key)
        new_head.next = self.head
        new_head.prev = None

        # CASE A: This is the 1st DLL node insertion
        if (self.is_empty()):
            self.tail = new_head
        
        # CASE B: NOT the 1st DLL node insertion
        else:
            self.head.prev = new_head
        
        # STEP 2: Adjust the DLL head pointer
        self.head = new_head
        return self.head

    def insert_tail(self, new_key):
        """
        INSERTS a new TAIL (i.e. END) node in the DLL.

        :Parameters:
            - `new_key`: is the INFORMATION to be associated with the new 
              TAIL DLL node

        :Return:
            A POINTER to the NEWLY added DLL TAIL node
        """
        
        # STEP 1: Adjust the DLL head pointer
        new_tail = DLLNode(new_key)
        new_tail.next = None
        new_tail.prev = self.tail

        # CASE A: This is the 1st DLL node insertion
        if (self.tail == None):
            self.head = self.tail = new_tail

        # CASE B: NOT the 1st DLL node insertion
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        
        # STEP 2: Return the NEWLY added DLL TAIL node
        return self.tail

    def delete_head(self):
        """
        DELETES the HEAD (i.e. FIRST) node of the DLL.

        :Return:
            - A POINTER to the new DLL HEAD node, OR 
            - `None`: if the DLL has NO nodes to delete
        """

        # STEP 1: Check if the DLL is empty
        if (self.is_empty()):
            return None
        
        # STEP 2: Initalise the POINTER variables
        old_head = self.head
        self.head = old_head.next

        # CASE A: The only DLL node got deleted
        if (self.head == None):
            self.tail = None

        # CASE B: At LEAST 2 DLL node remaining
        else:
            self.head.prev = None

        # STEP 3: Return the new DLL HEAD node
        return self.head

    def delete_tail(self):
        """
        DELETES the TAIL (i.e. END) node of the DLL.

        :Return:
            - A POINTER to the new DLL TAIL node, OR
            - `None`: if the DLL has NO nodes to delete
        """

        # STEP 1: Check if the DLL is empty
        if (self.is_empty()):
            return
        
        # STEP 2: Initialise POINTER variables
        old_tail = self.tail
        self.tail = old_tail.prev

        # CASE A: The only DLL node deleted
        if (self.tail == None):
            self.head = None

        # CASE B: At LEAST 2 DLL node remaining
        else:
            self.tail.next = None

        # STEP 3: Return the new DLL TAIL node
        return self.tail

    def __iterative_search(self, target_key):
        """
        ITERATIVELY searches the DLL & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the DLL

        :Return:
            - A POINTER to the DLL node that MATCHES the target search data, OR 
            - `None`: to indicate that NO matches were found
        """
        
        # STEP 1: Linear search the DLL up to the TAIL node
        curr = self.head
        while (curr):

            # STEP 2: Check if a MATCH was detected
            if (curr.key == target_key):
                return curr

            # STEP 3: NO match detected, move to the next node
            curr = curr.next

        # STEP 4: Indicate that NO matches were detected
        return None

    def __recursive_search(self, target_key, self_head):
        """
        RECURSIVELY searches the DLL & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the DLL
            - `self_head`: is the CURRENT instance's head node (i.e. self.head)

        :Return: 
            - A POINTER to the node that MATCHES the target search data, OR
            - `None`: to indicate that NO matches were found
        """

        # BASE CASE 1: Went beyond the TAIL node OR ZERO nodes remain
        if (not self_head):
            return None
        
        # BASE CASE 2: Found a match
        if (self_head.key == target_key):
            return self_head

        # RECURSIVE CASE: Still more DLL nodes to search
        return self.__recursive_search(target_key, self_head.next)

    def search(self, target_key, mode = 'i'):
        """
        SEARCHES the DLL & returns the 1st instance of a DLL node who's key 
        MATCHES the target search key.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the DLL
            - `mode` (optional): a SINGLE character `str` that indicates if  
              the DLL search is conducted iteratively 'i' (default), or 
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
            result = self.__iterative_search(target_key)

        # CASE C: Use the RECURSIVE search method
        elif (mode == 'r'):
            result = self.__recursive_search(target_key, self.head)

        # CASE D: Mode is an INAPPROPRIATE value
        else:
            raise ValueError("`mode` must be of VALUE 'i' or 'r'")

        return result

    def __iterative_reverse(self):
        """
        ITERATIVELY reverses the node ORDER in a DLL.
        """

        # STEP 1: Initialise the POINTER variables
        curr = self.head
        self.head = self.tail
        self.tail = curr

        # STEP 2: Iterate all the way until the TAIL (i.e. LAST) DLL node
        while (curr != None):
            next = curr.next
            curr.next = curr.prev
            curr.prev = next
            curr = next

    def __recursive_reverse(self, self_head):
        """
        RECURSIVELY reverses the node ORDER in a DLL.

        Parameter(s):
            - `self_head`: is the CURRENT instance's head node (i.e. self.head)

        Return:
            A POINTER to STARTING from the ORIGINAL TAIL node
        """
        
        # EXCEPTION: DLL is EMPTY or has FINSIHED reversing DLL
        if (self_head == None):
            return None

        # BASE CASE: Reached the TAIL node of the DLL
        if (self_head.next == None):
            self.tail = self.head
            self.head = self_head

        # RECURSIVE CASE: from the the TAIL node adjust pointers BACKWARDS
        next_node = self_head.next
        self_head.next = self_head.prev
        self_head.prev = next_node
        self.__recursive_reverse(self_head.prev)
    
    def reverse(self, mode = 'i'):
        """
        REVERSES the node order of the DLL.

        :Parameters:
            - `mode` (optional): a SINGLE character `str` that indicates if 
              the DLL node reversal is conducted iteratively 'i' (default),  
              or recursively 'r'
        """

        # CASE A: Mode is an INAPPROPRIATE type
        if (not isinstance(mode, str)):
            raise TypeError("`mode` must of TYPE `str`")

        # CASE B: Use the ITERATIVE search method
        elif (mode == 'i'):
            self.__iterative_reverse()

        # CASE C: Use the RECURSIVE search method
        elif (mode == 'r'):
            self.__recursive_reverse(self.head)

        # CASE D: Mode is an INAPPROPRIATE value
        else:
            raise ValueError("`mode` must be of VALUE 'i' or 'r'")