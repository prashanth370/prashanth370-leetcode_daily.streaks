from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque(range(len(deck)))
        result = [0] * len(deck)
        for card in deck:
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        return result



















# Let's go through the detailed iteration of the deckRevealedIncreasing function using the example test case deck1 = [17, 13, 11, 2, 3, 5, 7].

# Step 1: Sorting the input deck
# The input deck is [17, 13, 11, 2, 3, 5, 7]. After sorting it, we get [2, 3, 5, 7, 11, 13, 17].

# Step 2: Initializing the queue
# We initialize a deque with the indices of the cards in the deck, in the order they are currently present. So, queue becomes deque([0, 1, 2, 3, 4, 5, 6]).

# Step 3: Initializing the result array
# We initialize an empty array result with the same length as the deck, which is [0, 0, 0, 0, 0, 0, 0].

# Step 5: Iterating through the deck and revealing cards
# We iterate through the sorted deck [2, 3, 5, 7, 11, 13, 17].

# Iteration 1:
# card = 2
# We reveal the card 2 and add it to the result array at the position of the top card in the deck.
# Since queue is not empty, we rotate the queue so that the next card to be revealed moves to the back.
# result = [2, 0, 0, 0, 0, 0, 0]
# queue = deque([1, 2, 3, 4, 5, 6, 0])
# Iteration 2:
# card = 3
# We reveal the card 3 and add it to the result array.
# Rotate the queue.
# result = [2, 3, 0, 0, 0, 0, 0]
# queue = deque([2, 3, 4, 5, 6, 0, 1])
# Iterations 3-6:
# Similar steps are repeated for cards 5, 7, 11, and 13.
# After each iteration, we reveal the card, add it to the result array, and rotate the queue.
# Iteration 7:
# card = 17
# We reveal the card 17 and add it to the result array.
# Since it's the last card, we don't need to rotate the queue anymore.
# result = [2, 3, 5, 7, 11, 13, 17]
# queue = deque([])
# Step 6: Returning the result array
# We return the result array [2, 3, 5, 7, 11, 13, 17].

# This process ensures that the cards are revealed in increasing order as required by the problem statement.


# Sorting the input deck: Sorting the deck takes O(n log n) time, where n is the number of cards in the deck.
# Initializing the queue: Initializing the queue takes O(n) time, where n is the number of cards in the deck.
# Iterating through the sorted deck: In the worst case, we iterate through each card in the sorted deck once. This takes O(n) time.
# Inside the loop, popping an element from the left of the queue (queue.popleft()) and appending to the result array (result[queue.popleft()] = card) both take O(1) time.
# Rotating the queue (queue.append(queue.popleft())) also takes O(1) time.


# Sorting the input deck: Sorting is typically performed in-place, so it doesn't incur additional space complexity. It takes O(1) extra space.
# Initializing the queue: We initialize a deque to store the indices of the cards. The size of the deque is O(n), where n is the number of cards in the deck.
# Initializing the result array: We initialize an array to store the order of revealed cards. The size of the result array is also O(n).
# Overall, the space complexity is O(n) due to the additional space required for the queue and the result array.
