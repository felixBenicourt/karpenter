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

## Usage

Here’s a demonstration of Karpenter in action:

![Search Bar](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGZqejBrNzB4MzJzNDliMHgxamlncGZqbWEzcGd3ZGlqeXZwdmszdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IidIrvm14Q0lxrQQl2/giphy.webp)

![List cmd](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXFrNm1jb3F6ZTVxZ21naHhhZWNxeDA4bWgwNDAwanBsZGw5dHdvcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DXwzhMy0CttVJiVMuy/giphy.webp)

![execute cmd](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2c2MjdzcGl3bWVjc3Nmc2RzajFmdTQyMHdnOTl5bTNlY2VkdmcyMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/S69wwHgbo2vFtqYN1R/giphy.gif)

![check instances](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnV3MXJ5cDdtanA0dmcwdThzdWd1bWl3bTBjaGtlNjN2am42ZXkyZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TIRCGBZ67Ro0ktUJxI/giphy.webp)

![edit cmd](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXUwa3MzamNmbWY4czJjaDlnaDU0YjMxOHp5em8wd2VlenpmMmhweCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6AswTMjNWlqoguxHuw/giphy.webp)

![execute script](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDlkb2N2djh6enhkdGVhNHhjdDE4YjJtNGVpcDdpOHprdTc5NG56eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TWbd0cqiDUJbKX4zyT/giphy.webp)

### Launching the Tool

Run the main entry script:

```bash
rez env karpenter -- karpenter
