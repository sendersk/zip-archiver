# 📦 Zip Archiver

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue)
![uv](https://img.shields.io/badge/package%20manager-uv-purple)
![Ruff](https://img.shields.io/badge/linter-Ruff-red)
![MyPy](https://img.shields.io/badge/type%20checking-MyPy-blue)
![Pytest](https://img.shields.io/badge/tests-Pytest-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Docker Compose](https://img.shields.io/badge/docker--compose-supported-2496ED)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063)
![PyYAML](https://img.shields.io/badge/PyYAML-configuration-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

**Production-ready CLI application for automatic yearly file archiving**

Version **v1.0.0**

Designed with Clean Architecture, strong typing, automated testing and Docker-first deployment.

</div>

---

# Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Goals](#project-goals)
- [Architecture](#architecture)
- [Application Flow](#application-flow)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Command Line Interface](#command-line-interface)
- [Examples](#examples)
- [Reports](#reports)
- [Structured Logging](#structured-logging)
- [Statistics Engine](#statistics-engine)
- [Docker](#docker)
- [Docker Compose](#docker-compose)
- [Testing](#testing)
- [Code Quality](#code-quality)
- [Development Workflow](#development-workflow)
- [Design Principles](#design-principles)
- [Roadmap](#roadmap)
- [Version History](#version-history)
- [Author](#author)
- [License](#license)

---

# Overview

Zip Archiver is a production-style command-line application that automatically archives files into yearly ZIP archives.

Instead of manually selecting files and creating archives, the application scans directories, determines the appropriate year for each file, groups them accordingly and creates compressed archives automatically.

The project has been intentionally designed as a **portfolio-quality software engineering project** rather than a simple scripting exercise.

The primary focus is on software engineering best practices including:

- modular architecture
- clean code
- testability
- type safety
- reproducibility
- observability
- containerization
- maintainability

The application demonstrates many concepts commonly used in production backend and DevOps environments.

---

# Features

## File Processing

- Scan directories
- Recursive scanning
- Year detection
- Multiple date sources
- Archive planning
- Automatic ZIP creation
- Safe file handling
- Optional deletion of archived files

---

## Configuration

- YAML configuration
- Strong validation using Pydantic
- Configurable archive behavior
- Future-proof configuration model

---

## Reporting

Automatically generates detailed JSON reports including:

- execution timestamp
- execution duration
- number of scanned directories
- number of scanned files
- archived files
- skipped files
- failed files
- archive statistics
- compression ratio
- disk space savings
- archive metadata
- configuration snapshot

---

## Logging

Production-style structured logging.

Supports:

- JSON logs
- console output
- log files
- Docker logs
- INFO level
- WARNING level
- ERROR level
- stack traces

---

## Quality Assurance

- Full type hints
- MyPy
- Ruff
- Pytest
- Strict validation
- Modular services

---

## Deployment

- Python 3.13+
- uv package manager
- Docker
- Docker Compose

---

# Project Goals

This project was created to demonstrate practical software engineering skills rather than implementing a complex compression algorithm.

Its objectives include:

- writing maintainable Python code
- designing loosely coupled modules
- building reusable services
- implementing configuration-driven behavior
- creating production-quality CLI applications
- applying Clean Architecture principles
- preparing software for containerized deployment

The resulting project closely resembles internal tooling commonly used by DevOps engineers, Platform Engineers and Site Reliability Engineers.

---

# Architecture

The application follows a layered architecture.

```text
                 CLI
                  │
                  ▼
           Configuration
                  │
                  ▼
             File Scanner
                  │
                  ▼
          Date Resolution
                  │
                  ▼
          Archive Planner
                  │
                  ▼
            ZIP Archiver
                  │
      ┌───────────┴───────────┐
      ▼                       ▼
 Statistics Engine      Structured Logger
      │                       │
      └───────────┬───────────┘
                  ▼
             JSON Reporter
```

Each module has a single responsibility.

Dependencies always point downward.

Business logic is separated from the CLI layer.

---

# Application Flow

The following diagram presents the complete execution pipeline.

```text
Start

 │

 ▼

Load configuration

 │

 ▼

Scan directory

 │

 ▼

Resolve file dates

 │

 ▼

Group files by year

 │

 ▼

Create archive plan

 │

 ▼

Generate ZIP archives

 │

 ▼

Collect statistics

 │

 ▼

Generate JSON report

 │

 ▼

Write structured logs

 │

 ▼

Finish
```

This pipeline makes the application predictable, deterministic and easy to test.

---

# Project Structure

```text
zip-archiver/
│
├── config/
│   └── settings.yaml
│
├── data/
│
├── logs/
│
├── reports/
│
├── src/
│   └── zip_archiver/
│       ├── __init__.py
│       ├── archiver.py
│       ├── config.py
│       ├── date_resolver.py
│       ├── logging_config.py
│       ├── main.py
│       ├── models.py
│       ├── planner.py
│       ├── reporter.py
│       ├── scanner.py
│       └── statistics.py
│
├── tests/
│
├── Dockerfile
├── docker-compose.yaml
├── .dockerignore
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# Module Responsibilities

| Module            | Responsibility               |
|-------------------|------------------------------|
| scanner.py        | Directory traversal          |
| date_resolver.py  | Resolve file year            |
| planner.py        | Build archive plans          |
| archiver.py       | Create ZIP archives          |
| statistics.py     | Calculate metrics            |
| reporter.py       | Generate JSON reports        |
| logging_config.py | Configure structured logging |
| config.py         | Load YAML configuration      |
| models.py         | Pydantic models              |

---

# Technology Stack

The project intentionally uses a modern Python ecosystem and tooling commonly found in production environments.

| Category         | Technology                      |
|------------------|---------------------------------|
| Language         | Python 3.13+                    |
| CLI              | Typer                           |
| Validation       | Pydantic v2                     |
| Configuration    | PyYAML                          |
| Package Manager  | uv                              |
| Testing          | Pytest                          |
| Static Analysis  | MyPy                            |
| Linting          | Ruff                            |
| Containerization | Docker                          |
| Orchestration    | Docker Compose                  |
| Logging          | Python logging (JSON Formatter) |
| Reports          | JSON                            |
| File Handling    | pathlib                         |
| Archive Format   | ZIP                             |

---

# Requirements

Before running the project, ensure the following tools are installed.

| Software | Version |
|-----------|---------|
| Python | 3.13 or newer |
| uv | latest |
| Git | latest |
| Docker *(optional)* | latest |
| Docker Compose *(optional)* | latest |

---

# Installation

## Clone the repository

```bash
git clone https://github.com/your-username/zip-archiver.git

cd zip-archiver
```

---

## Install dependencies

Using **uv**:

```bash
uv sync
```

This command:

- creates a virtual environment
- installs project dependencies
- installs development tools
- restores exact package versions from `uv.lock`

---

## Verify installation

```bash
uv run zip-archiver --help
```

Expected output:

```text
Usage: zip-archiver [OPTIONS] DIRECTORY

Options:

--dry-run
--recursive
--help
--version
```

---

# Configuration

The application behavior is fully driven by YAML configuration.

Configuration file:

```text
config/settings.yaml
```

Example configuration:

```yaml
recursive: true

date_source: modified

remove_originals: false

compression: ZIP_DEFLATED

output_directory: reports

log_directory: logs
```

---

## Configuration Options

| Option | Description |
|---------|-------------|
| recursive | Scan subdirectories |
| date_source | modified / created |
| remove_originals | Delete archived files |
| compression | ZIP compression algorithm |
| output_directory | JSON reports |
| log_directory | Structured logs |

---

# Command Line Interface

The application exposes a clean CLI based on **Typer**.

General syntax:

```bash
uv run zip-archiver [OPTIONS] DIRECTORY
```

---

## Help

```bash
uv run zip-archiver --help
```

Displays:

- available options
- arguments
- usage examples

---

## Version

```bash
uv run zip-archiver --version
```

Example:

```text
zip-archiver 1.0.0
```

---

## Archive Directory

Archive an entire directory.

```bash
uv run zip-archiver ./data
```

---

## Dry Run

Preview the execution without modifying any files.

```bash
uv run zip-archiver ./data --dry-run
```

No archives are created.

No files are deleted.

A complete report is still generated.

---

## Recursive Scan

```bash
uv run zip-archiver ./data --recursive
```

Scans:

```text
data/

data/photos/

data/documents/

data/backups/

...
```

---

## Remove Originals

```bash
uv run zip-archiver ./data --remove-originals
```

After successful archive creation:

```
ZIP created

↓

original files removed
```

This option should be used carefully.

---

# Example Workflow

Input directory:

```text
Documents/

invoice.pdf

holiday.jpg

notes.txt

archive/

meeting.docx

photo.png
```

Detected years:

```text
invoice.pdf

↓

2024

holiday.jpg

↓

2025

notes.txt

↓

2024

meeting.docx

↓

2023

photo.png

↓

2025
```

Generated archives:

```text
Documents/

Documents_2023.zip

Documents_2024.zip

Documents_2025.zip
```

---

# Example Output

Console output:

```text
INFO  Loading configuration

INFO  Scanning directory

INFO  Building archive plan

INFO  Creating ZIP archive

INFO  Generating report

INFO  Done
```

---

# Generated Report

Example:

```json
{
  "timestamp": "2026-07-31T09:20:15Z",

  "duration_ms": 185,

  "directories_scanned": 7,

  "files_scanned": 248,

  "archives_created": 3,

  "files_archived": 240,

  "files_skipped": 8,

  "files_failed": 0,

  "total_original_size": 95412642,

  "total_archive_size": 32561322,

  "saved_space": 62851320,

  "compression_ratio": 65.87,

  "archives": [
    {
      "year": 2023,
      "archive_name": "Documents_2023.zip",
      "files": 71,
      "original_size": 18456123,
      "archive_size": 6123412,
      "saved_space": 12332711,
      "compression_ratio": 66.82
    },
    {
      "year": 2024,
      "archive_name": "Documents_2024.zip",
      "files": 83,
      "original_size": 35214581,
      "archive_size": 12236780,
      "saved_space": 22977801,
      "compression_ratio": 65.25
    },
    {
      "year": 2025,
      "archive_name": "Documents_2025.zip",
      "files": 86,
      "original_size": 41741938,
      "archive_size": 14101130,
      "saved_space": 27640808,
      "compression_ratio": 66.22
    }
  ],

  "configuration": {
    "recursive": true,
    "date_source": "modified",
    "remove_originals": false,
    "compression": "ZIP_DEFLATED"
  }
}
```

---

# Structured Logging

The application uses structured JSON logging.

Benefits:

- machine readable
- searchable
- Docker compatible
- CI/CD friendly
- production ready

---

## Example Log

```json
{
  "timestamp":"2026-07-31T09:15:20Z",
  "level":"INFO",
  "logger":"zip_archiver",
  "message":"Archive process started"
}
```

---

```json
{
  "timestamp":"2026-07-31T09:15:21Z",
  "level":"INFO",
  "logger":"zip_archiver",
  "message":"Scanning directory"
}
```

---

```json
{
  "timestamp":"2026-07-31T09:15:23Z",
  "level":"INFO",
  "logger":"zip_archiver",
  "message":"Archive created"
}
```

---

```json
{
  "timestamp":"2026-07-31T09:15:24Z",
  "level":"INFO",
  "logger":"zip_archiver",
  "message":"Report generated"
}
```

---

Log files are written to:

```text
logs/app.log
```

while the same messages are simultaneously emitted to the console, making them immediately visible via Docker logs.

---

# Statistics Engine

One of the core components of the application is the statistics engine.

After every execution, the engine collects runtime information and generates a detailed execution summary.

The following metrics are calculated automatically:

| Metric | Description |
|----------|-------------|
| `timestamp` | Execution date and time (UTC) |
| `duration_ms` | Total execution time |
| `directories_scanned` | Number of scanned directories |
| `files_scanned` | Number of processed files |
| `archives_created` | Number of generated ZIP archives |
| `files_archived` | Total archived files |
| `files_skipped` | Files intentionally skipped |
| `files_failed` | Files that could not be archived |
| `total_original_size` | Total size before compression |
| `total_archive_size` | Total ZIP size |
| `saved_space` | Saved disk space |
| `compression_ratio` | Compression efficiency |
| `configuration` | Configuration snapshot |
| `archives` | Per-archive statistics |

The statistics engine is isolated from the archiving logic, making it independently testable and reusable.

---

# Docker

The project is fully containerized.

## Build image

```bash
docker build -t zip-archiver .
```

---

## Run container

Linux / macOS

```bash
docker run --rm \
-v $(pwd)/data:/data \
zip-archiver \
/data
```

Windows PowerShell

```powershell
docker run --rm `
-v ${PWD}/data:/data `
zip-archiver `
/data
```

---

## Container Features

- Lightweight Python 3.13 image
- uv dependency management
- Production-ready execution
- JSON logging
- Read-only application code
- Mounted data directory
- Mounted logs directory
- Mounted reports directory

---

# Docker Compose

The project includes Docker Compose support.

Run:

```bash
docker compose up
```

Example configuration:

```yaml
services:

  zip-archiver:

    build: .

    container_name: zip-archiver

    volumes:

      - ./data:/data

      - ./logs:/app/logs

      - ./reports:/app/reports

    command:

      - /data
```

Benefits:

- One-command startup
- Persistent reports
- Persistent logs
- Easy local development
- Reproducible environment

---

# Testing

The project contains a comprehensive automated test suite.

Run all tests:

```bash
uv run pytest
```

Run with coverage:

```bash
uv run pytest --cov=src
```

Verbose mode:

```bash
uv run pytest -v
```

---

## Test Coverage

The project contains unit tests for:

- scanner
- planner
- date resolver
- reporter
- statistics
- archiver
- configuration
- CLI

Every module is tested independently.

---

# Static Analysis

## Ruff

Run linter:

```bash
uv run ruff check .
```

Auto-fix:

```bash
uv run ruff check . --fix
```

---

## MyPy

Static type checking:

```bash
uv run mypy src
```

The project is written using strict type hints.

---

# Development Workflow

Recommended workflow for contributors:

```text
Create feature branch

↓

Implement feature

↓

Run Ruff

↓

Run MyPy

↓

Run Pytest

↓

Commit changes

↓

Push branch

↓

Create Pull Request
```

---

# Design Principles

The application follows several software engineering principles.

## Single Responsibility Principle

Each module has exactly one responsibility.

Examples:

- scanner.py scans directories
- planner.py groups files
- archiver.py creates ZIP archives
- reporter.py generates reports

---

## Separation of Concerns

Responsibilities are clearly separated.

CLI never contains business logic.

Business logic never depends on user interaction.

Reporting is independent from archiving.

Logging is independent from reporting.

---

## Dependency Direction

Dependencies always point inward.

```text
CLI

↓

Services

↓

Models

↓

Utilities
```

This minimizes coupling.

---

## Pathlib First

The project intentionally avoids `os.path`.

All file system operations use:

```python
from pathlib import Path
```

This improves readability and cross-platform compatibility.

---

## Type Safety

Every public function includes explicit type hints.

Example:

```python
def create_archive(
    files: list[Path],
) -> Path:
```

Strict typing is enforced using MyPy.

---

## Configuration Driven

Application behavior is defined by configuration rather than hardcoded values.

This allows future extensions without modifying the business logic.

---

# Performance

The application is optimized for typical filesystem workloads.

Characteristics:

- Low memory usage
- Lazy directory traversal
- Efficient grouping
- Streaming ZIP creation
- Minimal temporary allocations

---

# Error Handling

The application handles common failure scenarios gracefully.

Examples:

- missing directories
- permission errors
- invalid configuration
- corrupted files
- ZIP creation failures

Errors are:

- logged
- reported
- counted in execution statistics

---

# Future Improvements

Possible future enhancements include:

- Watch mode
- Incremental archives
- Parallel compression
- Multiple compression algorithms
- TAR/GZIP support
- Encryption
- Password-protected archives
- Progress bar
- Resume interrupted jobs
- Configuration profiles
- Archive verification
- Cloud storage support (AWS S3, Azure Blob, Google Cloud Storage)
- Scheduled execution
- GUI application
- REST API
- Web dashboard

---

# Roadmap

## Version 1.0

- [x] CLI
- [x] Directory scanning
- [x] Recursive mode
- [x] Archive planner
- [x] ZIP creation
- [x] JSON reporting
- [x] Statistics engine
- [x] Structured logging
- [x] Docker support
- [x] Docker Compose
- [x] Unit tests
- [x] Ruff
- [x] MyPy

---

## Version 1.1

- [ ] Progress bar
- [ ] Parallel archiving
- [ ] Archive verification

---

## Version 2.0

- [ ] Cloud storage
- [ ] REST API
- [ ] Web dashboard
- [ ] Incremental archiving
- [ ] Scheduler

---

# Version History

## v1.0.0

Initial stable release.

Features:

- Production-ready CLI
- ZIP archiving
- YAML configuration
- JSON reports
- Structured logging
- Docker support
- Automated testing
- Clean architecture

---

# Contributing

Contributions are welcome.

Recommended development process:

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Run Ruff.
5. Run MyPy.
6. Run Pytest.
7. Submit a Pull Request.

---

# Author

**Przemysław Senderski**

Application Support Engineer transitioning toward Platform Engineering / Site Reliability Engineering.

This project is part of a portfolio focused on:

- Python
- Automation
- DevOps
- Clean Architecture
- Backend Engineering
- Production-ready CLI applications

---

# License

This project is licensed under the MIT License.

---

<div align="center">

## ⭐ If you found this project useful, consider giving it a star.

**Zip Archiver**

**Version 1.0.0**

Built with ❤️ using Python 3.13

</div>