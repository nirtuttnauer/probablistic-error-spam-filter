"""Regression checks for the simulation harness (standard library only)."""

import unittest
from unittest.mock import patch

from tests import test_spam_filter as run_simulation


class SimulationTests(unittest.TestCase):
    def test_no_positive_filter_passes_error_limit(self):
        with patch("tests.SpamFilterA") as filter_class, patch("builtins.print") as output:
            filter_class.return_value.is_spam.return_value = False
            run_simulation(1)
        output.assert_any_call("Passed The Error Limit With Minimal Space? True")

    def test_all_positive_filter_exceeds_error_limit(self):
        # Every non-spam address is a false positive: the reported rate is 100%.
        with patch("tests.SpamFilterA") as filter_class, patch("builtins.print") as output:
            filter_class.return_value.is_spam.return_value = True
            run_simulation(1)
        output.assert_any_call("Passed The Error Limit With Minimal Space? False")


if __name__ == "__main__":
    unittest.main()
