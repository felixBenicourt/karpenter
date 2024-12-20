# Karpenter Tool Box

Karpenter is a versatile tool designed to manage and execute scripts across multiple DCC (Digital Content Creation) applications like Maya, Houdini, Unreal, and Blender. It features an intuitive UI built with PyQt and supports configuration management, instance detection, and dynamic script execution.


## Table of Contents

- [Features](#Features)
- [Installation](#snstallation)
- [Usage](#Usage)
- [License](#License)


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

## Usage

### Launching the Tool

Run the main entry script:

```bash
rez env karpenter -- karpenter
```

### Demonstration of Karpenter in Action

#### Search Bar
![Search Bar](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGZqejBrNzB4MzJzNDliMHgxamlncGZqbWEzcGd3ZGlqeXZwdmszdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IidIrvm14Q0lxrQQl2/giphy.webp)

You can use the search bar to quickly find the command you want to execute.

---

#### List Commands
![List Commands](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXFrNm1jb3F6ZTVxZ21naHhhZWNxeDA4bWgwNDAwanBsZGw5dHdvcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DXwzhMy0CttVJiVMuy/giphy.webp)

Click on the gear icon to open the **Edit Commands** window. This window displays all the custom commands you've created.  
- Select a command to edit it.
- Create a new command using the `+` button.
- Delete a selected command using the `-` button.
- Save all changes by clicking the disk icon.

---

#### Execute Commands
![Execute Commands](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2c2MjdzcGl3bWVjc3Nmc2RzajFmdTQyMHdnOTl5bTNlY2VkdmcyMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/S69wwHgbo2vFtqYN1R/giphy.gif)

Click on a command's execution icon to run it.  
In this example, we execute a Rez command:  
```bash
rez env k_maya -- maya
```

---

#### Edit Commands
![edit cmd](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXUwa3MzamNmbWY4czJjaDlnaDU0YjMxOHp5em8wd2VlenpmMmhweCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6AswTMjNWlqoguxHuw/giphy.webp)

You can edit your commands.

- Title : the displayed title in the searchbar.
- Type : python or rez you can choose if you want to execute this as a OS command or a python script through the socket server.
- Tags : the tags help you to filter the commands by tags.
- Code : your code or command.

#### Execute Script

![find_instances](https://i.imgur.com/9T0CgbU.png)

You can find the instance of the opened DCC (Maya, houdini, Unreal) and you can select the instances you need. 

![execute script](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExam56ZmZjN3VvZ3g3ZGUwaWpxeWozMGN2bHR6NDg4Zmd1MzVsMHl5MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/k5NAceIsLmXWk9caCl/giphy.gif)

Here a demo of the python script executed on the selected DCC instances.
```python
import maya.cmds as cmds

cmds.polyCube(n="imhere")
```

## License
```text
Custom License Agreement

Copyright (c) 2024 Felix Benicourt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to use,
study, and modify the Software for personal, educational, or internal purposes,
subject to the following conditions:

1. Redistribution and Resale:
   - Redistribution, sublicensing, or resale of the Software, in whole or in part, 
     is strictly prohibited without prior written consent from the author.

2. Attribution:
   - This copyright notice and permission notice shall be included in all copies 
     or substantial portions of the Software.

3. No Warranty:
   - THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
     IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
     FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL 
     THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER 
     LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING 
     FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
     IN THE SOFTWARE.

```





