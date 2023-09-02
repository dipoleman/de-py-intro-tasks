# Python Foundations

This repo is split into three sections:

-   **`Syntax and Control Flow`** offers you the opportunity to get to grips with some of the basic syntax in Python. It will encourage you to predict behaviour, investigate control flow, and familiarise yourself with pythonic operators.

-   **`Katas`** will introduce function syntax. It will allow you to develop your problem solving techniques whilst researching tools available in Python. The tests are already written underneath the declaration. _We will look at a more formal approach to TDD in a later session._
    
    In order to run the tests you'll need to install `pytest`.

```sh
pip install pytest
```

To run the tests for each function run the following command:

```sh
pytest <file name>
```

-   **`Extension Tasks`** offer some more complicated problems for you to practise your newly formed python knowledge.

## Virtual Environment Reminder

Before working on this repo, remember you'll need to create a virtual environment. To do this run the command

```sh
python -m venv venv
```

which should create a `venv` directory at the root of your project. Run the _activate_ binaries using

```sh
source venv/bin/activate
```

Don't forget to deactivate your virtual environment afterwards with:

```sh
deactivate
```
