# @file     array_queue.py
# @brief    A file for implementing an array-based queue
# @author   Jude Thaddeau Data
# @note     GitHub: https://github.com/jtd-117
# ---------------------------------------------------------------------------- #

class ArrQueue(object):
    """
    An INTERFACE for an array-based queue.
    """

    def __init__(self):
        self._arr = []

    def len(self):
        return len(self._arr)

    @property
    def arr(self):
        """
        The ARRAY implemented as a QUEUE.
        """
        return self._arr
    
    @arr.setter
    def arr(self, i, new_value):
        """
        REPLACES the value at index `i` with `new_value`.

        :Parameters:
            - `i`: the INDEX to access the queue
            - `new_value`: the item to replace value at index `i`
        """
        self._arr[i % self.len()] = new_value

    @arr.deleter
    def arr(self):
        """
        RESETS the array to ZERO elements.
        """
        self._arr = []

    def enqueue(self, new_value):
        """
        ADDS a `new_value` at the END of the queue.

        :Parameters:
            - `new_value`: the item to be added at the END of the queue

        :Return:
            The NEWLY added LAST item in the queue
        """

        # STEP 1: Add the value at the END of the queue
        self.arr.append(new_value)

        # STEP 2: Return the newly LAST item of the queue
        return self.arr[self.len() - 1]

    def dequeue(self):
        """
        REMOVES the item at the FRONT of the queue.

        :Return:
            - The NEW & LAST item in the queue, OR
            - `None`: if the queue is EMPTY
        """
        
        # STEP 1: Check of the queue is EMPTY
        if (self.len() == 0):
            return None

        # STEP 2: Delete the FIRST item
        self.arr.pop(0)

        # STEP 3A: Only return the LASY item if non-empty
        if (self.len() > 0):
            return self.arr[self.len() - 1]
        
        # STEP 3B: Indicate the queue is now empty after the pop
        return None

    def __iterative_search(self, target_value):
        """
        ITERATIVELY searches the queue for the 1st instance that matches 
        `target_value`.

        :Parameters:
            - `target_value`: the item to look for in the queue

        :Return:
            - The 1st instance that matches `target_value`, OR
            - `None`: if NO match was found
        """
        
        # STEP 1: Iterate through every item in the queue
        for i in range(0, self.len()):

            # STEP 2: Return the instance if MATCHED
            if (self.arr[i] == target_value):
                return self.arr[i]

        # STEP 3: Indicate that no matches were found
        return None

    def __recursive_search(self, target_value, i = 0):
        """
        RECURSIVLEY searches the queue for the 1st instance that matches 
        `target_value`.

        :Parameters:
            - `target_value`: the item to look for in the queue
            - `i` (optional): the INDEX in the queue to query

        :Return:
            - The 1st instance that matches `target_value`, OR
            - `None`: if NO match was found
        """
        
        # BASE CASE 1: No match was found
        if (i >= self.len()):
            return None

        # BASE CASE 2: A match was found
        if (self.arr[i] == target_value):
            return self.arr[i]

        # RECURSIVE CASE: more items to traverse
        return self.__recursive_search(target_value, i + 1)

    def search(self, target_value, mode = 'i'):
        """
        SEARCHES for the 1st instance that matches `target_value`.

        :Parameters:
            - `target_value`: the item to look for in the queue
            - `mode` (optional): a SINGLE character `str` that indicates if  
              the queue search is conducted iteratively 'i' (default), or 
              recursively 'r'

        :Return:
            - The 1st instance that matches `target_value`, OR
            - `None`: if NO match was found
        """

        # CASE A: Mode is an INAPPROPRIATE type
        if (not isinstance(mode, str)):
            raise TypeError("`mode` must of TYPE `str`")

        # CASE B: Use the ITERATIVE search method
        elif (mode == 'i'):
            return self.__iterative_search(target_value)

        # CASE C: Use the RECURSIVE search method
        elif (mode == 'r'):
            return self.__recursive_search(target_value)

        # CASE D: Mode is an INAPPROPRIATE value
        else:
            raise ValueError("`mode` must be of VALUE 'i' or 'r'")