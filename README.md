# Internet Speed Test CLI Executable

## Project Overview

This project converts a Python CLI application into a Windows `.exe` executable which assesses internet speed.

The application measures:
- Ping (ms)
- Download speed (Mbps)
- Upload speed (Mbps)

The script is made into a `.exe` executable file using PyInstaller. 
CI/CD automation has been implemented to automatically build and release new versions.

## Features

- Converts a Python script into a Windows `.exe` executable
- Displays ping, download, and upload speeds
- Keeps CLI open until the user presses ENTER to exit
- Automated testing with unittest + coverage.py
- GitHub Actions CI/CD pipeline builds and releases executable
- Final `.exe` executable is downloadable from GitHub Releases

## Install and Run Locally

1. Run the following command to install all required libraries:

    ```bash
    pip install -r requirements.txt
    ```

    - Installs `speedtest-cli`, `pytest`, `coverage`, and `pyinstaller`
    - These libraries are imported inside the Python code
    - Install before running

2. Run the application:

    ```bash
    python src/speed_test_app.py
    ```

3. Application will wait for the user to press ENTER before closing the terminal after the speed test results are displayed.

## Build Executable Locally

1. Install PyInstaller (if you haven't already):

    ```bash
    pip install pyinstaller
    ```

2. Build executable:

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

- Test Coverage Goal: ≥ 75%

## Technologies Used

| Component        | Technology            |
|------------------|-----------------------|
| Primary Language | Python 13             |
| Speed Testing    | speedtest-cli         |
| Packaging        | PyInstaller           |
| Unit Testing     | unittest + coverage.py|
| CI/CD Automation | GitHub Actions        |
| Deployment       | GitHub Releases       |

Note: The application uses GitHub Releases as its deployment platform.

## Authors

- Antonette Di Diana

## Acknowledgments

- Original internet speed test project inspired by [PyShark's tutorial](https://pyshark.com/test-internet-speed-using-python/).
- This project received multiple optimizational treatments in preparation for DevOps delivery requirements through implementation of CI/CD automation, testing, coverage measurement, and distribution as a single click deployable executable.
