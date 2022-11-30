import pytest
import os
import sys

# Run all tests in the repository root.
repo_root = os.path.dirname(os.getcwd())
os.chdir(repo_root)

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

_ = pytest.main(sys.argv[1:])
