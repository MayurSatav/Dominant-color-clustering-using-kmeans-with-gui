from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from PIL import ImageTk, Image
#import ntpath
#import os

# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
#import argparse
import utils
import cv2

class Root(Tk):

    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Dialog Widget")
        self.minsize(300, 500)
        #self.wm_iconbitmap('icon.ico')

        self.labelFrame = ttk.LabelFrame(self, text ='Input Image')
        self.labelFrame.grid(column = 0, row = 1, padx = 5, pady = 5)
        
        self.labelFrame1 = ttk.LabelFrame(self, text ='Path')
        self.labelFrame1.grid(column = 0, row = 3, padx = 5, pady = 5)
        
        self.labelFrame2 = ttk.LabelFrame(self, text ='Cluster')
        self.labelFrame2.grid(column = 0, row = 4, padx = 5, pady = 5)

        self.labelFrame3 = ttk.LabelFrame(self, text ='Image')
        self.labelFrame3.grid(column = 0, row = 5, padx = 5, pady = 5)

        self.labelFrame4 = ttk.LabelFrame(self, text ='Run')
        self.labelFrame4.grid(column = 0, row = 6, padx = 5, pady = 5)
        
        
        

        self.button()
        
    def button(self):
        self.button = ttk.Button(self.labelFrame, text = 'Browse File', width=50,command = self.fileDialog)
        self.button.grid(column = 0, row = 1)
        
        self.spin = ttk.Spinbox(self.labelFrame2, from_=0, to=10,width=48) 
        self.spin.grid(column=0, row=3)

        #global spinvalue
        #self.spinvalue=spin.get()
        #print ('spinvalue',spinvalue)
        
        self.button1 = ttk.Button(self.labelFrame4, text = 'Run Program', width=50,command = self.RunPro)
        self.button1.grid(column = 0, row = 1)
        

    def RunPro(self):
    
        myimage = self.path
        mycluster = int((self.spin).get())

        # load the image and convert it from BGR to RGB so that
        # we can dispaly it with matplotlib
        image = cv2.imread(myimage)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # reshape the image to be a list of pixels
        image = image.reshape((image.shape[0] * image.shape[1], 3))

        # cluster the pixel intensities
        clt = KMeans(n_clusters = mycluster)
        clt.fit(image)

        # build a histogram of clusters and then create a figure
        # representing the number of pixels labeled to each color
        hist = utils.centroid_histogram(clt)
        bar = utils.plot_colors(hist, clt.cluster_centers_)

        # show our color bart
        plt.figure()
        plt.axis("off")
        plt.imshow(bar)
        plt.show()

        
    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir= '/',title = 'select file', filetype = (('jpeg','*.jpg'),('All Files','*.*')))

        #self.label = ttk.Label(self.labelFrame, text = '')
        #self.label.grid(column = 0,row = 2)

        self.e1 = ttk.Entry(self.labelFrame1, width = 50)
        self.e1.insert(0, self.filename)
        self.e1.grid(row=2, column=0, columnspan=50)
        
        #self.label.configure(text = self.filename)
        Root.OpenImage(self.filename)
        #place image
        
        newpath=self.filename
        self.path = newpath.replace('/','\\\\')
        print (self.path)
        
        im = Image.open(self.path)
        resized = im.resize((300, 300),Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized)
        myvar=ttk.Label(self.labelFrame3,image = tkimage)
        myvar.image = tkimage
        myvar.grid(column=0, row=4)

        
        

    def OpenImage(self):
        pass
        
        
        


if __name__ == '__main__':
    
    root = Root()
    
    root.mainloop()
