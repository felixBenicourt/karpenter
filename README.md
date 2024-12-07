# Karpenter Tool

Karpenter is a versatile tool designed to manage and execute scripts across multiple DCC (Digital Content Creation) applications like Maya, Houdini, Unreal, and Blender. It features an intuitive UI built with PyQt and supports configuration management, instance detection, and dynamic script execution.

## Features

- **Toolbox UI**: Search, filter, and execute scripts with ease.
- **Instance Detection**: Automatically detects running instances of Maya, Houdini, Unreal, and Blender.
- **Script Management**:
  - Add, edit, or delete script configurations.
  - Execute scripts in specific DCC instances.
- **Dynamic Styles**: Supports custom QSS stylesheets for UI customization.

## Installation

### Requirements

- Python 3.x
- Required modules:
  - PyQt5 or compatible library (qtpy for abstraction)
  - rez for environment management
  - JSON handling (`json` module)
  - Networking (`socket` module)

### Steps

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd karpenter
    ```

2. Install dependencies:

    ```bash
    pip install PyQt5 qtpy
    ```

3. (Optional) Set up a Rez environment:

    ```bash
    rez env karpenter -- karpenter
    ```

!([(https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGZqejBrNzB4MzJzNDliMHgxamlncGZqbWEzcGd3ZGlqeXZwdmszdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IidIrvm14Q0lxrQQl2/giphy.webp)](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGZqejBrNzB4MzJzNDliMHgxamlncGZqbWEzcGd3ZGlqeXZwdmszdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IidIrvm14Q0lxrQQl2/giphy.webp))


## Usage

### Launching the Tool

Run the main entry script:

```bash
python karpenter.py
