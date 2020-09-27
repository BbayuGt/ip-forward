from cx_Freeze import setup, Executable

base = None

executables = [Executable("IP forward.py", base=base)]

packages = ["click", "random", "requests", "http.server", "getpass", "hashlib", "datetime", "subprocess"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "ip-forward",
    options = options,
    version = "1.4",
    description = 'By BbayuGt',
    executables = executables
)
