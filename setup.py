# Update the code and upload the package to pypi
# 1. python ./setup.py bdist_wheel --universal
# 2. twine upload dist/simple_tensorflow_serving-x.x.x-py2.py3-none-any.whl

from setuptools import setup, find_packages

print("FIND PACKAGES")
print(find_packages())

# see https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
setup(
    name="serving",
    version=1.2,
    url="https://github.com/damianphung/flask_jinja_example",
    author="damianphung",
    description=
    "Example setup",
    packages= find_packages(),
    install_requires=[
        'flask',
        'jinja2',
        'flask-cors',
    ],
    package_data={
        "serving":  # Name of directory ( ie; package from packages=find_packages() )
            ["templates/*.html",
             "static/bootstrap*/css/*.css",
             "static/bootstrap*/js/*.js" # Is there a recursive way of installing all directories?
        ]
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "serving=serving.main:main",
        ],
    })
