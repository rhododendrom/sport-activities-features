from sport_activities_features import GPXFile


# read TCX file
gpx_file = GPXFile()
data = gpx_file.read_one_file('path_to_file')

