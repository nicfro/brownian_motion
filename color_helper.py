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
        # Calcuate a color at each evenly spaced value
        for t in range(1, self.number_of_colors):
            # Interpolate RGB vector
            curr_vector = [
                int(self.start_color[j] + (float(t)/(self.number_of_colors-1))*(self.end_color[j]-self.start_color[j]))
                for j in range(3)
            ]
            RGB_list.append(curr_vector)
        return RGB_list

    def get_color(self, density):
        return self.RGB_list[int(density - self.smallest_weight - 1)]

