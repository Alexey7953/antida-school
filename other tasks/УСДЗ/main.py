
# Create application
    import sys
    app = QtGui.QApplication(sys.argv)
    USDZ = QtGui.QDialog()
    ui = Ui_USDZ()
    ui.setupUi(USDZ)
    USDZ.show()
    sys.exit(app.exec_())