import unittest
import subprocess
import sys
import os

class TestIntegration(unittest.TestCase):

    def test_run_speed_test_script(self):
        script_path = os.path.join('src', 'speed_test_app.py')
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True
        )

        #debugging output if test fails
        if result.returncode != 0 or not result.stdout:
            print("\nSTDOUT:\n", result.stdout)
            print("\nSTDERR:\n", result.stderr)

        #test based on either pass or fail
        if result.returncode == 0:
            # Only assert Ping: if it actually worked
            self.assertIn("Ping:", result.stdout)
            self.assertIn("Download Speed:", result.stdout)
            self.assertIn("Upload Speed:", result.stdout)
        else:
            #if fail check that error message is printed
            self.assertIn("Error", result.stderr)

if __name__ == "__main__":
    unittest.main()
