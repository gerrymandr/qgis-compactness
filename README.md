# QGIS plugin for Compactness Metrics

A work-in-progress at the Metric Geometry and Gerrymandering Group (MGGG)

An open-source plugin built to allow QGIS users to apply different Measures of Compactness on District polygons

Built on top of Python's [Mander Library](https://pypi.python.org/pypi/mander)

## Using these Resources

* <a href="https://pypi.python.org/pypi/mander">Mander Library</a>
* <a href="https://plugins.qgis.org/plugins/pluginbuilder/">QGIS plugin builder</a>
* <a href="https://www.qt.io/download/">QT Creator</a>

## Setup

1.  In your QGIS plugin directory, compile the resources file using pyrcc4 (simply run **make** if you have automake or use **pb_tool**)
2.  Test the generated sources using **make test** (or run tests from your IDE)
3.  Copy the entire directory containing your new plugin to the QGIS plugin directory (see Notes below)
4.  Test the plugin by enabling it in the QGIS plugin manager
5.  Customize it by editing the implementation file **compactness_calculator.py**
6.  Create your own custom icon, replacing the default **icon.png**
7.  Modify your user interface by opening **compactness_calculator_dialog_base.ui** in Qt Designer

Notes:

*   You can use the **Makefile** to compile and deploy when you make changes. This requires GNU make (gmake). The Makefile is ready to use, however you will have to edit it to add addional Python source files, dialogs, and translations.
*   You can also use **pb_tool** to compile and deploy your plugin. Tweak the _pb_tool.cfg_ file included with your plugin as you add files. Install **pb_tool** using _pip_ or _easy_install_. See [http://loc8.cc/pb_tool](http://loc8.cc/pb_tool) for more information.

## License

Open source, MIT license
