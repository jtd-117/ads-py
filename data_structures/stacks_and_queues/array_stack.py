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
    def arr(self, i, new_value):
        """
        REPLACES the value at index `i` with `new_value`.

        :Parameters:
            - `i`: the INDEX to access the stack
            - `new_value`: the item to replace value at index `i`
        """
        self._arr[i % self.len()] = new_value
    
    @arr.deleter
    def arr(self):
        """
        RESETS the array to ZERO elements.
        """
        self._arr = []

    def push(self, new_value):
        """
        ADDS a `new_value` at the END of the array.

        :Parameters:
            - `new_value`: the item to be added at the END of the array

        :Return:
            The NEWLY added LAST item in the stack
        """

        # STEP 1: Add the value at the END of the stack
        self.arr.append(new_value)

        # STEP 2: Return the newly LAST item of the stack
        return self.arr[self.len() - 1]

    def pop(self):
        """
        REMOVES the item at the END of the array.

        :Return:
            - The NEW & LAST item in the stack, OR
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

    def __iterative_search(self, new_value):
        """
        ITERATIVELY searches the stack for the 1st instance that matches 
        `new_value`.

        :Parameters:
            - `new_value`: the item to look for in the stack

        :Return:
            - The 1st instance that matches `new_value`, OR
            - `None`: if NO match was found
        """
        
        # STEP 1: Iterate through every item in the stack
        for i in range(0, self.len()):

            # STEP 2: Return the instance if MATCHED
            if (self.arr[i] == new_value):
                return self.arr[i]

        # STEP 3: Indicate that no matches were found
        return None

    def __recursive_search(self, new_value, i = 0):
        """
        RECURSIVLEY searches the stack for the 1st instance that matches 
        `new_value`.

        :Parameters:
            - `new_value`: the item to look for in the stack
            - `i` (optional): the INDEX in the stack to query

        :Return:
            - The 1st instance that matches `new_value`, OR
            - `None`: if NO match was found
        """
        
        # BASE CASE 1: No match was found
        if (i >= self.len()):
            return None

        # BASE CASE 2: A match was found
        if (self.arr[i] == new_value):
            return self.arr[i]

        # RECURSIVE CASE: more items to traverse
        return self.__recursive_search(new_value, i + 1)

    def search(self, new_value, mode = 'i'):
        """
        SEARCHES for the 1st instance that matches `new_value`

        :Parameters:
            - `new_value`: the item to look for in the stack
            - `mode` (optional): a SINGLE character `str` that indicates if  
              the stack search is conducted iteratively 'i' (default), or 
              recursively 'r'

        :Return:
            - The 1st instance that matches `new_value`, OR
            - `None`: if NO match was found
        """

        # CASE A: Mode is an INAPPROPRIATE type
        if (not isinstance(mode, str)):
            raise TypeError("`mode` must of TYPE `str`")

        # CASE B: Use the ITERATIVE search method
        elif (mode == 'i'):
            result = self.__iterative_search(new_value)

        # CASE C: Use the RECURSIVE search method
        elif (mode == 'r'):
            result = self.__recursive_search(new_value)

        # CASE D: Mode is an INAPPROPRIATE value
        else:
            raise ValueError("`mode` must be of VALUE 'i' or 'r'")

        return result