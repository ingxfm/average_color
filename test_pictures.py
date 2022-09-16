# built-in
import unittest
import glob

# own
from pictures import AverageColor


class TestPictures(unittest.TestCase):

    def test_determine_color(self):
        files = glob.glob(r"images/t*2x2.png")
        results_expected = {'blue': [0, 0, 255],
                            "red": [255, 0, 0],
                            "green": [0, 255, 0]}
        results_obtained = {}
        for file in files:
            color = AverageColor()
            name, color_ = color.determine_color(file=file)
            results_obtained[name] = color_
        self.assertEqual(results_expected, results_obtained)


if __name__ == "__main__":
    unittest.main()
