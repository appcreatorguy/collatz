build: clean
	py setup.py bdist_wheel --universal
clean:
	rm -rf collatz.egg-info
	rm -rf dist
	rm -rf build