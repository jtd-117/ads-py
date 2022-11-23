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
    def key(self, newKey):
        self._key = newKey
    
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
    def next(self, newNext):

        # STEP 1: Ensure the `newNext` is of type `DLLNode` or `None`
        if (isinstance(newNext, DLLNode) or (newNext is None)):
            self._next = newNext
            return
        
        # STEP 2: `newNext` is an INAPPROPRIATE type
        raise TypeError("`next` must be of TYPE `DLLNode` or `None`")
    
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
    def prev(self, newPrev):

        # STEP 1: Ensure the `newPrev` is type `DLLNode` or `None`
        if (isinstance(newPrev, DLLNode) or (newPrev is None)):
            self._prev = newPrev
            return
        
        # STEP 2: `newPrev` is an INAPPROPRIATE type
        raise TypeError("`prev` must be of TYPE `DLLNode` or `None`")
    
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
    def head(self, newHead):

        # STEP 1: Ensure the `newHead` is of TYPE `DLLNode` or `None`
        if (isinstance(newHead, DLLNode) or (newHead is None)):
            self._head = newHead
            return
        
        # STEP 2: `newHead` is an INAPPROPRIATE type
        raise TypeError("`head` must be of TYPE `DLLNode` or `None`")
    
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
    def tail(self, newTail):

        # STEP 1: Ensure the `newTail` is of TYPE `DLLNode` or `None`
        if (isinstance(newTail, DLLNode) or (newTail is None)):
            self._tail = newTail
            return
        
        # STEP 2: `newTail` is an inappropriate type
        raise TypeError("`tail` must be of TYPE `DLLNode` or `None`")
    
    @tail.deleter
    def tail(self):
        del self._tail

    def isEmpty(self):
        """
        CHECKS if the DLL is empty.

        :Return: 
            - `True` if the DLL is empty
            - `False` if the DLL is NOT empty
        """
        return ((self.head == None) and (self.tail == None))

    def insertHead(self, newKey):
        """
        INSERTS a new HEAD (i.e. FIRST) node in the DLL.

        :Parameters:
            - `newKey`: the INFORMATION to be associated with the new HEAD 
              DLL node

        :Return:
            A POINTER to the newly added DLL HEAD node
        """
        
        # STEP 1: Initialise the POINTER variables
        newHead = DLLNode(newKey)
        newHead.next = self.head
        newHead.prev = None

        # CASE A: This is the 1st DLL node insertion
        if (self.isEmpty()):
            self.tail = newHead
        
        # CASE B: NOT the 1st DLL node insertion
        else:
            self.head.prev = newHead
        
        # STEP 2: Adjust the DLL head pointer
        self.head = newHead
        return self.head

    def insertTail(self, newKey):
        """
        INSERTS a new TAIL (i.e. END) node in the DLL.

        :Parameters:
            - `newKey`: is the INFORMATION to be associated with the new 
              TAIL DLL node

        :Return:
            A POINTER to the NEWLY added DLL TAIL node
        """
        
        # STEP 1: Adjust the DLL head pointer
        newTail = DLLNode(newKey)
        newTail.next = None
        newTail.prev = self.tail

        # CASE A: This is the 1st DLL node insertion
        if (self.tail == None):
            self.head = self.tail = newTail

        # CASE B: NOT the 1st DLL node insertion
        else:
            self.tail.next = newTail
            self.tail = newTail
        
        # STEP 2: Return the NEWLY added DLL TAIL node
        return self.tail

    def deleteHead(self):
        """
        DELETES the HEAD (i.e. FIRST) node of the DLL.

        :Return:
            - A POINTER to the new DLL HEAD node, OR 
            - `None` if the DLL has NO nodes to delete
        """

        # STEP 1: Check if the DLL is empty
        if (self.isEmpty()):
            return None
        
        # STEP 2: Initalise the POINTER variables
        oldHead = self.head
        self.head = oldHead.next

        # CASE A: The only DLL node got deleted
        if (self.head == None):
            self.tail = None

        # CASE B: At LEAST 2 DLL node remaining
        else:
            self.head.prev = None

        # STEP 3: Return the new DLL HEAD node
        return self.head

    def deleteTail(self):
        """
        DELETES the TAIL (i.e. END) node of the DLL.

        :Return:
            - A POINTER to the new DLL TAIL node, OR
            - `None` if the DLL has NO nodes to delete
        """

        # STEP 1: Check if the DLL is empty
        if (self.isEmpty()):
            return
        
        # STEP 2: Initialise POINTER variables
        oldTail = self.tail
        self.tail = self.tail.prev

        # CASE A: The only DLL node deleted
        if (self.tail == None):
            self.head = None

        # CASE B: At LEAST 2 DLL node remaining
        else:
            self.tail.next = None

        # STEP 3: Return the new DLL TAIL node
        return self.tail

    def __iterativeSearch(self, targetKey):
        """
        ITERATIVELY searches the DLL & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `targetKey`: is the DESIRED search data to be queried in the DLL

        :Return:
            - A POINTER to the DLL node that MATCHES the target search data, OR 
            - `None` to indicate that NO matches were found
        """
        
        # STEP 1: Linear search the DLL up to the TAIL node
        curr = self.head
        while (curr):

            # STEP 2: Check if a MATCH was detected
            if (curr.key == targetKey):
                return curr

            # STEP 3: NO match detected, move to the next node
            curr = curr.next

        # STEP 4: Indicate that NO matches were detected
        return None

    def __recursiveSearch(self, targetKey, selfHead):
        """
        RECURSIVELY searches the DLL & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `targetKey`: is the DESIRED search data to be queried in the DLL
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

        # RECURSIVE CASE: Still more DLL nodes to search
        return self.__recursiveSearch(targetKey, selfHead.next)

    def search(self, targetKey, mode = 'i'):
        """
        SEARCHES the DLL & returns the 1st instance of a DLL node who's key 
        MATCHES the target search key.

        :Parameters:
            - `targetKey`: is the DESIRED search data to be queried in the DLL
            - `mode` (optional): a SINGLE character `str` that indicates if  
              the DLL search is conducted iteratively 'i' (default), or 
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

    def __recursiveReverse(self, selfHead):
        """
        RECURSIVELY reverses the node ORDER in a DLL.

        Parameter(s):
            - `selfHead`: is the CURRENT instance's head node (i.e. self.head)

        Return:
            A POINTER to STARTING from the ORIGINAL TAIL node
        """
        
        # EXCEPTION: DLL is EMPTY or has FINSIHED reversing DLL
        if (selfHead == None):
            return None

        # BASE CASE: Reached the TAIL node of the DLL
        if (selfHead.next == None):
            self.tail = self.head
            self.head = selfHead

        # RECURSIVE CASE: from the the TAIL node adjust pointers BACKWARDS
        nextNode = selfHead.next
        selfHead.next = selfHead.prev
        selfHead.prev = nextNode
        self.__recursiveReverse(selfHead.prev)
    
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
            self.__iterativeReverse()

        # CASE C: Use the RECURSIVE search method
        elif (mode == 'r'):
            self.__recursiveReverse(self.head)

        # CASE D: Mode is an INAPPROPRIATE value
        else:
            raise ValueError("`mode` must be of VALUE 'i' or 'r'")