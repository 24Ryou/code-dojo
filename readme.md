## Repository Overview

This repository contains my solutions to the kata challenges on the Codewars website. I created an automatic system for myself so that whenever I want to solve a new kata, I can categorize my solutions based on the programming language used. I have an "app" folder with an initial file for solving each kata. For example, I have a Python file for solving katas in Python.

The "dist" folder contains subfolders categorized by the programming language used, such as "dist/python/slug-of-kata.py" for Python solutions. I wrote a system that allows me to add solutions in other programming languages and sort them accordingly. For this purpose, I have a database with tables for katas and programming languages. I store the information for each kata in the kata table and added a column for solutions. Whenever a kata is solved in a specific language, the solution is updated in this column.

The language table contains basic information about each programming language.

## Getting Started

To get started, clone the repository to your local machine.

```
git clone https://github.com/24Ryou/code-dojo.git
```

Once you have cloned the repository, you can install the dependencies by running the following command:

```
pip install -r requirements.txt
```

you can find how to run test dependencies of each programming-language on [codewars docs](https://docs.codewars.com/languages)
## Running the Code

To run the code, you can use the following command:

```
python .
```

This will start the automatic system that will categorize your solutions based on the programming language used.

## Planned update

I am planning to update my repository by adding a webpage that will allow users to search and review the content more easily. Additionally, I will share tips and insights that I learn from solving each kata.

## Contributing

If you would like to contribute to the repository, please fork the repository and submit a pull request.

## License

The repository is licensed under the MIT License.