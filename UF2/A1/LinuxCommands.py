COMMANDS = ('touch', 'grep', 'cat', 'fdisk', 'cmp', 'dmesg', 'man', 'top', 'htop', 'halt')
HELP_VER = (('v1.2', 'touch: Create an empty file.'), ('v2.5', 'grep: Search for patterns in files.'), ('v3.1', 'cat: Concatenate and display file contents.'), ('v1.8', 'fdisk: Manipulate disk partition tables.'), ('v2.3', 'cmp: Compare two files byte by byte.'), ('v1.6', 'dmesg: Display system message buffer.'), ('v2.0', 'man: Display manual pages for commands.'), ('v1.4', 'top: Display and update sorted information about processes.'), ('v3.2', 'htop: Interactive process viewer.'), ('v1.9', 'halt: Stop the system.'))
OPTIONS = ('-v', '--version', '-h', '--help')


def read_input(COMMANDS):
    cmd = input().split()
    if cmd == 'halt':
        return cmd
    elif len(cmd) != 1:
        if cmd[0] in COMMANDS and cmd[1] in OPTIONS:
            return cmd
        else:
            print(f'{cmd} command not found.')
    else:
        print(f'Options needed.')

def execute_command(cmd):
    match cmd:
        case '-v':
            print(HELP_VER)