# -*- coding: utf-8 -*-
"""
/***************************************************************************
 compactnessCalculatorDialog
                                 A QGIS plugin
 Compactness calculations
                             -------------------
        begin                : 2017-08-10
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Ariel and Vanessa
        email                : vanessa@flippable.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from qgis.core import QgsMapLayerRegistry

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'compactness_calculator_dialog_base.ui'))


class compactnessCalculatorDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, iface, parent=None):
        """Constructor."""
        self.iface = iface
        super(compactnessCalculatorDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.cbo1.clear()
        self.cbo2.clear()
        legendInterface = self.iface.legendInterface()
        listLayerName = [i.name() for i in legendInterface.layers() if i.type() == QgsMapLayer.VectorLayer]
        self.cbo1.addItems(listLayerName)
        self.cbo2.addItems(listLayerName)
        #connect filepath bar to browse function
        self.Browse.clicked.connect(self.outFile)

    def outFile(self): 
        # by Carson Farmer 2008
        # display file dialog for output shapefile
        self.outShp.clear()
        fileDialog = QtGui.QFileDialog()
        fileDialog.setConfirmOverwrite(False)
        outName = fileDialog.getSaveFileName(self, "Output Shapefile",".", "Shapefiles (*.shp)")
        outPath = QtCore.QFileInfo(outName).absoluteFilePath()
        if not outPath.upper().endswith(".SHP"):
            outPath = outPath + ".shp"
        if outName:
            self.outShp.clear()
            self.outShp.insert(outPath)
