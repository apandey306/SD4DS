from refactoring import _weighted_mean


def test_weighted_mean():
    result = _weighted_mean([1, 2, 4], [1, 2, 4])
    assert result == 3

    empty_list_result = _weighted_mean([], [])
    assert not empty_list_result

def test_weighted_mean_normal(self):
    self.assertAlmostEqual(_weighted_mean([1, 2, 3], [1, 1, 1]), 2.0)
    self.assertAlmostEqual(_weighted_mean([1, 2, 3], [0.5, 0.25, 0.25]), 1.5)

def test_weighted_mean_empty_lists(self):
    self.assertIsNone(_weighted_mean([], []))

def test_weighted_mean_zero_weights(self):
    self.assertIsNone(_weighted_mean([1, 2, 3], [0, 0, 0]))

def test_weighted_mean_unequal_length(self):
    with self.assertRaises(ValueError):
        _weighted_mean([1, 2], [1, 2, 3])

def test_weighted_mean_non_numeric_values(self):
    with self.assertRaises(TypeError):
        _weighted_mean(['a', 'b', 'c'], [1, 2, 3])
