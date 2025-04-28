import unittest
from unittest.mock import patch, MagicMock
from src.speed_test_app import run_speedtest, display_results

class TestSpeedTestApp(unittest.TestCase):

    @patch('src.speed_test_app.speedtest.Speedtest')
    def test_run_speedtest_success(self, mock_speedtest):
        mock_instance = MagicMock()
        mock_instance.download.return_value = 100_000_000
        mock_instance.upload.return_value = 50_000_000
        mock_instance.results.ping = 20
        mock_instance.get_best_server.return_value = {
            "host": "mockserver",
            "country": "Mockland"
        }
        mock_speedtest.return_value = mock_instance

        results = run_speedtest()

        self.assertEqual(results['ping'], 20)
        self.assertAlmostEqual(results['download'], 100, places=1)
        self.assertAlmostEqual(results['upload'], 50, places=1)

    @patch('src.speed_test_app.speedtest.Speedtest')
    def test_run_speedtest_exception(self, mock_speedtest):
        mock_speedtest.side_effect = Exception("Network error")

        with self.assertRaises(Exception) as cm:
            run_speedtest()

        self.assertEqual(str(cm.exception), "Network error")

    def test_display_results(self):
        results = {"ping": 20, "download": 100, "upload": 50}
        display_results(results)

if __name__ == "__main__":
    unittest.main()
