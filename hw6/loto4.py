# author: Branden Kim
# assignment: 6
# description: Loto4 Program

import sys


class Loto4:

    def __init__(self, filename):
        self.num_freq, self.nums_found = {}, set()
        self.drawings, self.ordered_freq = [], []
        self.repitions, self.nums_not_drawn, self.most_drawn = [], [], []

        with open(filename, 'r') as f:
            for day in f.readlines():
                numbers = day[:len(day) - 2].split(',')
                numbers[0] = numbers[0].split('[')[1]
                if numbers:
                    self.drawings.append([int(num) for num in numbers])
        
        self.__get_frequencies()
        self.__sort_frequencies()
        self.__find_repitions()
        self.__find_missing()
        self.__get_most_drawn()

    def get_info(self):
        print(f'Frequencies: \n{self.num_freq}\n')
        print(f'Numbers drawn in decreasing order: \n{self.ordered_freq}\n')
        print(f'Repeated numbers: \n{self.repitions}\n')
        print(f'Numbers never drawn: \n{self.nums_not_drawn}\n')
        print(f'Most Drawn: \n{self.most_drawn}\n')
    
    def __get_frequencies(self):
        for day in self.drawings:
            for num in day:
                self.nums_found.add(num)
                self.num_freq[num] = self.num_freq.get(num, 0) + 1

    def __sort_frequencies(self):
        self.ordered_freq = sorted(self.num_freq, key=self.num_freq.get, reverse=True)

    def __find_repitions(self):
        for num in self.num_freq:
            if self.num_freq[num] > 1:
                self.repitions.append(num)

    def __find_missing(self):
        for num in range(1, 42):
            if num not in self.nums_found:
                self.nums_not_drawn.append(num)

    def __get_most_drawn(self):
        i = 0
        while i < len(self.ordered_freq) and len(self.most_drawn) < 4:
            same_freq = [self.ordered_freq[i]]
            c, num = 1, self.ordered_freq[i]
            next_num = self.ordered_freq[i+c]

            while i + c < len(self.ordered_freq) and \
                    self.num_freq[num] == self.num_freq[next_num]:
                same_freq.append(next_num)
                c += 1
                next_num = self.ordered_freq[i+c]
            
            same_freq.sort()
            x = 0
            while len(self.most_drawn) < 4 and x < len(same_freq):
                self.most_drawn.append(same_freq[x])
                x += 1

            i += c


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'Loto4.txt'
    
    Loto4(filename).get_info()
