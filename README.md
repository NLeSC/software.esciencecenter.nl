# eStep website

[![Build Status](https://travis-ci.org/NLeSC/software.esciencecenter.nl.svg?branch=gh-pages)](https://travis-ci.org/NLeSC/software.esciencecenter.nl)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/30fa8eb9a38c44cf85dbfd353b7f4688)](https://www.codacy.com/app/NLeSC/software-esciencecenter-nl)

Data on projects, people and software in eStep

## Installation

Install the estep website utility by running
```
pip install -r requirements.txt
```

## How to edit

In the `_person/`, `_software/`, `_project/` and `_organizations/` directories, add a Markdown file with frontmatter (https://jekyllrb.com/docs/frontmatter/).

The frontmatter is in yaml format and must adhere to json schemas defined in the `schema/` directory.

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
