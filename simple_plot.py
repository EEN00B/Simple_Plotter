# import sys
import pyqtgraph as pg
import pandas as pd

# print(sys.version)

column_to_plot = [1,2,3,4,5,6,7,8] #specify which columns to plot, up to 8 columns, index start from 0
scaling_factor = [1, 1, 1, 1, 1, 1, 1, 1] #scaling factor to apply later
offset = [0, 0, 0, 0, 0, 0, 0, 0] #offset to apply later
line_colour = [(39, 64, 1), (130, 138, 0), (242, 159, 5), (242, 92, 5),
               (214, 86, 140), (77, 133, 132), (166, 47, 3), (64, 13, 1)]
##################################### Read CSV file ###################################################

csv_data= pd.read_csv("sample_log.csv")
# csv_data= pd.read_csv(str(sys.argv[1]))

column_names = list(csv_data.columns.values)

data_to_plot = [0,0,0,0,0,0,0,0]

for x in range(len(column_to_plot)):
    data_to_plot[x] = (csv_data[csv_data.columns[column_to_plot[x]]].tolist())[1:] #convert pandas column to list
    data_to_plot[x] = [(i * scaling_factor[x] + offset[x]) for i in data_to_plot[x]] #apply the scaling factor

##################################### Graph Related ###################################################

x_axis_start = 0
x_axis_end = len(csv_data.index)
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
pg.setConfigOptions(antialias=True)
win = pg.GraphicsLayoutWidget(show=True)
win.resize(800,600) ### Initial window size, x and y ###
win.setWindowTitle('Simple Plot')

label = pg.LabelItem(justify='right')
win.addItem(label)

########################################################################################################
##########################################   PLOT   ####################################################
########################################################################################################

plot_1 = win.addPlot(row=1,col=0,title="Title")
plot_1.setLabel('bottom', 'Sample No.', 's')
plot_1.setLabel('left', 'Y-axis', 'Unit')
plot_1.setXRange(x_axis_start, x_axis_end)
# plot_1.setYRange(0,12,padding=0)
plot_1.showAxis('right')
plot_1.setMouseEnabled(y=False)
plot_1.addLegend()  ### Legend can be dragged around with mouse

for x in range(len(column_to_plot)):
    plot_1.plot(data_to_plot[x], pen = line_colour[x], name = column_names[column_to_plot[x]])

########################################################################################################
##########################################   CROSSHAIR   ###############################################
########################################################################################################

vLine = pg.InfiniteLine(angle=90, movable=False)
hLine = pg.InfiniteLine(angle=0, movable=False)
plot_1.addItem(vLine, ignoreBounds=True)
plot_1.addItem(hLine, ignoreBounds=True)

vb = plot_1.vb

def mouseMoved(evt):
    pos = evt[0]  ## using signal proxy turns original arguments into a tuple
    if plot_1.sceneBoundingRect().contains(pos):
        mousePoint = vb.mapSceneToView(pos)
        index = int(mousePoint.x())
        if index > 0 and index < len(data_to_plot[0]):
            format_str = "x=%d, " + ", ".join(f"{column_names[column_to_plot[i]]}=%0.1f" for i in range(len(column_to_plot)))
            values = [mousePoint.x()] + [data_to_plot[i][index] for i in range(len(column_to_plot))]
            label.setText(format_str % tuple(values))

        vLine.setPos(mousePoint.x())
        hLine.setPos(mousePoint.y())


proxy = pg.SignalProxy(plot_1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)


########################################################################################################
##########################################   MAIN   ####################################################
########################################################################################################
def main():
    #GUI starts, and blocking
    pg.exec()   

if __name__ == '__main__':
    main()
