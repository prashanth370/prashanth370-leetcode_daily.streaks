class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))

        people_sorted = sorted(people, key=lambda x:x[1], reverse=True)
        name = [person[0] for person in people_sorted]
        return name