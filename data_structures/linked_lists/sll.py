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
    def key(self, newKey):
        self._key = newKey
    
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
    def next(self, newNext):

        # STEP 1: Ensure the `newNext` is of type `SLLNode` or None
        if (isinstance(newNext, SLLNode) or (newNext is None)):
            self._next = newNext
            return
        
        # STEP 2: `newNext` is an INAPPROPRIATE type
        raise TypeError("`next` must be of TYPE `SLLNode`")
    
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
    def head(self, newHead):

        # STEP 1: Ensure the `newHead` is a `SLLNode`
        if (isinstance(newHead, SLLNode) or (newHead is None)):
            self._head = newHead
            return
        
        # STEP 2: `newHead` is an INAPPROPRIATE type
        raise TypeError("`head` must be of TYPE `SLLNode`")
    
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
    def tail(self, newTail):

        # STEP 1: Ensure the `newTail` is a `SLLNode`
        if (isinstance(newTail, SLLNode) or (newTail is None)):
            self._tail = newTail
            return
        
        # STEP 2: `newTail` is an INAPPROPRIATE type
        raise TypeError("`tail` must be of TYPE `SLLNode`")
    
    @tail.deleter
    def tail(self):
        del self._tail

    def isEmpty(self):
        """
        CHECKS if the SLL is empty.

        :Return: 
            - `True` if the SLL is empty
            - `False` if the SLL is NOT empty
        """
        return ((self.head == None) and (self.tail == None))

    def insertHead(self, newKey):
        """
        INSERTS a new HEAD (i.e. FIRST) node in the SLL.

        :Parameters:
            - `newKey`: the INFORMATION to be associated with the new HEAD 
              SLL node

        :Return:
            A POINTER to the newly added SLL HEAD node
        """

        # STEP 1: Initialise the new HEAD node & POINTER variables
        newHead = SLLNode(newKey)
        newHead.next = self.head
        self.head = newHead

        # EXCEPTION: 1st insertion into the SLL
        if (self.isEmpty()):
            self.tail = newHead

        # STEP 2: Return the newly added HEAD node
        return self.head

    def insertTail(self, newKey):
        """
        INSERTS a new TAIL (i.e. END) node in the SLL.

        :Parameters:
            - `newKey`: the INFORMATION to be associated with the new 
              TAIL SLL node

        :Return: 
            A POINTER to the newly added SLL TAIL node
        """
        
        # STEP 1: Initialise the new TAIL node & POINTER variables
        newTail = SLLNode(newKey)

        # CASE A: 1st insertion into the SLL
        if (self.tail == None):
            self.head = self.tail = newTail

        # CASE B: NOT the 1st insertion into the SLL
        else:
            self.tail.next = newTail
            self.tail = newTail
        
        # STEP 2: Return the newly added TAIL node
        return self.tail

    def deleteHead(self):
        """
        DELETES the HEAD (i.e. FIRST) node of the SLL.

        :Return:
            - A POINTER to the new SLL HEAD node, OR
            - `None` if the SLL has NO nodes to delete
        """
        
        # STEP 1: Check if the SLL is empty
        if (self.isEmpty()):
            return None

        # CASE A: Only ONE node in the SLL remains
        if (self.head == self.tail):
            self.head = self.tail = None

        # CASE B: At LEAST TWO nodes in the SLL
        else:
            self.head = self.head.next

        # STEP 2: Read the new SLL HEAD node
        return self.head
        
    def deleteTail(self):
        """
        DELETES the TAIL (i.e. END) node of the SLL.

        :Return:
            - A POINTER to the new SLL TAIL node, OR
            - `None` if the SLL has NO nodes to delete
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

    def __iterativeSearch(self, targetKey):
        """
        ITERATIVELY searches the SLL & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `targetKey`: is the DESIRED search data to be queried in the SLL

        :Return: 
            - A POINTER to the node that MATCHES the target search data, OR
            - A `None` to indicate that NO matches were found
        """

        # STEP 1: ZERO nodes remain
        if (not self.head):
            return None

        # STEP 2: Linear search the SLL up to TAIL node
        curr = self.head
        while (curr):

            # STEP 3: Check if the current node's key MATCHES the target key
            if (curr.key == targetKey):
                return curr

            # STEP 4: Move to the next node
            curr = curr.next

        # STEP 5: Indicate that NO matches were detected
        return curr

    def __recursiveSearch(self, targetKey, selfHead):
        """
        RECURSIVELY searches the SLL & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `targetKey`: is the DESIRED search data to be queried in the SLL
            - `selfHead`: is the CURRENT instance's head node (i.e. self.head)

        :Return: 
            - A POINTER to the node that MATCHES the target search data, OR
            - A `None` to indicate that NO matches were found
        """
        
        # BASE CASE 1: Went beyond the TAIL node OR ZERO nodes remain
        if (not selfHead):
            return None
        
        # BASE CASE 2: Found a match
        if (selfHead.key == targetKey):
            return selfHead

        # RECURSIVE CASE: Still more SLL nodes to search
        return self.__recursiveSearch(targetKey, selfHead.next)

    def search(self, targetKey, mode = 'i'):
        """
        SEARCHES the SLL & returns the 1st instance of a SLL node who's key 
        MATCHES the target search key.

        :Parameters:
            - `targetKey`: is the DESIRED search data to be queried in the SLL
            - `mode` (optional): a SINGLE character `str` that indicates if  
              the SLL search is conducted iteratively 'i' (default), or 
              recursively 'r'

        :Return: 
            - A POINTER to the node that MATCHES the target search data, OR
            - A `None` to indicate that NO matches were found
        """

        # STEP 1: Initialise result as `None`
        result = None

        # CASE A: Mode is an INAPPROPRIATE type
        if (not isinstance(mode, str)):
            raise TypeError("`mode` must of TYPE `str`")

        # CASE B: Use the ITERATIVE search method
        elif (mode == 'i'):
            result = self.__iterativeSearch(targetKey)

        # CASE C: Use the RECURSIVE search method
        elif (mode == 'r'):
            result = self.__recursiveSearch(targetKey, self.head)

        # CASE D: Mode is an INAPPROPRIATE value
        else:
            raise ValueError("`mode` must be of VALUE 'i' or 'r'")

        # STEP 2: Return the result
        return result

    def __iterativeReverse(self):
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

    def __recursiveReverse(self, selfHead):
        """
        RECURSIVELY reverses the node ORDER in a SLL.

        :Parameters:
            - `selfHead`: is the CURRENT instance's head node (i.e. self.head)

        :Return:
            A POINTER to starting from the ORIGINAL TAIL node
        """

        # STEP 1: Check if the SLL is empty
        if (selfHead == None):
            return None

        # BASE CASE: Reached the TAIL node of the DLL
        if (selfHead.next == None):
            self.tail = self.head
            self.head = selfHead
            return selfHead

        # RECURSIVE CASE: Keep traversing SLL to TAIL node
        rest = self.__recursiveReverse(selfHead.next)

        # STEP 2: Traverse the SLL BACKWARDS & adjust POINTER values
        selfHead.next.next = selfHead
        selfHead.next = None
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
            self.__iterativeReverse()

        # CASE C: Use the RECURSIVE search method
        elif (mode == 'r'):
            self.__recursiveReverse(self.head)

        # CASE D: Mode is an INAPPROPRIATE value
        else:
            raise ValueError("`mode` must be of VALUE 'i' or 'r'")