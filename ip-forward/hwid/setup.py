from cx_Freeze import setup, Executable

base = None

executables = [Executable("hwid.py", base=base)]

packages = ["getpass", "subprocess", "hashlib"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "hwid checker for ip-forward",
    options = options,
    version = None,
    description = 'By BbayuGt',
    executables = executables
)
