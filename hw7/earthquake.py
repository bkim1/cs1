# author: Branden Kim
# assignment: HW7
# description: Earthquake analysis


import numpy
import matplotlib.pyplot as plt


class EarthquakeData:

    def __init__(self, filename='earthquakes.txt'):
        self.quake_data = {}

        with open(filename, 'r') as f:
            for row in f.readlines():
                data = row.split(' ')
                if len(data) > 7:
                    location = ' '.join((x.rstrip() for x in data[6:]))
                else:
                    location = data[-1].rstrip()

                entry = self.quake_data.get(location, [])
                entry.append(data[ : 6])
                self.quake_data[location] = entry
        
        self.intensities = ['micro', 'light', 'lower', 'average', 'big', 'strong', 'disaster']
        self.num_per_intensity = [0 for _ in range(len(self.intensities))]

        self.hawaii_intensity = []

        self.occurrences = {}

        self.strongest_loc = ''
        self.strongest_magnitude = 0

        self.__setup()

    def run(self):
        self.__generate_intensity_chart()
        self.__generate_hawaii_chart()
        self.__generate_occurrences_chart()

        print(f'The strongest earthquake was in {self.strongest_loc} ' \
              f'{self.strongest_magnitude} of magnitude')

    def __setup(self):
        self.__group_by_intensity()
        self.__group_hawaii_data()
        self.__find_occurrences()
        self.__find_strongest()
    
    def __group_by_intensity(self):
        for location in self.quake_data:
            for quake in self.quake_data[location]:
                magnitude = float(quake[0])
                if magnitude < 3:
                    self.num_per_intensity[0] += 1
                elif magnitude < 3.9:
                    self.num_per_intensity[1] += 1
                elif magnitude < 4.9:
                    self.num_per_intensity[2] += 1
                elif magnitude < 5.9:
                    self.num_per_intensity[3] += 1
                elif magnitude < 6.9:
                    self.num_per_intensity[4] += 1
                elif magnitude < 7.9:
                    self.num_per_intensity[5] += 1
                else:
                    self.num_per_intensity[6] += 1

    def __group_hawaii_data(self):
        self.hawaii_intensity = [x[0] for x in self.quake_data.get('HAWAII REGION, HAWAII', [])]

    def __find_occurrences(self):
        for loc in self.quake_data:
            if len(self.quake_data[loc]) > 4:
                self.occurrences[loc] = len(self.quake_data[loc])

    def __find_strongest(self):
        for loc in self.quake_data:
            temp_max = max(self.quake_data[loc], key=lambda x: float(x[0]))
            magnitude = float(temp_max[0])

            if magnitude > self.strongest_magnitude:
                self.strongest_magnitude = magnitude
                self.strongest_loc = loc

    def __generate_intensity_chart(self):
        plt.bar(self.intensities, self.num_per_intensity)
        plt.ylabel('Amount of Earthquakes')
        plt.title('Earthquake Intensity')
        plt.show()

    def __generate_hawaii_chart(self):
        plt.plot(self.hawaii_intensity)
        plt.ylabel('Intensity')
        plt.title('Earthquake Intensities in HAWAII REGION, HAWAII')
        plt.show()

    def __generate_occurrences_chart(self):
        data, labels = [], []
        for loc in self.occurrences:
            labels.append(loc)
            data.append(self.occurrences[loc])

        plt.pie(data, labels=labels)
        plt.title('Occurrences')
        plt.show()


if __name__ == '__main__':
    EarthquakeData().run()

