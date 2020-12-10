from config import settings

class Color_helper:
    def __init__(self, start_color, end_color, largest_weight, smallest_weight):
        self.start_color = start_color
        self.end_color = end_color
        self.smallest_weight = smallest_weight
        self.largest_weight = largest_weight
        self.number_of_colors = int(largest_weight - smallest_weight)
        self.RGB_list = self.create_linear_gradient()

    def create_linear_gradient(self):
        RGB_list = [self.start_color]
        # Calcuate a color at each evenly spaced value of t from 1 to n
        for t in range(1, self.number_of_colors):
            # Interpolate RGB vector for color at the current value of t
            curr_vector = [
                int(self.start_color[j] + (float(t)/(self.number_of_colors-1))*(self.end_color[j]-self.start_color[j]))
                for j in range(3)
            ]
            # Add it to our list of output colors
            RGB_list.append(curr_vector)
        return RGB_list

    def get_color(self, density):
        return self.RGB_list[int(density - self.smallest_weight - 1)]

start_color = [255, 195, 0]
end_color = [88, 24, 69]

#color_test = Color_helper(start_color, end_color)

