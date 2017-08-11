# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CompactnessCalculatorDialog
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
import util

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'compactness_calculator_dialog_base.ui'))


class CompactnessCalculatorDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(CompactnessCalculatorDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.browse)
        # self.okButton.clicked.connect(self.ok)
        # self.cancelButton.clicked.connect(self.reject)
        # layer changed event
        # self.layerBox.currentIndexChanged.connect(self.sel)

    def browse(self):
        self.lineEdit.clear()    # clear output file field
        # open file dialog
        (self.shapefileName, self.encoding) = util.saveDialog(self)
        if self.shapefileName is None or self.encoding is None:
            return
        self.lineEdit.setText(self.shapefileName)  # fill output file field
