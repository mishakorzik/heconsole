import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='heconsole',  # should match the package folder
    packages=['heconsole'],  # should match the package folder
    version='1.0',  # important for updates
    license='MIT',  # should match your chosen license
    description='Perfect pip module to design and display your terminal, great customization',
    long_description=long_description,  # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='Misha Korzhik',
    author_email='developer.mishakorzhik@gmail.com',
    url='https://github.com/mishakorzik/heconsole',
    project_urls={  # Optional
        "Bug Tracker": "https://github.com/mishakorzik/heconsole/issues"
    },
    install_requires=['colorama'],  # list all packages that your package uses
    keywords=["color", "colors", "pypi", "customization", "console", "log", "color", "print", "debug", "warn", "info", "error", "pip"],  # descriptive meta-data
    classifiers=[  # https://pypi.org/classifiers
        'Development Status :: 1.0',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],

)
