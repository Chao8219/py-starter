# Welcome!

This project is a test project for better code structure and object orientated programming.

It may have some bugs in the middle of developing, but it could eventually become a complete and bugless project,
which means this could be a really simple project.

Also, this project is for designing the RPG game as well. So you may see some codes are about games.

The structure of this project follows [this](https://airbrake.io/blog/python/python-best-practices).

# Function of __init__.py

Quote from [here](https://docs.python.org/3/tutorial/modules.html#packages)

> The __init__.py files are required to make Python treat the directories as containing packages;
> this is done to prevent directories with a common name, such as string, from unintentionally
> hiding valid modules that occur later on the module search path. In the simplest case,
> __init__.py can just be an empty file, but it can also execute initialization code for
> the package or set the __all__ variable, described later.

Therefore, we can use an empty file as the __init__.py at each sub-directory.

# No More TK

The tkinter is simple to use, but not quite ideal since it seems not maintained any more.

# Virtual Environment

The virtual environment is useful when you are trying to install all the complex packages. When someone else wants to run your code and with the virtual environment, they do not need to install the packages all over again.

To setup a virtual environment: (in this case, we are using python3.x)

1. Open terminal, `python3 -m venv /path/py_starter/virtual_env_name/`, and the "path" is the absolute path to your project directory.

2. Wait for few seconds till done, then cd to your virtual environment sub directory.

3. Use `source bin/activate`, then you can install package in this environment.

4. Also, after use, you can simply `deactivate` it.

To install packages in this environment:

1. Make sure you have sourced it.

2. Double check your pip version `pip --version`, and python version `python --version`. Make sure you are using the one you want to use.

3. Use `pip install example_package`, remember do not add `sudo` which would install globally. 

4. After step 3, you should check the package with `pip list`. If the "example_package" shows up, congratulation! You made it!

More details could be found [here](https://stackoverflow.com/questions/21240653/how-to-install-a-package-inside-virtualenv).

# To-do List

[x] setup virtual environment
[ ] 