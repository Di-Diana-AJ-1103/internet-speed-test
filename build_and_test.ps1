#install dependencies
pip install -r requirements.txt

#run all tests
python -m unittest discover tests

#generate and show coverage report
coverage run -m unittest discover
coverage report -m

#build executable
pyinstaller --onefile src/speed_test_app.py

Write-Output "Build and tests completed successfully!"
Write-Output "Executable is located inside /dist/"
