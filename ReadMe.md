<p align="center">
  <a href="https://gitea.io/">
    <img alt="Gitea" src="https://raw.githubusercontent.com/go-gitea/gitea/main/public/img/gitea.svg" width="220"/>
  </a>
</p>
<h1 align="center">Gitea - Git with a cup of tea</h1>

<p align="center">
  <a href="https://drone.gitea.io/go-gitea/gitea" title="Build Status">
    <img src="https://drone.gitea.io/api/badges/go-gitea/gitea/status.svg?ref=refs/heads/main">
  </a>
  <a href="https://discord.gg/Gitea" title="Join the Discord chat at https://discord.gg/Gitea">
    <img src="https://img.shields.io/discord/322538954119184384.svg">
  </a>
  <a href="https://app.codecov.io/gh/go-gitea/gitea" title="Codecov">
    <img src="https://codecov.io/gh/go-gitea/gitea/branch/main/graph/badge.svg">
  </a>
  <a href="https://goreportcard.com/report/code.gitea.io/gitea" title="Go Report Card">
    <img src="https://goreportcard.com/badge/code.gitea.io/gitea">
  </a>
  <a href="https://pkg.go.dev/code.gitea.io/gitea" title="GoDoc">
    <img src="https://pkg.go.dev/badge/code.gitea.io/gitea?status.svg">
  </a>
  <a href="https://github.com/go-gitea/gitea/releases/latest" title="GitHub release">
    <img src="https://img.shields.io/github/release/go-gitea/gitea.svg">
  </a>
  <a href="https://www.codetriage.com/go-gitea/gitea" title="Help Contribute to Open Source">
    <img src="https://www.codetriage.com/go-gitea/gitea/badges/users.svg">
  </a>
  <a href="https://opencollective.com/gitea" title="Become a backer/sponsor of gitea">
    <img src="https://opencollective.com/gitea/tiers/backers/badge.svg?label=backers&color=brightgreen">
  </a>
  <a href="https://opensource.org/licenses/MIT" title="License: MIT">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg">
  </a>
  <a href="https://gitpod.io/#https://github.com/go-gitea/gitea">
  <img
    src="https://img.shields.io/badge/Contribute%20with-Gitpod-908a85?logo=gitpod"
    alt="Contribute with Gitpod"
  />
  </a>
  <a href="https://crowdin.com/project/gitea" title="Crowdin">
    <img src="https://badges.crowdin.net/gitea/localized.svg">
  </a>
  <a href="https://www.tickgit.com/browse?repo=github.com/go-gitea/gitea&branch=main" title="TODOs">
    <img src="https://badgen.net/https/api.tickgit.com/badgen/github.com/go-gitea/gitea/main">
  </a>
  <a href="https://app.bountysource.com/teams/gitea" title="Bountysource">
    <img src="https://img.shields.io/bountysource/team/gitea/activity">
  </a>
</p>

<p align="center">
  <a href="README_ZH.md">View this document in Chinese</a>
</p>


# Rebase
## merge features; rebase off of master
### generally, rebase/squash before you merge, unless dev⇨rel
# Bisect
## Binary search for faulty commits
# Log (--graph) (--format)
## manages a verbose commit history for you
## show <commit> -- <file>
# Blame
## blame is hori; log is vert
# Submodules
# Unrelated Histories/Orphan
## Win/Mac⇨Dev; Dev⇨QA⇨Rel; Snap/Sys/Dock⇨Dev
# Etc
## push/pull from a fileshare
## git reset --hard HEAD^
## git revert <commit>
## git stash/pop
## git cherry-pick <commit>
## git checkout master && git checkout <branch> -- <file>
## pull only the gitignore
### 	git init && git remote add gitignore https://github.com/github/gitignore && git fetch && git check origin/master -m VisualStudio.gitignore
## how to create a private fork of a github repo
### https://gist.github.com/0xjac/85097472043b697ab57ba1b1c7530274
## how to create a mirror proper
### https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository
### would be a great way to mention gitea
# How to keep track of this?
## git alias
## wt command palette
## ahk
# Stuff to work in implicitly
## git difftool
## git mergetool
# Things I won't cover
## Jenkins
## GitPython
## GitLab
## What's in the .git folder?
## Why doesn't my former employer use git?
## Why is Bamboo broken?