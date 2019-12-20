# -*- coding: utf-8 -*-
"""
 This class loads information from dataframe to QTableView.
    It counts number of rows and column through the use of dataframe' column and row count.

@author: Team Job Buddy
"""
from PyQt5 import QtCore

Qt = QtCore.Qt

class PandasModel(QtCore.QAbstractTableModel):

    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]))
        return QtCore.QVariant()
        
        
