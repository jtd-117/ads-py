# @file     array_stack.py
# @brief    A file for implementing an array-based stack
# @author   Jude Thaddeau Data
# @note     GitHub: https://github.com/jtd-117
# ---------------------------------------------------------------------------- #

class ArrStack(object):
    """
    An INTERFACE for an array-based stack.
    """

    def __init__(self):
        self._arr = []

    def len(self):
        return len(self._arr)
    
    @property
    def arr(self):
        """
        The ARRAY implemented as a STACK.
        """
        return self._arr
    
    @arr.setter
    def arr(self, i, newValue):
        """
        REPLACES the value at index `i` with `newValue`.

        :Parameters:
            - `i`: the INDEX to access the stack
            - `newValue`: the item to replace value at index `i`
        """
        self._arr[i % self.len()] = newValue
    
    @arr.deleter
    def arr(self):
        """
        RESETS the array to ZERO elements.
        """
        self._arr = []

    def push(self, newValue):
        """
        ADDS a `newValue` at the END of the array.

        :Parameters:
            - `newValue`: the item to be added at the END of the array

        :Return:
            The NEWLY added LAST item in the stack
        """

        # STEP 1: Add the value at the END of the stack
        self.arr.append(newValue)

        # STEP 2: Return the newly LAST item of the stack
        return self.arr[self.len() - 1]

    def pop(self):
        """
        REMOVES the item at the END of the array.

        :Return:
            - The NEW & LAST item in the stack
            - `None`: if the stack is EMPTY
        """
        
        # STEP 1: Check of the stack is EMPTY
        if (self.len() == 0):
            return None

        # STEP 2: Delete the LAST item
        self.arr.pop(self.len() - 1)

        # STEP 3A: Only return the LASY item if non-empty
        if (self.len() > 0):
            return self.arr[self.len() - 1]
        
        # STEP 3B: Indicate the stack is now empty after the pop
        return None

    def __iterativeSearch(self, targetValue):
        """
        ITERATIVELY searches the stack for the 1st instance that matches 
        `targetValue`.

        :Parameters:
            - `targetValue`: the item to look for in the stack

        :Return:
            - The 1st instance that matches `targetValue`
            - `None`: if NO match was found
        """
        
        # STEP 1: Iterate through every item in the stack
        for i in range(0, self.len()):

            # STEP 2: Return the instance if MATCHED
            if (self.arr[i] == targetValue):
                return self.arr[i]

        # STEP 3: Indicate that no matches were found
        return None

    def __recursiveSearch(self, targetValue, i = 0):
        """
        RECURSIVLEY searches the stack for the 1st instance that matches 
        `targetValue`.

        :Parameters:
            - `targetValue`: the item to look for in the stack
            - `i` (optional): the INDEX in the stack to query

        :Return:
            - The 1st instance that matches `targetValue`
            - `None`: if NO match was found
        """
        
        # BASE CASE 1: No match was found
        if (i >= self.len()):
            return None

        # BASE CASE 2: A match was found
        if (self.arr[i] == targetValue):
            return self.arr[i]

        # RECURSIVE CASE: more items to traverse
        return self.__recursiveSearch(targetValue, i + 1)

    def search(self, targetValue, mode = 'i'):
        """
        SEARCHES for the 1st instance that matches `targetValue`

        :Parameters:
            - `targetValue`: the item to look for in the stack
            - `mode` (optional): a SINGLE character `str` that indicates if  
              the stack search is conducted iteratively 'i' (default), or 
              recursively 'r'

        :Return:
            - The 1st instance that matches `targetValue`
            - `None`: if NO match was found
        """

        # CASE A: Mode is an INAPPROPRIATE type
        if (not isinstance(mode, str)):
            raise TypeError("`mode` must of TYPE `str`")

        # CASE B: Use the ITERATIVE search method
        elif (mode == 'i'):
            result = self.__iterativeSearch(targetValue)

        # CASE C: Use the RECURSIVE search method
        elif (mode == 'r'):
            result = self.__recursiveSearch(targetValue)

        # CASE D: Mode is an INAPPROPRIATE value
        else:
            raise ValueError("`mode` must be of VALUE 'i' or 'r'")

        return result