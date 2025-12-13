# Gemini Project Context: Skill Box & Showcase

This document provides an overview of the "Skill Box" project, its structure, and key development workflows. The goal is to help the Gemini agent understand the project for future tasks.

## Project Overview

This repository is a comprehensive system for managing and showcasing a collection of AI "skills" for a large language model. The user's goal is to create compelling, non-technical demonstrations of these skills for a general audience.

The project consists of two main parts:

1.  **Skill Management System (Python):** A set of Python scripts located in the `/scripts` directory responsible for fetching skills from external GitHub repositories, processing their metadata, and aggregating them into a central `marketplace.json` file.
2.  **Skills Showcase (React Web App):** A modern web application located in `/awesome-skills-showcase` that displays the skills from the marketplace. It is built with Vite, React, TypeScript, and styled with Tailwind CSS.

## Key Components & Data Flow

The entire system is designed around a clear data pipeline:

1.  **Configuration (`config/external_skills_config.json`):** A master JSON file that defines the list of all skills to be included. Each entry contains a GitHub URL, local target folder, category, and description.

2.  **Fetching (`scripts/fetch_external_skills.py`):** This script reads the master config file and downloads the corresponding skill repositories or subfolders from GitHub into the correct directories (e.g., `/development`, `/data-analysis`). It requires a `GITHUB_TOKEN` environment variable.

3.  **Processing (`scripts/skill_processor.py` & `scripts/marketplace_updater.py`):**
    *   After fetching, scripts process the downloaded skill directories.
    *   They read the `SKILL.md` file within each skill's folder, which contains metadata in a YAML frontmatter block.
    *   The `marketplace_updater.py` script then combines this metadata with the information from the master config to generate a single, unified `/marketplace.json` file. This file acts as the central database for all skills.

4.  **Showcasing (`/awesome-skills-showcase`):**
    *   This React application serves as the frontend for the skills marketplace.
    *   Before running or building the app, a `sync` script (`scripts/sync-marketplace.js`) copies the root `marketplace.json` file into the app's `src` directory.
    *   The application then loads this local `marketplace.json` to render the list of skills, their categories, and descriptions.

---

## Building and Running

### 1. Skill Management (Python)

To update the skill database, you need to run the Python scripts.

**Prerequisites:**
*   Python 3
*   Install dependencies: `pip install -r requirements.txt`
*   Set the `GITHUB_TOKEN` environment variable to a valid GitHub personal access token.

**Workflow:**

```bash
# 1. Fetch skills from GitHub
python scripts/fetch_external_skills.py

# 2. Update the marketplace.json with the new skills
# (Assuming a main script orchestrates this, e.g., main.py or similar)
# Placeholder for the exact command to run the full update pipeline.
# TODO: Document the exact command to run the full marketplace update.
```

### 2. Skills Showcase (Web App)

To run the frontend showcase application.

**Prerequisites:**
*   Node.js and `pnpm`

**Workflow (from the `awesome-skills-showcase` directory):**

```bash
# Navigate to the web app directory
cd awesome-skills-showcase

# Install dependencies
pnpm install

# Run the development server (automatically syncs marketplace.json)
pnpm dev

# Build for production
pnpm build
```

---

## Development Conventions

*   **Adding a New Skill:**
    1.  Add a new entry to `config/external_skills_config.json`.
    2.  Run the Python fetching and processing scripts to download the skill and update `marketplace.json`.
    3.  Verify the skill appears correctly in the showcase web app.

*   **Skill Structure:** Each skill is a self-contained directory. The most important file is `SKILL.md`, which defines the skill's purpose and contains YAML frontmatter for its `name`, `description`, etc.

*   **Web App Components:** The showcase app is built with modern React patterns, utilizing components from `radix-ui` and `shadcn/ui` principles, and is styled with Tailwind CSS. New UI features should follow this convention.
