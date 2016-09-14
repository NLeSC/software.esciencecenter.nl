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

1. Clone this repo, ``git clone https://github.com/NLeSC/software.esciencecenter.nl.git``
2. ``cd software.esciencecenter.nl``
3. Create a branch for your additions with the gh-pages branch as a starting point (``git branch mybranch`` followed by ``git checkout mybranch``).
4. Let's say you want to add an item about some software.
  * Copy `schema/software-template.md` to the `_software` directory, rename it according to the name of your software. The filename should be lowercase, end with `.md` and contain no url-unfriendly characters (e.g. space, /).
  * Edit the file's '[front matter](https://jekyllrb.com/docs/frontmatter/)', i.e. the block between the triple minuses.
    * The front matter is in YAML format and must adhere to predefined JSON schemas. Refer to the `schema/` directory to see the expected type of input for each property.
    * Use (copies of) the templates from the `schema` directory as a starting point for editing; also look at existing Markdown files for example usage, e.g those from the `_software` or `_project` directories.    
    * For URLs within the site, `http://software.esciencecenter.nl` can be omitted, so you should write ``/person/s.verhoeven`` instead of ``http://software.esciencecenter.nl/person/s.verhoeven``. Also note that HTTPS is not supported on this site.
5. Every time you edit data, test the validity of the entered data again with ``estep validate -v``. At this stage you can ignore any errors relating to relations not being reciprocal, for example errors like these:
```
* Error      : '/software/differential-evolution' is not a 'uri'
  Cause      : /software/differential-evolution not found locally as _software/differential-evolution.md
  On property: userOf.items.format
```
6. Let the estep tool make local copies of remote logos (if you have any) with ``estep generate logo``
7. Some relations are reciprocal, e.g.
  - `organization#involvedIn` vs `project#involvedOrganization`
  - `software#user` vs `organization#uses`
  - `software#engineer` vs `person#engineerOf`.
  Reciprocal relations can be filled in automatically by the ``estep`` tool (provided that the required files already exist). Create the related pages in the `_software/`, `_person/`, `_project/`, `_publication/`, `_report/` and `_organization/` directories as necessary, then run ``estep generate reciprocal`` to automatically write content to those files.
8. Test the validity of the entered data again with ``estep validate -v``. At this stage, it needs to pass without any errors.
9. ``git add file1 file2 fileN`` your changes, ``git commit -m 'commit message'``, then ``git push origin mybranch``.
10. On GitHub create a pull request to ask the repository's Administrators to merge your changes into the gh-pages branch.


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
docker run --rm --volume=$(pwd):/srv/jekyll -i -t  -p 127.0.0.1:4000:4000 jekyll/jekyll:pages
```
The website can be viewed on http://localhost:4000

The docker container will fail when there is a virtualenv in the current working directory.
Resolve by putting virtualenv somewhere else or prefixing it with '.'.

To preview without Docker:
1. Install Ruby using your favourite option from https://www.ruby-lang.org/
2. Use gem package manager to install jekyll and github-pages
```
gem install jekyll
gem install github-pages
```
3. Run the jekyll page generator and webserver
```
jekyll serve -w
```
4. steer your browser to http://localhost:4000 (or wherever jekyll serve reported it's port to be in the previous step)
