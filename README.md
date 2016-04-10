# eStep software website

[![Build Status](https://travis-ci.org/NLeSC/software.esciencecenter.nl.svg?branch=gh-pages)](https://travis-ci.org/NLeSC/software.esciencecenter.nl)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/30fa8eb9a38c44cf85dbfd353b7f4688)](https://www.codacy.com/app/NLeSC/software-esciencecenter-nl)

Data on projects, people and software in eStep.

## Installation

Requirements:

* libyaml, C library and development headers

Install the estep website utility by running
```
pip install -e .
```

## How to edit

1. Clone this repo
2. Create a branch for your additions with the gh-pages branch as a starting point.

3. In `_software` directory, add a Markdown file with front matter (https://jekyllrb.com/docs/frontmatter/) for your software.

  * The front matter is in yaml format and must adhere to json schemas defined in the `schema/` directory.
  * Use the existing Markdown files as examples.
  * The filename should be lowercase, end with `.md` and contain no url-unfriendly characters (e.g. space, /).
  * Also create/update the related pages in the the `_person/`, `_software/`, `_project/` and `_organization/` directories, e.g. some software is used in a project then write a Markdown file in both the `_software` and `_project` directories. If someone else is responsible for the data in related pages, place a stub there with at least the correct `name`. If it concerns a person, also fill in `affiliation`.
  * Many relations are reciprocal, be sure to fill them in for both related objects. For example, when updating software's `user` property, also update that users' `userOf` property. Other examples of reciprocal relations: `organization#involvedIn` vs `project#involvedOrganization`, `software#user` vs `organization#uses`, `software#engineer` vs `person#engineerOf`.
  * Use `http://` prefixes for all internal URLs, currently HTTPS is not properly supported.

4. After editing data, test the validity of the entered data with
```
estep validate -v
```
5. Commit and push changes.
6. Create a pull request to merge your changes into the gh-pages branch.

## Preview website

The website uses Jekyll powered Github pages.

To preview locally use docker:
```
docker run --rm --volume=$(pwd):/srv/jekyll -i -t  -p 127.0.0.1:80:80 jekyll/jekyll:pages
```
The website can be viewed on http://localhost:80

The docker container will fail when there is a virtualenv in the currend working directory.
Resolve by putting virtualenv somewhere else or prefixing it with '.'.
