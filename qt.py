import sys
from PyQt5 import QtCore , QtWidgets, QtGui, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtMultimedia import QCamera, QCameraInfo, QMediaObject, QCameraViewfinderSettings, QCameraImageCapture
from PyQt5.QtMultimediaWidgets import QCameraViewfinder


class Camera(QObject):
    def __init__(self, parent = QObject()):
        super(Camera, self).__init__(parent)
        self.cam = QCamera()
        self.caminfo = QCameraInfo(self.cam)
        self.camvfind = QCameraViewfinder()
        self.camvfindset = QCameraViewfinderSettings()
        self.cammode = self.cam.CaptureMode(1)
        self.camimgcap = QCameraImageCapture(self.cam)

    def iniCamera(self):
        print(self.caminfo.description())
        print(self.caminfo.availableCameras())
        
        if self.cam.isCaptureModeSupported(self.cammode):
            print("Capturemode supported")
            
    
    def startVid(self):
        self.camvfind.setVisible(True)
        
        self.cam.setViewfinder(self.camvfind)

        self.cam.setCaptureMode(self.cammode)
        self.cam.start()
        
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    cam = Camera()
    
    cam.iniCamera()
    
    cam.startVid()
    
    sys.exit(app.exec_())
