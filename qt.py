 import sys
from PyQt5 import QtCore , QtWidgets, QtGui, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtMultimedia import QCamera, QCameraInfo, QMediaObject, QCameraViewfinderSettings, QCameraImageCapture
from PyQt5.QtMultimediaWidgets import QCameraViewfinder


class Camera(QObject):
    def __init__(self, parent = QObject()):
        super(Camera, self).__init__(parent)
        print("3")
        self.cam = QCamera(QCameraInfo.defaultCamera())   #"/dev/video0".encode()
        print("4")
        self.caminfo = QCameraInfo(self.cam)
        self.camvfind = QCameraViewfinder()
        self.camvfindset = QCameraViewfinderSettings()
        self.cammode = self.cam.CaptureMode(0)
        self.camimgcap = QCameraImageCapture(self.cam)

    def iniCamera(self):
        print(self.caminfo.description())
        print(self.caminfo.availableCameras())

        for caminfo in QCameraInfo.availableCameras():
            print(caminfo.deviceName())

        if self.cam.isCaptureModeSupported(self.cammode):
            print("Capturemode supported")

    def startVid(self):
        #self.camimgcap.CaptureDestination(2)

        self.camvfind.show()

        self.cam.setViewfinder(self.camvfind)

        self.cam.setCaptureMode(self.cammode)

        self.cam.start()



if __name__ == '__main__':
    print("1")
    app = QtWidgets.QApplication(sys.argv)
    print("2")
    cam = Camera()
    print("4")
    cam.iniCamera()

    cam.startVid()

    sys.exit(app.exec_())
