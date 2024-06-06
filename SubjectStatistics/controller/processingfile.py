from SubjectStatistics.models import file

def processing_file():
    read_file = file.ReadFile()
    read_file.read()
    read_file.display_file()
