import tarfile
import os


def create_tar_archive(output_file, needed_files):
	# Get the directory containing the script as the build context
	script_directory = os.path.dirname(os.path.abspath(__file__))
	build_context = os.path.basename(script_directory)

	# Create a tar archive
	with tarfile.open(output_file, "w") as tar:
		# Add all files in the build context to the archive
		for file in os.listdir():
			for needed_file in needed_files:
				if file == needed_file:
					file_path = os.path.join(file)
					tar.add(file_path)

	print(f"Tar archive created: {output_file}")


# Provide the name of the output tar archive
output_filename = "vrchat-ip-grabber.tar"

needed_files = ["Dockerfile", "requirements.txt", "api.py", "grabme.mp4"]

# Create the tar archive
create_tar_archive(output_filename, needed_files)