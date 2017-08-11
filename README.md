### Plugin Builder Results

Congratulations! You just built a plugin for QGIS!  

<div id="help" style="font-size:.9em;">Your plugin **CompactnessCalculator** was created in:  
  **/Users/vanessaarchambault/Documents/tufts/CompactnessCalculator**

Your QGIS plugin directory is located at:  
  **/Users/vanessaarchambault/.qgis2/python/plugins**

### What's Next

1.  In your plugin directory, compile the resources file using pyrcc4 (simply run **make** if you have automake or use **pb_tool**)
2.  Test the generated sources using **make test** (or run tests from your IDE)
3.  Copy the entire directory containing your new plugin to the QGIS plugin directory (see Notes below)
4.  Test the plugin by enabling it in the QGIS plugin manager
5.  Customize it by editing the implementation file **compactness_calculator.py**
6.  Create your own custom icon, replacing the default **icon.png**
7.  Modify your user interface by opening **compactness_calculator_dialog_base.ui** in Qt Designer

Notes:

*   You can use the **Makefile** to compile and deploy when you make changes. This requires GNU make (gmake). The Makefile is ready to use, however you will have to edit it to add addional Python source files, dialogs, and translations.
*   You can also use **pb_tool** to compile and deploy your plugin. Tweak the _pb_tool.cfg_ file included with your plugin as you add files. Install **pb_tool** using _pip_ or _easy_install_. See [http://loc8.cc/pb_tool](http://loc8.cc/pb_tool) for more information.

</div>

<div style="font-size:.9em;">

For information on writing PyQGIS code, see [http://loc8.cc/pyqgis_resources](http://loc8.cc/pyqgis_resources) for a list of resources.

</div>

©2011-2016 GeoApt LLC - geoapt.com
