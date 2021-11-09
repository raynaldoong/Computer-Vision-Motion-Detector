# Project Scope
The purpose of this project is to further solidify my knowledge on video processing using Computer Vision and interactive visualisation using Bokeh.

# Project Methodology 
1. Check if the camera works, when camera turns on it captures the first frame as reference 
<img src="images/color frame.png" alt="test" width="800"/>
3. Refreshes frame every 1 ms
4. Creates a Gray Frame and makes frame blury to make it insensitive to small changes
<img src="schema.png" alt="query2" width="800"/>
6. Creates a Delta Frame which calculates the difference in first frame and all following frame
<img src="schema.png" alt="query2" width="800"/>
8. Creates a Thershold Frame which determines when the difference in first frame and following frame is more than 30 using cv2.THRESH_BINARY
<img src="schema.png" alt="query2" width="800"/>
10. For every changes it detects, creates a green rectangular using cv2.rectangle
<img src="schema.png" alt="query2" width="800"/>
12. Tracks every changes in motion from Threshold Frame, plot a barchart using Bokeh 
<img src="schema.png" alt="query2" width="800"/>
14. Press q to exit 

# Project Respository Files
## Capture.py
A python file consisting the codes for video processing
## Graph1.html
An HTML file consisting the code needed to load Bokeh Graph to browser
## Plotting.py
A ptython file consisting the codes for data visualisation
## Times.csv
A CSV file that tracks the start and end time when motion is detected
