# Create a class named Solution.
# LeetCode uses this class to run our solution.
class Solution:

    # Create a function named kidsWithCandies.
    #
    # candies = list containing the number of candies each kid has
    # extraCandies = number of extra candies we can give to a kid
    def kidsWithCandies(self, candies, extraCandies):

        # Find the largest number of candies any kid currently has.
        #
        # Example:
        # candies = [2, 3, 5, 1, 3]
        # greatest = 5
        greatest = max(candies)

        # Create an empty list.
        # We will store True or False for each kid.
        answer = []

        # Go through each kid's number of candies.
        #
        # For example:
        # candies = [2, 3, 5, 1, 3]
        #
        # candy will become:
        # 2 → 3 → 5 → 1 → 3
        for candy in candies:

            # Add the extra candies to the current kid's candies.
            #
            # Then check whether the result is greater than
            # or equal to the current greatest number.
            if candy + extraCandies >= greatest:

                # If the kid can have the greatest number of candies,
                # add True to the answer list.
                answer.append(True)

            else:

                # If the kid still cannot have the greatest number,
                # add False to the answer list.
                answer.append(False)

        # Return the final list containing True/False
        # for every kid.
        return answer
