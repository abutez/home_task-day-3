#class BinarySearch inheriting from class list and return a dictionary
class BinarySearch(list):
    def __init__(self, leng, step):
        self.search_list = []
        #
        search_gen = (n for n in range(step, (step * leng) + 1, step))
        for item in search_gen:
            self.append(item)
        self.length = len(self)
#earch index function

    def search(self, a):
        count = 0
        index = None
        search_index = (self.length // 2) - 1
        found = False
        temp = self.length - search_index
#while loop to do a binary search if the index elements and return a dictionary of the count and the index of the number in question
        while found is False:
            if search_index >= self.length or search_index<0:
                index = -1
                found = True
            elif self[search_index] == a:
                index = search_index
                found = True
            elif temp==0:
                index=-1
                found=True
            elif self[search_index] > a:
                search_index = search_index - (temp // 2)
                temp = (temp // 2)

            elif self[search_index] < a:
                search_index = search_index + (temp//2)
                temp = (temp // 2)


            count += 1
        return {"count": count, "index": index}