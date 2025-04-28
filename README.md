
---

## Install and Run Locally

1. **Install all required libraries** by running:

    ```bash
    pip install -r requirements.txt
    ```

    - This installs `speedtest-cli`, `pytest`, `coverage`, and `pyinstaller`.
    - These libraries are **imported inside the Python code** and must be installed before running.

2. **Run the application**:

    ```bash
    python src/speed_test_app.py
    ```

3. **After the speed test results are displayed**, the application will **wait for the user to press ENTER** before closing the terminal.

## Build Executable Locally

1. Install PyInstaller if you haven't already:

    ```bash
    pip install pyinstaller
    ```

2. Build the executable:

    ```bash
    pyinstaller --onefile src/speed_test_app.py
    ```

3. The `.exe` file will be generated inside the `dist/` folder:

    ```
    dist/speed_test_app.exe
    ```

You can now run the `.exe` file directly, even on a machine that doesn't have Python installed.

## Testing and Coverage

- To run all unit and integration tests:

    ```bash
    python -m unittest discover tests
    ```

- To measure code coverage:

    ```bash
    coverage run -m unittest discover
    coverage report -m
    ```

- Test Coverage Goal: **≥ 75%**

## Technologies Used

| Component        | Technology            |
|------------------|-----------------------|
| Primary Language | Python 13             |
| Speed Testing    | speedtest-cli         |
| Packaging        | PyInstaller           |
| Unit Testing     | unittest + coverage.py|
| CI/CD Automation | GitHub Actions        |
| Deployment       | GitHub Releases       |

## Authors

- Antonette Di Diana

## Acknowledgments

- Original speed test script by [PyShark's tutorial](https://pyshark.com/test-internet-speed-using-python/).
- This project has been refactored, modularized, and expanded for DevOps final submission requirements, including CI/CD automation, testing, coverage, and packaging into an executable for single click deployment.

## License

This project is licensed for educational purposes.

