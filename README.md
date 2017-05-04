# eStep software website

[![Build Status](https://travis-ci.org/NLeSC/software.esciencecenter.nl.svg?branch=gh-pages)](https://travis-ci.org/NLeSC/software.esciencecenter.nl)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/30fa8eb9a38c44cf85dbfd353b7f4688)](https://www.codacy.com/app/NLeSC/software-esciencecenter-nl)

Data on software, projects, people, organizations, publications and reports in eStep.

## tl;dr

1. Create/update Markdown file(s) in `_software/`, `_person/`, `_project/`, `_publication/`, `_report/` and `_organization/` directories.
2. Commit & push changes
3. Create a Pull Request

## Installation

Install the estep website utility by running

```shell
pyvenv .env3
. .env3/bin/activate
pip install -U pip wheel
pip install -r requirements.txt -e .
```

## How to edit

1. Clone this repo
2. Create a branch for your additions with the gh-pages branch as a starting point.

3. In `_software` directory, add a Markdown file with front matter (https://jekyllrb.com/docs/frontmatter/) for your software.

  * The front matter is in yaml format and must adhere to json schemas defined in the `schema/` directory.
  * Use the existing Markdown files as examples.
  * The filename should be lowercase, end with `.md` and contain no url-unfriendly characters (e.g. space, /).
  * Also create/update the related pages in the the `_software/`, `_person/`, `_project/`, `_publication/`, `_report/` and `_organization/` directories, e.g. some software is used in a project then write a Markdown file in both the `_software` and `_project` directories. If someone else is responsible for the data in related pages, place a stub there with at least the correct `name`. If it concerns a person, also fill in `affiliation`.
  * Many relations are reciprocal, be sure to fill them in for both related objects. For example, when updating software's `user` property, also update that users' `userOf` property. Other examples of reciprocal relations: `organization#involvedIn` vs `project#involvedOrganization`, `software#user` vs `organization#uses`, `software#engineer` vs `person#engineerOf`.
  * For URLs within the site, `http://software.esciencecenter.nl` can be omitted. HTTPS is not supported on this site.

4. Many relations are reciprocal, be sure to fill them in for both related objects. For example, when updating software's `user` property, also update that users' `userOf` property. Other examples of reciprocal relations: `organization#involvedIn` vs `project#involvedOrganization`, `software#user` vs `organization#uses`, `software#engineer` vs `person#engineerOf`. Automatically fill them in with
```
estep generate reciprocal
```
5. Download remote logos (if any) with
```
estep generate logo
```
6. After editing data, test the validity of the entered data with
```
estep validate -v
```
7. Commit and push changes.
8. Create a pull request to merge your changes into the gh-pages branch.

### Generate publication

Publications are stored in the `_publication/` directory.
A publication Markdown file can be generated with it's [DOI](http://www.doi.org/) by running:
```
estep generate publication http://dx.doi.org/10.1002/cpe.3416
```

A publication can be linked to a project by using the `--project=<project_url>` argument.

## Preview website

The website uses Jekyll powered Github pages.

To preview locally use docker:
```
docker run --rm --volume=$(pwd):/srv/jekyll -i -t  -p 127.0.0.1:4000:4000 jekyll/jekyll:pages jekyll serve
```
The website can be viewed on http://localhost:4000

The docker container will fail when there is a virtualenv in the current working directory.
Resolve by putting virtualenv somewhere else or prefixing it with '.'.

To preview without Docker:
1. Install Ruby using your favourite option from https://www.ruby-lang.org/
2. Use gem package manager to install jekyll and github-pages, make sure to use same versions as https://pages.github.com/versions/
```
gem install jekyll
gem install github-pages
```
3. Run the jekyll page generator and webserver
```
jekyll serve -w
```
4. steer your browser to http://localhost:4000 (or wherever jekyll serve reported it's port to be in the previous step)
