"""
This example presents how to draw a map with identified intervals.
"""

import sys

sys.path.append("../")

from sport_activities_features.interval_identification import (
    IntervalIdentificationByPower,
    IntervalIdentificationByHeartrate,
)
from sport_activities_features.tcx_manipulation import TCXFile
from sport_activities_features.plot_data import PlotData

# Reading the TCX file
tcx_file = TCXFile()
(
    activity_type,
    positions,
    altitudes,
    distances,
    total_distance,
    timestamps,
    heartrates,
) = tcx_file.read_one_file("path_to_the_data").values()

# Identifying the intervals in the activity by power and drawing the map
Intervals = IntervalIdentificationByPower(distances, timestamps, altitudes, 70)
Intervals.identify_intervals()
all_intervals = Intervals.return_intervals()
Map = PlotData()
Map.draw_intervals_in_map(timestamps, distances, all_intervals)

# Identifying the intervals in the activity by heart rate and drawing the map
Intervals = IntervalIdentificationByHeartrate(
    distances, timestamps, altitudes, heartrates
)
Intervals.identify_intervals()
all_intervals = Intervals.return_intervals()
Map = PlotData()
Map.draw_intervals_in_map(timestamps, distances, all_intervals)
