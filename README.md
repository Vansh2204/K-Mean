# K-Mean
KMean Algorithm of Clustering created using libraries and tkinter for GUI 

## Imports 

tkinter - To get GUI
filedialog and message dialog to get appropriate actions of messages.

pandas - library for data manipulation and here used to read the selected csv file
sklearn , cluster , KMeans - Imports the KMean class from cluster module from sklearn with include KMean Algorithm
matplotlib - To get the scatter plot and to plot the points for cluster creation

## init(self,root)
Root window as the main container and packs it in a frame.
Vista theme is used from tkinter.
Widgets like button, label, frame, entry(to enter the value count of clusters to be made)

## upload_file(self)
Filedialog from tkinter to get the file from the system.
Pandas library to read the file from the user as read_csv.
And after the file is uploaded the button set to normal from disabled

## perform_kmeans(self)
Check if the data is not null.
Converts the number enetered to an integer and pass it in an object of KMean
# fit_predict
What is does, **fit** means it iteratively moves and gets the cluster , it runs until we get no change in the cluster assignment
**predict** assign that which cluster belong to which data point.









