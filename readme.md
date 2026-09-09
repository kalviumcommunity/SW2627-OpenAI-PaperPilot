# PaperPilot

### AI-Powered Academic Research & Citation Assistant

**Ask. Discover. Understand. Cite.**

PaperPilot is an AI-powered academic research assistant designed to help university students discover trusted library resources, understand research topics, and generate accurate citations.

---

## 📌 Project Overview

Academic research can be time-consuming because students often need to search across multiple library resources, identify relevant sources, understand research findings, and format citations manually.

PaperPilot aims to simplify this process by providing concise, citation-backed answers using trusted university library resources.

### Core Workflow


Research Question
       ↓
Search Academic Sources
       ↓
AI-Generated Summary
       ↓
Citation-Backed Evidence
       ↓
Investigate Sources
       ↓
Save / Cite / Export
```

---

## 🎯 Project Goals

* Make academic research easier and more efficient.
* Help students discover relevant university library resources.
* Provide concise answers supported by academic sources.
* Allow users to investigate the evidence behind an answer.
* Generate properly formatted citations.
* Maintain a clear connection between research claims and their sources.

---

## 👤 Target Users

**Primary Users:**
University students conducting academic research.

**Secondary Users:**
Researchers, faculty members, and university library users.

---

## ✨ Key Features

### 1. Research Assistant

Students can enter a research question using natural language.

### 2. Citation-Backed Answers

Scholara presents concise answers with supporting academic citations.

### 3. Source Explorer

Users can browse and filter relevant academic sources by factors such as year, subject, source type, and relevance.

### 4. Source Investigation

Users can inspect source metadata, relevance, available previews, and access the original resource through the university library.

### 5. Citation Workspace

Users can collect sources and generate citations in formats such as APA, MLA, and Chicago.

### 6. Saved Research

Users can save research sessions and useful academic sources for later use.

---

## 🖥️ UX Flow

Home
  ↓
Ask Research Question
  ↓
Search / Loading
  ↓
AI Research Results
  ↓
Investigate Source
  ↓
Save Source / Add Citation
  ↓
Citation Workspace
  ↓
Copy / Export Bibliography


---

## 🎨 UX Design

The UX follows a **summary-before-detail** approach.

Users first see a concise research answer and can then investigate the evidence supporting that answer.

The main design principles are:

* Clear primary action
* Minimal unnecessary navigation
* Evidence close to claims
* Progressive disclosure of source details
* Clear filters and recovery actions
* Explicit loading, empty, and error states
* Accessible and understandable interface labels

---

# 🔀 Git & GitHub Workflow

This project follows a feature-branch workflow instead of making changes directly to `main`.

### Branch Strategy

The `main` branch should remain stable and releasable.

New work should be completed on a dedicated feature branch.

### Branch Naming Convention

```text
feature/<feature-name>
fix/<bug-name>
docs/<documentation-name>
refactor/<change-name>
test/<test-name>
```

## 📝 GitHub Issues

Each significant piece of work should have a GitHub Issue.

An issue should contain:

* Clear action-oriented title
* Description and context
* Expected outcome
* Labels
* Assignee

### Example

```text
Title:
Implement PaperPilot research dashboard documentation

Labels:
feature, documentation

Assignee:
[Khushi]
```

---

## 🌿 Feature Branch Workflow

```bash
git checkout main
git pull origin main

git checkout -b feature/scholara-research-dashboard
```


---


## 🧑‍💻 Team Collaboration Rules

1. Do not push directly to `main`.
2. Create an issue before starting significant work.
3. Create a feature branch for each task.
4. Use meaningful conventional commit messages.
5. Push the feature branch to GitHub.
6. Create a pull request when the work is ready.
7. Link the relevant issue to the PR.
8. Request code review from a teammate.
9. Address review feedback before merging.
10. Merge only after approval.
11. Delete the feature branch after merging.

---

## 🚧 Current Status

**Project Stage:** UX / Product Planning

### Completed

* Problem definition
* Product Requirements Document (PRD)
* User stories
* UX workflow
* Mock UX wireframes
* Git/GitHub workflow planning

### Next Steps

* Convert wireframes into a high-fidelity Figma prototype.
* Define technical architecture.
* Implement the research interface.
* Connect academic library data sources.
* Implement citation generation.
* Add testing and validation.


## 📄 Documentation

Project documentation includes:

* Product Requirements Document (PRD)
* Mock UX / Wireframes
* User Flow
* Git/GitHub Collaboration Workflow

---

## 👥 Team

**Project:** PaperPilot
**Type:** Academic  Product Project
**Team:** KhushiNain, AnushkaBhatt
**Repository:** https://github.com/kalviumcommunity/SW2627-OpenAI-PaperPilot
---

