# eStep website

[![Build Status](https://travis-ci.org/eStep/eStep.github.io.svg?branch=master)](https://travis-ci.org/eStep/eStep.github.io)

Data on projects, people and software in eStep

## Installation

Install the converter by running
```
pip install -r requirements.txt
```

## How to edit

In the `person/`, `software/`, `project/` and `organizations/` directories, add a Markdown file with frontmatter, as in the python-frontmatter project.

After editing data, test the validity of the entered data with
```
estep validate
```

## Preview website

The website uses Jekyll powered Github pages.

To preview locally use docker:
```
docker run --rm --volume=$(pwd):/srv/jekyll -i -t  -p 127.0.0.1:80:80 jekyll/jekyll:pages
```
The website can be viewed on http://localhost:80

