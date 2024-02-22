import subprocess
import os


main_directory = "/home/student/resources/workshops/ws3-variant-calling"
main_dir_indexes = [y for y in os.listdir(
    main_directory) if not "RESULTS" in y]
for item in main_dir_indexes:
    extended_path = os.path.join(main_directory, item)
    list_of_dirs = [x for x in os.listdir(extended_path) if ".vcf" in x]
    for index in list_of_dirs:
        specific_file = os.path.join(extended_path, index)
        if "filtered" in index:
            cmd = [
                "perl", "/home/student/resources/workshops/VCF_summary.pl", specific_file]
            amogus = subprocess.run(
                cmd, shell=True, capture_output=True, cwd=extended_path)
            amogus_lines = amogus.stdout.split("\n")
            with open(os.path.join(main_directory, "RESULTS.txt"), 'a') as output:
                for line in amogus_lines:
                    output.write(f"{item}\n{line}\n")
        else:
            extra = "(LowCov|Amb|Del)"
            final_exit = os.path.join(extended_path, f"{item}-bwa-mem.sorted.bam.pilon-filtered.vcf")
            if not os.path.exists(final_exit):
                with open(final_exit, 'w') as one:
                    pass
            directive = ["grep", "-vwE", f"{extra}", specific_file, ">", ]
            subprocess.run(directive, cwd=extended_path)
            cmd = [
                "perl", "/home/student/resources/workshops/VCF_summary.pl", specific_file]
            amogusus = subprocess.run(
                cmd, shell=True, capture_output=True, cwd=extended_path)
            amogusus_lines = amogus.stdout.split("\n")
            with open(os.path.join(main_directory, "RESULTS.txt"), 'a') as output:
                for liner in amogusus_lines:
                    output.write(f"{item}\n{liner}\n")
