from setuptools import setup

setup(
    name="test-jacques-deploy",
    entry_points={
        "console_scripts": [
            "test-jacques-deploy = test_jacques_deploy:main",
        ],
    },
)
