# Payload Generator Tool

## Overview
The Payload Generator Tool is a Python-based command-line interface (CLI) application designed to generate various types of payloads for security testing purposes. It supports generating SQL Injection, XSS (Cross-Site Scripting), and Command Injection payloads, as well as custom payloads provided by the user. The tool also offers functionality to save and load custom payloads to and from files.

## Features
- Generate SQL Injection payloads
- Generate XSS payloads
- Generate Command Injection payloads
- Generate custom payloads
- View history of generated payloads
- Save custom payloads to a file
- Load custom payloads from a file
- Interactive menu interface
- Command-line arguments support for generating payloads

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/incogneto1337/Payload-Generator.git
   cd Payload-Generator
   ```
2. Install any required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage
You can run the Payload Generator Tool either interactively through its menu or directly via command-line arguments.

### Interactive Menu
To start the tool with the interactive menu, run:
```bash
python payloadgen.py
```
You will see a menu with options to generate different types of payloads, view history, save or load custom payloads, and exit the tool.

### Command-Line Arguments
You can also generate payloads directly using command-line arguments. The available arguments are:
- `--sql`: Generate an SQL Injection payload
- `--xss`: Generate an XSS payload
- `--cmd`: Generate a Command Injection payload
- `--custom <payloads>`: Generate a custom payload from a comma-separated list of payloads

#### Examples
Generate an SQL Injection payload:
```bash
python payloadgen.py --sql
```

Generate an XSS payload:
```bash
python payloadgen.py --xss
```

Generate a Command Injection payload:
```bash
python payloadgen.py --cmd
```

Generate a custom payload:
```bash
python payloadgen.py --custom "<payload1>,<payload2>,<payload3>"
```

## File Operations
### Save Custom Payloads
You can save a list of custom payloads to a file from the interactive menu:
1. Select the option to save custom payloads.
2. Enter the custom payloads separated by commas.
3. Enter the filename to save the payloads.

### Load Custom Payloads
You can load custom payloads from a file from the interactive menu:
1. Select the option to load custom payloads.
2. Enter the filename to load the payloads from.

## Example
```bash
$ python payloadgen.py
Payload Generator Menu:
1. Generate SQL Injection Payload
2. Generate XSS Payload
3. Generate Command Injection Payload
4. Generate Custom Payload
5. View History
6. Save Custom Payloads to File
7. Load Custom Payloads from File
8. Exit
Enter your choice: 1
Generated SQL Injection Payload: ' OR '1'='1
```

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Contact
For any questions or suggestions, please open an issue on GitHub.

---

Enjoy using the Payload Generator Tool for your security testing needs!
