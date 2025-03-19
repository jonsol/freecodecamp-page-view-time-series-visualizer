import unittest
import time_series_visualizer
import matplotlib.pyplot as plt
import seaborn as sns

class TestTimeSeriesVisualizer(unittest.TestCase):
    def setUp(self):
        """Setup: Run all functions before testing."""
        self.line_plot = time_series_visualizer.draw_line_plot()
        self.bar_plot = time_series_visualizer.draw_bar_plot()
        self.box_plot = time_series_visualizer.draw_box_plot()

    def test_line_plot(self):
        """Test if the line plot is created successfully."""
        self.assertIsInstance(self.line_plot, plt.Figure)

    def test_bar_plot(self):
        """Test if the bar plot is created successfully."""
        self.assertIsInstance(self.bar_plot, plt.Figure)

    def test_box_plot(self):
        """Test if the box plot is created successfully."""
        self.assertIsInstance(self.box_plot, plt.Figure)


if __name__ == "__main__":
    unittest.main()
