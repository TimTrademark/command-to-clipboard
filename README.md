# Command to clipboard 📎

## Motivation

I created this simple tool during my preparation for the OSCP certification
where I found myself having to retype a lot of commands. 
Command to clipboard saves a lot of time by copying a predefined 
command to your clipboard, especially in non-interactive shell 
environments like a *reverse shell* where you can't move your cursor to replace values.

## Configuration

You can customize the command in the config.json file, a default template is provided:
```json
{
  "command": "iwr -uri http://${IP}:${PORT}/${0} -Outfile ${0}",
  "parameters": {
    "IP": "192.168.0.1",
    "PORT": "80"
  }
}
```
You can add/remove parameters under `"parameters"`, these will replace the corresponding values in the `"command"` 
string annotated by `${}`.

The annotations containing a number like `${0}` correspond to the specified command-line arguments.

## Usage

```commandline
python3 cmd_to_clipboard.py test.txt
```
Will result in `iwr -uri http://192.168.0.1:80/test.txt -Outfile test.txt`
