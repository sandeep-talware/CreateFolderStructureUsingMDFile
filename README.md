# Markdown Project Structure Scaffold

A lightweight Python utility to **automatically generate a project folder structure from a Markdown tree specification**.

This tool is useful when project structures are documented in `.md` files (for architecture docs, design specs, or repository templates) and you want to **quickly scaffold the entire directory and file layout without manually creating each folder or file**.

---

## Problem This Tool Solves

When designing projects, developers often document the intended repository structure using a **tree-style format** like this:

```
project-name/
├── README.md
├── docker-compose.yml
├── ml-engine/
│   ├── requirements.txt
│   ├── config/
│   │   ├── pipeline_config.yaml
│   │   └── model_config.yaml
│   └── data/
```

Manually recreating such structures can be:

* Time-consuming
* Error-prone
* Repetitive when starting multiple projects

This utility reads the structure directly from the Markdown file and **generates the entire directory and file hierarchy automatically**.

---

## Features

* Parses **tree-style Markdown structures**
* Automatically creates **nested directories**
* Creates **empty files**
* Adds `.gitkeep` to empty directories
* Supports **dry-run preview**
* Works with **multiple root directories**
* Can generate the structure in the **same directory as the Markdown file or a custom output directory**

---

## Requirements

* Python 3.7+

No additional dependencies are required.

---

## Installation

Clone or copy the script into your repository.

Example structure:

```
repo/
├── CreateProjStructureFromMD.py
└── structure.md
```

Make the script executable (optional but recommended):

```
chmod +x CreateProjStructureFromMD.py
```

---

## Usage

### 1. Preview the Structure (Dry Run)

Before creating files and directories, you can preview what will be generated.

```
python CreateProjStructureFromMD.py structure.md --dry-run
```

Example output:

```
[DIR ] project-name
[FILE] project-name/README.md
[FILE] project-name/docker-compose.yml
[DIR ] project-name/ml-engine
[FILE] project-name/ml-engine/requirements.txt
```

---

### 2. Generate the Project Structure

```
python CreateProjStructureFromMD.py structure.md
```

The structure will be created **in the same directory where the Markdown file is located**.

---

### 3. Generate Structure in a Specific Directory

```
python CreateProjStructureFromMD.py structure.md --output ./projects
```

This will create the project structure inside the `projects` directory.

---

## Markdown Format

The script expects a **tree-style structure**, similar to output from the `tree` command.

Example:

```
project-name/
├── README.md
├── src/
│   ├── main.py
│   └── utils/
│       └── helper.py
├── tests/
│   └── test_main.py
└── requirements.txt
```

Guidelines:

* Directories should end with `/`
* Files should include their extension
* Indentation should follow the standard `tree` format

---

## Example

### Input (`structure.md`)

```
project-name/
├── README.md
├── docker-compose.yml
├── ml-engine/
│   ├── requirements.txt
│   ├── config/
│   │   ├── pipeline_config.yaml
│   │   └── model_config.yaml
│   └── data/
```

### Generated Output

```
project-name/
├── README.md
├── docker-compose.yml
├── ml-engine/
│   ├── requirements.txt
│   ├── config/
│   │   ├── pipeline_config.yaml
│   │   └── model_config.yaml
│   └── data/
│       └── .gitkeep
```

---

## Optional: Install as a Global CLI Tool

To make the tool available globally:

1. Move the script to a directory in your PATH (example: `~/bin`)

```
mkdir -p ~/bin
mv CreateProjStructureFromMD.py ~/bin/CreateProjStructureFromMD
chmod +x ~/bin/CreateProjStructureFromMD
```

2. Add the following shebang at the top of the script if not present:

```
#!/usr/bin/env python3
```

You can now run the tool from anywhere:

```
CreateProjStructureFromMD structure.md
```

---

## Use Cases

* Quickly scaffold **new repositories**
* Convert **architecture documentation into real project structures**
* Generate **starter templates for teams**
* Bootstrap **microservice or ML project layouts**
* Maintain **consistent folder structures across multiple projects**

---

## Contributing

Contributions and improvements are welcome.
Feel free to submit issues or pull requests to improve parsing, add features, or enhance usability.

---

## License

Open License.
