"""

Design a food rating system that can do the following:

Modify the rating of a food item listed in the system.
Return the highest-rated food item for a type of cuisine in the system.
Implement the FoodRatings class:

FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes 
the system. The food items are described by foods, cuisines and ratings, all of 
which have a length of n.

foods[i] is the name of the ith food,
cuisines[i] is the type of cuisine of the ith food, and
ratings[i] is the initial rating of the ith food.

void changeRating(String food, int newRating) Changes the rating 
of the food item with the name food.

String highestRated(String cuisine) Returns the name of the food 
item that has the highest rating for the given type of cuisine. If there 
is a tie, return the item with the lexicographically smaller name.

Note that a string x is lexicographically smaller than string y if x comes 
before y in dictionary order, that is, either x is a prefix of y, or if i 
is the first position such that x[i] != y[i], then x[i] comes before y[i] 
in alphabetic order.

Example 1:

Input
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

Explanation
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than "sushi".

Constraints:

1 <= n <= 2 * 104
n == foods.length == cuisines.length == ratings.length
1 <= foods[i].length, cuisines[i].length <= 10
foods[i], cuisines[i] consist of lowercase English letters.
1 <= ratings[i] <= 108
All the strings in foods are distinct.
food will be the name of a food item in the system across all calls to changeRating.
cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated.
At most 2 * 104 calls in total will be made to changeRating and highestRated.

Takeaway:

Using defaultdict for lists as values is cool.

Instead of sorting every time which is NOT a good idea, sort 
them as soon as you have them

Using heaps are great!

from heapq import heappush, heappop, heapify

"""

from collections import defaultdict

class FoodRatings_:
    """This class works but gives a Timeout Error for long inputs.
    So does it work? Idk.
    """
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self._all_menu = list(zip(foods, cuisines, ratings))
        
        self._cuisines_map = defaultdict(list)
        for food, cuisine, rating in self._all_menu:
            self._cuisines_map[cuisine].append([food, rating])

    def changeRating(self, food: str, newRating: int) -> None:
        """Changes the rating of the food item with the name food."""
        # find the cuisine
        cuisine = None
        for elem in self._all_menu:
            if elem[0] == food:
                cuisine = elem[1]
                break
        for entry in self._cuisines_map[cuisine]:
            if entry[0] == food:
                entry[1] = newRating
                return
        
    def highestRated(self, cuisine: str) -> str:
        """
        Returns the name of the food item that has the highest rating 
        for the given type of cuisine. If there is a tie, return the 
        item with the lexicographically smaller name.
        """
        # sort the elements
        self._cuisines_map[cuisine].sort(key=lambda x: (-x[1], x[0]))
        # return highest
        return self._cuisines_map[cuisine][0][0]

# We have a heap for each cuisine. We push to the heap whenever we update a rating. We 
# check the rating is current before returning the Highest rating.

from collections import defaultdict
    
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # food to rating map
        self.rating = {}
        # cuisines to rating and food
        self.cuisines = defaultdict(list)
        # food to cuisine map
        self.food_cuisine = {}
        
        for i in range(len(foods)):
            # no need to zip this way.
            food, r, cuisine = foods[i], ratings[i], cuisines[i]
            # because in default we have a min heap in Python
            self.rating[food] = -r
            # food to cuisine map
            self.food_cuisine[food] = cuisine
            # this list for each cuisine is a heap
            # we multiply by -1 to get a max heap instead of min
            heapq.heappush(self.cuisines[cuisine], (-r, food))
        

    def changeRating(self, food: str, newRating: int) -> None:
        # set the new rating
        self.rating[food] = -newRating
        # find the cuisine of the food
        cuisine = self.food_cuisine[food]
        # add new rating for the food
        heapq.heappush(self.cuisines[cuisine], (-newRating, food))
        

    def highestRated(self, cuisine: str) -> str:
        
        # that while loop is just removing old values of the foods which are not valid anymore, 
        # and we care about the value at the top of the heap. So as long as the food at the top 
        #  of our heap is holding the right rating, then we take that as an answer. The time 
        # complexity is within the number of the function calls as the duplicate ratings 
        # are generated from the "ChangeRating" method.
        
        # pop all the old ratings from the cuisine map using the rating map 
        while self.rating[self.cuisines[cuisine][0][1]] != self.cuisines[cuisine][0][0]:
            heapq.heappop(self.cuisines[cuisine])
        # return the right rating - the latest
        return self.cuisines[cuisine][0][1]
