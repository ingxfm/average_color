# Built-in
from time import time
from collections import OrderedDict, namedtuple

# 3rd-party
import cv2
import numpy as np
from scipy.spatial import distance as dist


class AverageColor:

    def __init__(self):
        self.name = ""
        self.channels = None
        colors_ = OrderedDict({
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "black": (0, 0, 0),
            "white": (255, 255, 255),
        })
        self.img_rgb_values = np.ones((len(colors_), 1, 3), dtype="uint8")
        self.color_names = []

        for (i, (color_name, rgb_values)) in enumerate(colors_.items()):
            self.img_rgb_values[i] = rgb_values
            self.color_names.append(color_name)

    def determine_color(self, file):
        start_time_in_sec = time()
        src_img = cv2.imread(f"{file}")  # images in BGR
        average_color_pixel_row = np.average(src_img, axis=0)
        average_color_rgb_values = np.average(average_color_pixel_row, axis=0)
        average_color_img_values = np.ones(src_img.shape, dtype=np.uint8)
        average_color_img_values[:, :] = average_color_rgb_values
        # print(src_img)
        # print(average_color_pixel_row)
        # print(f"k: {average_color_rgb_values}")
        # print(average_color_rgb_values.shape)  # shape of the array
        # print(f"This is the average color: {average_color_rgb_values}.\n")

        distances = []
        for (i, row) in enumerate(self.img_rgb_values):
            distance = dist.euclidean(row[0][::-1], average_color_rgb_values)
            distances.append(distance)
            # print(f"The index is {i}, the row is {row}, and the row[0] is {row[0][::-1]}"
            #       f"\n and the distance is sqrt(  {row[0][::-1]}^2 - {average_color_rgb_values}^2  ).")
            # print(f"The average color is {average_color_rgb_values}.")
            # print(f"The distance is {distance:.1f} bits.\n")

        min_distance = min(distances)
        color_position = distances.index(min_distance)
        average_color_name = self.color_names[color_position]
        # print(color_position)
        # print(average_color_name)
        # cv2.imshow('Source image', src_img)
        # cv2.imshow('Average Color', average_color_img_values)
        end_time_in_sec = time()
        run_time_in_sec = end_time_in_sec - start_time_in_sec
        # print(f"The runtime is {run_time_in_sec:.2e} sec.")
        # cv2.waitKey(0)

        # print(image_info)
        # print(type(image_info))
        return average_color_name, list(average_color_rgb_values[::-1])
