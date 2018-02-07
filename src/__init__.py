"""
/***************************************************************************
ImageMapPlugin

This beta plugin generates a HTML-image map compatible with MicroStrategy

copyright            : forked the famous 'Html Image Map Plugin' from Richard Duivenvoorde
email                : o2br.com@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
from imagemapplugin import ImageMapPlugin

def name():
    return "Html Image Map To Business Inteligence"

def description():
    return "This beta plugin generates a HTML-image map compatible with MicroStrategy"

def qgisMinimumVersion():
    return "2.0"

def version():
    return "2.0.1"

def author():
    return "Andre da Silva Mesquita"

def email():
    return "o2br.com@gmail.com"

def category():
  return "Web"

def classFactory(iface):
    return ImageMapPlugin(iface)

