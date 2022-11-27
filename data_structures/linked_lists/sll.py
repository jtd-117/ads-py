# @file     sll.py
# @brief    A file for implementing a singly linked-list (SLL)
# @author   Jude Thaddeau Data
# @note     GitHub: https://github.com/jtd-117
# ---------------------------------------------------------------------------- #

class SLLNode(object):
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

        # STEP 1: Ensure the `new_next` is of TYPE `SLLNode` or `None`
        if (isinstance(new_next, SLLNode) or (new_next is None)):
            self._next = new_next
            return
        
        # STEP 2: `new_next` is an INAPPROPRIATE type
        raise TypeError("`new_next` must be of TYPE `SLLNode` or `None`")
    
    @next.deleter
    def next(self):
        del self._next

# ---------------------------------------------------------------------------- #

class SLL(object):
    """
    An INTERFACE for a singly linked-list (SLL).
    """

    def __init__(self):
        self._head = None
        self._tail = None
    
    @property
    def head(self):
        """
        The FIRST node in the SLL.
        """
        return self._head
    
    @head.setter
    def head(self, new_head):

        # STEP 1: Ensure the `new_head` is of TYPE `SLLNode` or `None`
        if (isinstance(new_head, SLLNode) or (new_head is None)):
            self._head = new_head
            return
        
        # STEP 2: `new_head` is an INAPPROPRIATE type
        raise TypeError("`new_head` must be of TYPE `SLLNode` or `None`")
    
    @head.deleter
    def head(self):
        del self._head

    @property
    def tail(self):
        """
        The LAST node in the SLL.
        """
        return self._tail
    
    @tail.setter
    def tail(self, new_tail):

        # STEP 1: Ensure the `new_tail` is of TYPE `SLLNode` or `None`
        if (isinstance(new_tail, SLLNode) or (new_tail is None)):
            self._tail = new_tail
            return
        
        # STEP 2: `new_tail` is an INAPPROPRIATE type
        raise TypeError("`new_tail` must be of TYPE `SLLNode` or `None`")
    
    @tail.deleter
    def tail(self):
        del self._tail

    def is_empty(self):
        """
        CHECKS if the SLL is empty.

        :Return: 
            - `True`: if the SLL is empty
            - `False`: if the SLL is NOT empty
        """
        return ((self.head == None) and (self.tail == None))

    def insert_head(self, new_key):
        """
        INSERTS a new HEAD (i.e. FIRST) node in the SLL.

        :Parameters:
            - `new_key`: the INFORMATION to be associated with the new HEAD 
              SLL node

        :Return:
            A POINTER to the newly added SLL HEAD node
        """

        # STEP 1: Initialise the new HEAD node & POINTER variables
        new_head = SLLNode(new_key)
        new_head.next = self.head
        self.head = new_head

        # EXCEPTION: 1st insertion into the SLL
        if (self.is_empty()):
            self.tail = new_head

        # STEP 2: Return the newly added HEAD node
        return self.head

    def insert_tail(self, new_key):
        """
        INSERTS a new TAIL (i.e. END) node in the SLL.

        :Parameters:
            - `new_key`: the INFORMATION to be associated with the new 
              TAIL SLL node

        :Return: 
            A POINTER to the newly added SLL TAIL node
        """
        
        # STEP 1: Initialise the new TAIL node & POINTER variables
        new_tail = SLLNode(new_key)

        # CASE A: 1st insertion into the SLL
        if (self.tail == None):
            self.head = self.tail = new_tail

        # CASE B: NOT the 1st insertion into the SLL
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        
        # STEP 2: Return the newly added TAIL node
        return self.tail

    def delete_head(self):
        """
        DELETES the HEAD (i.e. FIRST) node of the SLL.

        :Return:
            - A POINTER to the new SLL HEAD node, OR
            - `None`: if the SLL has NO nodes to delete
        """
        
        # STEP 1: Check if the SLL is empty
        if (self.is_empty()):
            return None

        # CASE A: Only ONE node in the SLL remains
        if (self.head == self.tail):
            self.head = self.tail = None

        # CASE B: At LEAST TWO nodes in the SLL
        else:
            self.head = self.head.next

        # STEP 2: Read the new SLL HEAD node
        return self.head
        
    def delete_tail(self):
        """
        DELETES the TAIL (i.e. END) node of the SLL.

        :Return:
            - A POINTER to the new SLL TAIL node, OR
            - `None`: if the SLL has NO nodes to delete
        """
        
        # STEP 1: Initialise the POINTER variables
        tmp = self.head

        # CASE A: ZERO nodes in the SLL
        if (tmp == None):
            return

        # CASE B: Only ONE node is the SLL remaining
        elif (tmp.next == None):
            self.head = self.tail = None

        # CASE C: At least TWO nodes in the SLL
        else:

            # STEP BI: Iterate the 2nd last node
            while (tmp.next.next):
                tmp = tmp.next

            # STEP BII: Adjust the pointers of the NEW tail
            tmp.next = None
            self.tail = tmp

        # STEP 2: Return the new SLL TAIL node
        return self.tail

    def __iterative_search(self, target_key):
        """
        ITERATIVELY searches the SLL & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the SLL

        :Return: 
            - A POINTER to the node that MATCHES the target search data, OR
            - `None`: to indicate that NO matches were found
        """

        # STEP 1: ZERO nodes remain
        if (not self.head):
            return None

        # STEP 2: Linear search the SLL up to TAIL node
        curr = self.head
        while (curr):

            # STEP 3: Check if the current node's key MATCHES the target key
            if (curr.key == target_key):
                return curr

            # STEP 4: Move to the next node
            curr = curr.next

        # STEP 5: Indicate that NO matches were detected
        return None

    def __recursive_search(self, target_key, self_head):
        """
        RECURSIVELY searches the SLL & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the SLL
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

        # RECURSIVE CASE: Still more SLL nodes to search
        return self.__recursive_search(target_key, self_head.next)

    def search(self, target_key, mode = 'i'):
        """
        SEARCHES the SLL & returns the 1st instance of a SLL node who's key 
        MATCHES the target search key.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the SLL
            - `mode` (optional): a SINGLE character `str` that indicates if  
              the SLL search is conducted iteratively 'i' (default), or 
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
        ITERATIVELY reverses the node ORDER in a SLL.
        """
        
        # STEP 1: Initialise the POINTER variables
        curr = self.head
        self.tail = curr
        prev = None

        # STEP 2: Iterate all the way until the TAIL (i.e. LAST) SLL node
        while (curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # STEP 3: Make the head point to the ORIGINAL tail
        self.head = prev

    def __recursive_reverse(self, self_head):
        """
        RECURSIVELY reverses the node ORDER in a SLL.

        :Parameters:
            - `self_head`: is the CURRENT instance's head node (i.e. self.head)

        :Return:
            A POINTER to starting from the ORIGINAL TAIL node
        """

        # STEP 1: Check if the SLL is empty
        if (self_head == None):
            return None

        # BASE CASE: Reached the TAIL node of the DLL
        if (self_head.next == None):
            self.tail = self.head
            self.head = self_head
            return self_head

        # RECURSIVE CASE: Keep traversing SLL to TAIL node
        rest = self.__recursive_reverse(self_head.next)

        # STEP 2: Traverse the SLL BACKWARDS & adjust POINTER values
        self_head.next.next = self_head
        self_head.next = None
        return rest

    def reverse(self, mode = 'i'):
        """
        REVERSES the node order of the SLL.

        :Parameters:
            - `mode` (optional): a SINGLE character `str` that indicates if 
              the SLL node reversal is conducted iteratively 'i' (default),  
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