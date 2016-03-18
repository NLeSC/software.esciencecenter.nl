# eStep website

[![Build Status](https://travis-ci.org/eStep/eStep.github.io.svg?branch=master)](https://travis-ci.org/eStep/eStep.github.io)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/cbf6d30b4b004e219f14bb6f7b10943e)](https://www.codacy.com/app/NLeSC/eStephub-io)

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

