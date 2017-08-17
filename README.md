# QGIS plugin for Compactness Metrics

A work-in-progress at the Metric Geometry and Gerrymandering Group (MGGG).

An open-source plugin built to allow QGIS users to apply different Measures of Compactness on District polygons.

1. Select a layer
1. (*optional*) Select one or more specific features
1. Click Compactness Calculator and choose desired metrics
1. Choose to save the layer/selection to disk (GeoJSON or Shapefile) and/or add it to your project

Built on top of the Python [Mander Library](https://pypi.python.org/pypi/mander) v. 0.3 and 64-bit QGIS 2.18.11

Watch this for an overview on the issues concerning [Redistricting, Gerrymandering, and Compactness of Political Districts](https://www.youtube.com/watch?v=vdkvQ9y04K4)

## Installation

1. Clone this repository and copy it to your QGIS plugins directory (for example, `~/.qgis2/python/plugins/`).
1. Install mander to your Python environment with eg. `[sudo ]pip install mander`.
1. Open QGIS and in the Plugins menu click `Manage and Install Plugins`.
1. Click `Settings` and check `Show also experimental plugins`.
1. Click `All` and find the `Compactness Calculator` plugin and click `Install`.
1. Make sure the checkbox is checked and click `Close`.
1. You should see a `Compactness Calculations` menu item in the `Vector` menu and a button on the toolbar.

(*In future*) The plugin will be available on the public QGIS plugin repository.

## Roadmap

### Phase 1: Meet standards for public plugins
* No duplicate functionality with existing plugins.
* Link to documentation from inside the plugin.
* Include a test set.
* Confirm metadata links are correct.
* PEP8 compliance and commenting.
* Rename folder (and repo) to not contain the word plugin.
* Add external dependencies to "About" metadata field.
* Create OSGeo account.

### Phase 2: Obvious and necessary improvements
* **MultiPolygons** - right now only simple polygons are supported.
* **Automatic metric visualization** - right now this is up to the user.
* Unit tests instead of if statements.
* Instead of hardcoding metrics, can we populate them dynamically from mander?
* Diagram or tree of how source code files are connected.
* Custom icon!

### Phase 3: Refactor and optimize
* Can we refactor this to be a subplugin of Processing so it has a lighter footprint and better integration with the rest of QGIS? (eg. modeling, batch commands)

## License

Open source, MIT license

# Plugin development

## Resources

* [PyQGIS Developer Cookbook](http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/)
* [QGIS API](http://www.qgis.org/api/)
* [Mander](https://pypi.python.org/pypi/mander)
* [QGIS Plugin Building]("https://plugins.qgis.org/plugins/pluginbuilder/")
* [QT Creator]("https://www.qt.io/download/")
* Google keyword `pyqgis`

## Tutorials

Plugin Builder has a ton of built in documentation that will describe how to compile and build your plugin. An example is copied here.

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
