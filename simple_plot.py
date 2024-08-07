# import sys
import pyqtgraph as pg
import pandas as pd

# print(sys.version)

column_to_plot = [1] #specify which columns to plot, up to 7, index start from 0
scaling_factor = [1, 1, 1, 1, 0.01, 0.1, 1, 1]
offset = [0, 0, 0, 0, 0, 50, 0, 0]
line_colour = ['g', 'b', 'r', 'c', 'm', 'r', 'k', 'g']
##################################### Read CSV file ###################################################

csv_data= pd.read_csv("sample_log.csv")
# csv_data= pd.read_csv(str(sys.argv[1]))

column_names = list(csv_data.columns.values)
##################################### Graph Related ###################################################

x_axis_start = 0
x_axis_end = len(csv_data.index)
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
pg.setConfigOptions(antialias=True)
win = pg.GraphicsLayoutWidget(show=True)
win.resize(800,600) ### Initial window size, x and y ###
win.setWindowTitle('Simple Plot')

########################################################################################################
##########################################   PLOT   ####################################################
########################################################################################################

plot_1 = win.addPlot(colspan=2,title="Title")
plot_1.setLabel('bottom', 'Sample No.', 's')
plot_1.setLabel('left', 'Y-axis', 'Unit')
plot_1.setXRange(x_axis_start, x_axis_end)
# plot_1.setYRange(0,12,padding=0)
plot_1.showAxis('right')
plot_1.setMouseEnabled(y=False)
plot_1.addLegend()  ### Legend can be dragged around with mouse

for x in range(len(column_to_plot)):
    data_to_plot = (csv_data[csv_data.columns[column_to_plot[x]]].tolist())[1:] #convert pandas column to list
    data_to_plot = [(i * scaling_factor[x] + offset[x]) for i in data_to_plot] #apply the scaling factor
    plot_1.plot(data_to_plot, pen = line_colour[x], name = column_names[column_to_plot[x]])

########################################################################################################
##########################################   MAIN   ####################################################
########################################################################################################
def main():
    #GUI starts, and blocking
    pg.exec()   

########################################################################################################
##########################################   MAIN   ####################################################
########################################################################################################

if __name__ == '__main__':
    main()
