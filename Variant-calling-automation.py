import subprocess
import os
import shlex


main_directory = "/home/student/resources/workshops/ws3-variant-calling"
if os.path.exists(os.path.join(main_directory, "RESULTS.txt")):
    os.remove(os.path.join(main_directory, "RESULTS.txt"))
    print("Deleted previous file!")
main_dir_indexes = [y for y in os.listdir(main_directory) if not "RESULTS" in y]
for item in main_dir_indexes:
    extended_path = os.path.join(main_directory, item)
    list_of_dirs = [x for x in os.listdir(extended_path) if ".vcf" in x and "pilon" in x]
    for index in list_of_dirs:
        if "filtered" in str(index):
            specific_file = os.path.join(extended_path, index)
            cmd = f"perl /home/student/resources/workshops/VCF_summary.pl {specific_file}"
            amogus = subprocess.run(cmd, shell=True, capture_output=True, cwd=extended_path)
            with open(os.path.join(main_directory, "RESULTS.txt"), 'a') as output:
               output.write(f"{item}\n{amogus}\n")
        else:
            extra = '(LowCov|Amb|Del)'
            specific_file_2 = os.path.join(extended_path, index)
            final_exit = os.path.join(extended_path, f"{item}-bwa-mem.sorted.bam.pilon-filtered.vcf")
            if not os.path.exists(final_exit):
                with open(final_exit, 'w') as one:
                    pass
            directive = f"grep -vwE {shlex.quote(extra)} {specific_file_2} > {final_exit}"
            subprocess.run(directive, cwd=extended_path, shell=True)
            cmd_2 = f"perl /home/student/resources/workshops/VCF_summary.pl {final_exit}"
            amogusus = subprocess.run(cmd_2, shell=True, capture_output=True, cwd=extended_path)
            with open(os.path.join(main_directory, "RESULTS.txt"), 'a') as output:
                output.write(f"{item}\n{amogusus}\n")
