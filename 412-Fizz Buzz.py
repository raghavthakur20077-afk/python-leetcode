class Solution:
    def fizzBuzz(self, n):
        
        # Create an empty list to store our answers
        answer = []

        # Loop from 1 to n
        # n + 1 is used because range() does not include the ending value
        for i in range(1, n + 1):

            # Check if i is divisible by both 3 and 5
            # 15 is divisible by both 3 and 5
            if i % 15 == 0:
                answer.append("FizzBuzz")

            # Check if i is divisible by 3
            elif i % 3 == 0:
                answer.append("Fizz")

            # Check if i is divisible by 5
            elif i % 5 == 0:
                answer.append("Buzz")

            # If none of the above conditions are true
            else:
                # Convert the number into a string and add it to the list
                answer.append(str(i))

        # Return the final list
        return answer
