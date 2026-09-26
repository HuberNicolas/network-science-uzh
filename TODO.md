# TODO

Open tasks before the repository is made public. See also [Known issues](README.md#known-issues).

## 1. Clean-up

- [x] Tag the submitted state as `v1.0.0` (commit "Merged", 22 December 2023)
- [x] Remove the assignment sheets of the course team from the current state (they stay in old commits)
- [x] Remove the duplicate hand-in copies and the partial result PDFs
- [x] Keep one shared copy of the assignment 3 data
- [x] Delete the remote branch `summary`: it only holds lecture exercises, official solutions and data of the course
  (backup: `_archive/network-science-before-filter-repo.bundle`)
- [x] Keep the branches `task1`, `task2`, `task3`, `a4t2` and `correction`: they show how the work was done

## 2. Environment

- [x] Add `pyproject.toml` and `uv.lock` with Python 3.10 and the library versions of December 2023
- [x] Declare `numba`, which NEMtropy needs but does not declare
- [ ] Run the long notebooks (assignments 1–3) once in a copy to confirm they still finish

## 3. Documentation

- [x] Rewrite the README (contents per assignment, data, known issues, authors)
- [ ] Add the name of the lecturer to the README
- [ ] Add original sources and licenses of the datasets, if they can be found

## 4. Before publishing

- [x] Choose and add a license (MIT, both authors)
- [x] Add the project context (course, institution, semester) to the README
- [x] Get the consent of Raphael Wäspi
- [x] Rename the GitHub repository to `network-science-uzh`, then `git remote set-url origin git@github.com:HuberNicolas/network-science-uzh.git`
- [ ] Rewrite the old commit e-mail addresses with a mailmap (dates and content stay the same)
- [x] Push `main` and the tag `v1.0.0`, create the release "As submitted"
- [ ] Tag the cleaned-up state as `v1.1.0`
- [ ] Check for secrets in the files and the git history, right before publishing
