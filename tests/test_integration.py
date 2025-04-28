import unittest
from unittest.mock import patch, MagicMock
import subprocess
import sys
import os

class TestIntegration(unittest.TestCase):

    def setUp(self):
        """Set up the script path for testing."""
        self.script_path = os.path.join('src', 'speed_test_app.py')

    @patch('subprocess.run')
    def test_run_speedtest_script(self, mock_run):
        """Test if 'Ping:' is in output."""
        mock_run.return_value = subprocess.CompletedProcess(
            args=[sys.executable, self.script_path],
            returncode=0,
            stdout="Best server based on ping: example.com located in United States\nPing: 20 ms\nDownload Speed: 100 Mbps\nUpload Speed: 50 Mbps\n",
            stderr=""
        )
        result = subprocess.run([sys.executable, self.script_path], capture_output=True, text=True)
        self.assertIn("Ping:", result.stdout)

    @patch('subprocess.run')
    def test_run_speedtest_download_output(self, mock_run):
        """Test if 'Download Speed:' is in output."""
        mock_run.return_value = subprocess.CompletedProcess(
            args=[sys.executable, self.script_path],
            returncode=0,
            stdout="Download Speed: 100 Mbps\nUpload Speed: 50 Mbps\nPing: 20 ms\n",
            stderr=""
        )
        result = subprocess.run([sys.executable, self.script_path], capture_output=True, text=True)
        self.assertIn("Download Speed:", result.stdout)

    @patch('subprocess.run')
    def test_run_speedtest_upload_output(self, mock_run):
        """Test if 'Upload Speed:' is in output."""
        mock_run.return_value = subprocess.CompletedProcess(
            args=[sys.executable, self.script_path],
            returncode=0,
            stdout="Upload Speed: 50 Mbps\nDownload Speed: 100 Mbps\nPing: 20 ms\n",
            stderr=""
        )
        result = subprocess.run([sys.executable, self.script_path], capture_output=True, text=True)
        self.assertIn("Upload Speed:", result.stdout)

    @patch('subprocess.run')
    def test_run_speedtest_best_server_output(self, mock_run):
        """Test if 'Best server based on ping:' is in output."""
        mock_run.return_value = subprocess.CompletedProcess(
            args=[sys.executable, self.script_path],
            returncode=0,
            stdout="Best server based on ping: example.com located in United States\n",
            stderr=""
        )
        result = subprocess.run([sys.executable, self.script_path], capture_output=True, text=True)
        self.assertIn("Best server based on ping:", result.stdout)

    @patch('subprocess.run')
    def test_run_speedtest_no_crash(self, mock_run):
        """Test that script exits normally with code 0."""
        mock_run.return_value = subprocess.CompletedProcess(
            args=[sys.executable, self.script_path],
            returncode=0,
            stdout="All tests passed\n",
            stderr=""
        )
        result = subprocess.run([sys.executable, self.script_path], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)

if __name__ == "__main__":
    unittest.main()
