import os
import subprocess
for file in os.listdir(r"/Users/chrismitsacopoulos/Downloads"):
    if file.endswith(".fq"):
        print(f"starting {file} conversion")
        filepath = os.path.join(r"/Users/chrismitsacopoulos/Downloads", file)
        newname = file.split("-")[0]
        subprocess.run(f"seqtk seq -a {filepath} > /Users/chrismitsacopoulos/Downloads/{newname}.fa", shell=True)
        print(f"{newname} conversion complete, moving on")
    else:
        print("moving on")
