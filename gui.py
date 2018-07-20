from __init__ import *

class SimpleExample1(BaseWidget):
    
    
    def __init__(self):
        super(SimpleExample1,self).__init__('Crypto Thing')#Defines title

        #Definition of the forms fields
        self._coinone     = ControlText('Coin 1')
        self._cointwo     = ControlText('Coin 2')
        self._coithree         = ControlText('Coin 3')
        self._coinfour         = ControlText('Coin 4')
        self._button         = ControlButton('Look up')
        self._graph         = ControlMatplotlib('Graph')

        #Define the button action
        self._button.value = self.__buttonAction

        self._graph.value = self.__on_draw



    def __on_draw(self, figure):
        """ Redraws the figure
        """
        data = [25, 500, 1250, .01]
        x      = ["cern1", "cern2", "cern3", "cern4"]
        
        axes = figure.add_subplot(111)
        axes.bar(left=x, height=data)

        
        #axes = figure.add_subplot(222, projection='3d')
        #axes.clear(); 
        #pts = axes.scatter(x, data, data, c=x)
        #figure.colorbar(pts)


    def __buttonAction(self):
        """Button action event"""
        self._coinone = self._coinone.value
        self._cointwo = self._cointwo.value
        self._cointhree = self._cointhree.value
        self._coinfour = self._coinfour.value




##################################################################################################################
##################################################################################################################
##################################################################################################################

#Execute the application
if __name__ == "__main__": pyforms.start_app( SimpleExample1 )