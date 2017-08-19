import sys
from config import *
from search.java.exec.util import FolderManager
from search.java.exec.util import JsonInputFile
from search.java.exec.util import JsonProcessedUrls
from search.java.exec.util import GitUtil

# make folders
if not FolderManager.create_folder(RESULT_FOLDER) or \
	not FolderManager.create_folder(TEMP_REPOS_FOLDER):
	print("error to create result and repos folder")
	sys.exit()

# open json file and get urls
jsonInputFile = JsonInputFile(INPUT_JSON_FILE)
urls = jsonInputFile.get_urls()

# for each url not in db do clone(url)
jsonProcessedUrls = JsonProcessedUrls(PROCESSED_JSON_FILE)
for url in urls:
	if not jsonProcessedUrls.check_url(url):

		git_util = GitUtil(url)
		if git_util.clone(TEMP_REPOS_FOLDER):
			
			# get a list of java files in temporary folder

			
			# run a thread for each file (limited by number of threads)

				
				# analyze imports of each file. if file ok, put in results (if not exists)

			
			jsonProcessedUrls.add_url(url)

		git_util.delete_local_repo()
