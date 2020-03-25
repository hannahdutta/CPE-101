# Name:         Parth Ray
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Crime Time  
# Term:         Fall 2019
def main():
    crimes = open("crimes.tsv", "r")
    ids = []
    for i in crimes.readlines():
        if ("ROBBERY" in i.split("\t")[1]) and ids.count(int(i[0:i.find("\t")])) == 0:
            ids.append(int(i[0:i.find("\t")]))
    crimes.close()
    robobjs = sort_crimes([Robbery(i) for i in ids], "id")
    timess = open("times.tsv", "r")
    times = timess.readlines()
    for i in times[1:]:
        x = find_crime(robobjs, int(i[0:9]))
        if x != -1:  
            robobjs[x].convert_time(i[-7:-1])
    timess.close()
    robobjs = sort_crimes(robobjs, "time")
    fp = open("robberies.tsv", "w")
    fp.write("ID\tTime\n")
    for i in robobjs:
        fp.write(str(i))


def sort_crimes(crimes, by):
        for i in range(len(crimes)):
            min_idx = i
            if by == "id":
                minn = crimes[i].id                                        
                for j in range(i + 1, len(crimes)):
                    if crimes[j].id < minn:
                        minn = crimes[j].id
                        min_idx = j
            else:
                minn = crimes[i].time                                        
                for j in range(i + 1, len(crimes)):
                    if crimes[j].__lt__(crimes[min_idx]):
                        minn = crimes[j].time
                        min_idx = j           
            crimes[i], crimes[min_idx] = crimes[min_idx], crimes[i]
        return crimes


def find_crime(crimes, crime_id):
    start = 0
    end = len(crimes)
    while start < end:
        mid = (start + end) // 2
        if crimes[mid].id > crime_id:
            end = mid
        elif crimes[mid].id < crime_id:
            start = mid + 1
        else:
            return mid
    return -1
    

class Robbery:
        def __init__(self, crime_id):
            self.id = crime_id
            self.time = None
        

        def __eq__(self, other):
            return self.id == other.id


        def __repr__(self):
            if self.time == None:
                return f"{self.id}\tNone\n"
            elif self.time == 0:
                return f"{self.id}\t12:00AM\n"
            elif self.time < 100:
                return f"{self.id}\t12:{(self.time % 100) // 10}{self.time % 10}AM\n"
            elif self.time >= 1300:
                return f"{self.id}\t{(self.time - 1200) // 100}:{((self.time - 1200) % 100) // 10}{(self.time - 1200) % 10}PM\n"
            elif self.time < 1200:       
                return f"{self.id}\t{self.time // 100}:{(self.time % 100) // 10}{self.time % 10}AM\n"
            else:
                return f"{self.id}\t{self.time // 100}:{(self.time % 100) // 10}{self.time % 10}PM\n"


    #sets time from 24 hour str to 24 int
        def convert_time(self, string_time):
            self.time = int("".join(string_time.split(":")))
        
    #tells me if self is less than other
        def __lt__(self, other):
            if self.time == other.time:
                return self.id < other.id
            return self.time < other.time


if __name__ == "__main__":
    main()
