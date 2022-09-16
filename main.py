# Built-in
import glob

# 3rd-party
import numpy as np

# own
from pictures import AverageColor


def getting_avg_color(files, file_dict):
    for file in files:
        picture_color_info = AverageColor()
        avg_color_rgb_values_ = picture_color_info.determine_color(file=file)
        file_dict[f"{file}"] = avg_color_rgb_values_
        # print(file)
    return file_dict
    # print(f"The current dictionary is {images_average_colors}.\n")


def main():
    images_average_colors: dict = {}
    files_jpg = glob.glob(r"images/*.jpg")
    files_png = glob.glob(r"images/*.png")
    files = files_png + files_jpg
    try:
        images_average_colors = getting_avg_color(files=files, file_dict=images_average_colors)
        # print(files)
        # print(f"The current dictionary is {images_average_colors}.\n")
        # print(images_average_colors)

    except Exception as exc:
        print(exc)
        main()


if __name__ == "__main__":
    main()
