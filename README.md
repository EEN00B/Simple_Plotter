# Simple_Plotter
A python script to print CSV to line curves using pyqtgraph

Live-interaction, <br />
Zoom, Pan, <br />
Drag, <br />
Crosshair, <br />
Data Points when zoomed in <br />
and many more. <br />

The Data Points feature would make things a bit slow but still acceptable. <br />

Without Data Points feature, it opens and plots the example file (1.3M data, 8 column) in ~560 millisecond.  <br />

With Data Points feature, it takes ~2.8 second. <br />

Check out the screenshots below.

Tested with 8 columns of 1.3 million data points each column.

The code is pretty self-explanatory 

Known issue: Line Weight higher than 1.0 will cause performance issue (lag)
Details at:https://github.com/pyqtgraph/pyqtgraph/issues/533

===============================================================

![Screenshot 2024-08-07 164003](https://github.com/user-attachments/assets/49a9bdb0-4678-49f3-984a-8989f11b8378)
![Screenshot 2024-08-07 164022](https://github.com/user-attachments/assets/fad04b57-6d21-41b7-a2a7-c9eb510c42fc)
![Screenshot 2024-08-07 164455](https://github.com/user-attachments/assets/848836ea-614a-47d4-ab3a-d87067f84497)
![Screenshot 2024-08-07 164426](https://github.com/user-attachments/assets/18eba1fe-d58d-4473-bf89-c903bc784e29)
![Screenshot 2024-08-07 164352](https://github.com/user-attachments/assets/f609a7a7-cb97-4c7e-81c2-363ede81dc3c)
![Screenshot 2024-08-07 164306](https://github.com/user-attachments/assets/55b1b3bf-1b3c-40cf-abcc-35da9071269c)
![image](https://github.com/user-attachments/assets/442f0952-0562-40d1-9ef3-468d41bc9d6a)
