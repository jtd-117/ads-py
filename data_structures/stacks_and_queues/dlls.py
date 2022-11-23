# @file     dlls.py
# @brief    A file for implementing a doubly linked-list stack (DLLS)
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

class DLLS(object):
    """
    An INTERFACE for a doubly linked-list stack (DLLS)
    """
    
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self):
        """
        The FIRST node in the DLLS.
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
        The LAST node in the DLLS.
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
        CHECKS if the DLLS is empty.

        :Return: 
            - `True` if the DLLS is empty
            - `False` if the DLLS is NOT empty
        """
        return ((self.head == None) and (self.tail == None))

    def push(self, newKey):
        """
        INSERTS a new TAIL (i.e. END) node in the DLLS.

        :Parameters:
            - `newKey`: is the INFORMATION to be associated with the new 
              TAIL DLLS node

        :Return:
            A POINTER to the NEWLY added DLLS TAIL node
        """
        
        # STEP 1: Adjust the DLLS head pointer
        newTail = DLLNode(newKey)
        newTail.next = None
        newTail.prev = self.tail

        # CASE A: This is the 1st DLLS node insertion
        if (self.tail == None):
            self.head = self.tail = newTail

        # CASE B: NOT the 1st DLLS node insertion
        else:
            self.tail.next = newTail
            self.tail = newTail
        
        # STEP 2: Return the NEWLY added DLLS TAIL node
        return self.tail

    def pop(self):
        """
        DELETES the TAIL (i.e. END) node of the DLLS.

        :Return:
            - A POINTER to the new DLLS TAIL node, OR
            - `None` if the DLLS has NO nodes to delete
        """

        # STEP 1: Check if the DLLS is empty
        if (self.isEmpty()):
            return
        
        # STEP 2: Initialise POINTER variables
        oldTail = self.tail
        self.tail = self.tail.prev

        # CASE A: The only DLLS node deleted
        if (self.tail == None):
            self.head = None

        # CASE B: At LEAST 2 DLLS node remaining
        else:
            self.tail.next = None

        # STEP 3: Return the new DLLS TAIL node
        return self.tail

    def __iterativeSearch(self, targetKey):
        """
        ITERATIVELY searches the DLLS & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `targetKey`: is the DESIRED search data to be queried in the DLLS

        :Return:
            - A POINTER to the DLLS node that MATCHES the target search data, OR 
            - `None` to indicate that NO matches were found
        """
        
        # STEP 1: Linear search the DLLS up to the TAIL node
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
        RECURSIVELY searches the DLLS & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `targetKey`: is the DESIRED search data to be queried in the DLLS
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

        # RECURSIVE CASE: Still more DLLS nodes to search
        return self.__recursiveSearch(targetKey, selfHead.next)

    def search(self, targetKey, mode = 'i'):
        """
        SEARCHES the DLLS & returns the 1st instance of a DLLS node who's key 
        MATCHES the target search key.

        :Parameters:
            - `targetKey`: is the DESIRED search data to be queried in the DLLS
            - `mode` (optional): a SINGLE character `str` that indicates if  
              the DLLS search is conducted iteratively 'i' (default), or 
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