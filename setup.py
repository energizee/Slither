import cx_Freeze

executables = [cx_Freeze.Executable("Slither.py")]

cx_Freeze.setup(
    name="Slither",
    version = "1.1",
    options = {"build_exe":{"packages":["pygame"],"include_files":["snakehead.png", "apple.png"]}},
    description = "Slither, a remake of the classic game, snake.",
    executables = executables    
    )