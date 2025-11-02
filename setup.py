from setuptools import setup, find_packages

setup(
    name="devops_tool",
    version="1.0.0",
    py_modules=["day7_devops_cli"],
    entry_points={
        "console_scripts": [
            "devops-tool = day7_devops_cli:main",
        ],
    },
)