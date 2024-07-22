class Solution(object):
    def sortPeople(self, names, heights):
        hashmap = {}   
        for i in range(len(names)):
            hashmap[heights[i]] = names[i]
        heights.sort(reverse=True)
        for i in range(len(names)):
            h = heights[i]
            names[i] = hashmap[h]

        return names
            
