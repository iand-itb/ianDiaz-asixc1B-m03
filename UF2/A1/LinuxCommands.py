COMMANDS = ('touch', 'grep', 'cat', 'fdisk', 'cmp', 'dmesg', 'man', 'top', 'htop', 'halt')
HELP_VER = (('v1.2', 'touch: Create an empty file.'), ('v2.5', 'grep: Search for patterns in files.'), ('v3.1', 'cat: Concatenate and display file contents.'), ('v1.8', 'fdisk: Manipulate disk partition tables.'), ('v2.3', 'cmp: Compare two files byte by byte.'), ('v1.6', 'dmesg: Display system message buffer.'), ('v2.0', 'man: Display manual pages for commands.'), ('v1.4', 'top: Display and update sorted information about processes.'), ('v3.2', 'htop: Interactive process viewer.'), ('v1.9', 'halt: Stop the system.'))
options = ['-v', '-h', '--version', '--help']
opt = options.copy()

def read_input(COMMANDS, options, opt):
    cmd = [0]
    while cmd[0] != 'halt':
        cmd = input().split()

        if len(cmd) != 1:
            if cmd[0] in COMMANDS and cmd[1] in options:
                if cmd[1] == '--version':
                    cmd.pop(-1)
                    cmd.append('-v')
                else:
                    cmd.pop(-1)
                    cmd.append('-h')
                opt.pop(-1)
                opt.pop(-1)
                execute_command(cmd, opt)
            elif cmd[0] in COMMANDS and cmd[1] not in options:
                print(f'not valid option {cmd[1]}')
            else:
                print(f'{cmd[0]} command not found.')
        elif cmd[0] != 'halt' and cmd[0] in COMMANDS:
            print(f'{cmd[0]} needs an option. For example -v or -h')
        else:
            if cmd[0] == 'halt':
                continue
            print(f'{cmd[0]} not found.')

def execute_command(cmd, opt):
    function = COMMANDS.index(cmd[0])
    option = opt.index(cmd[1])
    print(HELP_VER[function][option])

read_input(COMMANDS, options, opt)