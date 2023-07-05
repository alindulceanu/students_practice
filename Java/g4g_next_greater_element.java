/* Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.*/

import java.util.Stack;

public class g4g_next_greater_element {

    public static long[] nextLargerElement(long[] arr, int n)
    { 
        Stack<Long> stack = new Stack<>();                      // Initializing the stack and the nextLargerElement array
        long[] larg = new long[n];

        for(int i = n - 1; i >= 0; i--){                        // Iterating backwards
            if(stack.empty()){                                  // First element will always result in -1
                larg[i] = -1;
            }
            while(!stack.empty() && arr[i] >= stack.peek()){    // Delete all elements that are not greater than the current one
                stack.pop();
            }

            if(stack.empty()){                                  // If all the elements have been deleted, there is not greater value
                larg[i] = -1;
            }
            else{
                larg[i] = stack.peek();                         // The last value that remained in the stack should be greater than the current one, so we update the array
            }

            stack.push(arr[i]);                                 // Add the current value in the stack
        }

        return larg;
    }
}