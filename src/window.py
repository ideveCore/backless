# window.py
#
# Copyright 2024 Ideve Core
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import gi

gi.require_version("Adw", "1")
gi.require_version("Gtk", "4.0")

from typing import Union, Dict
from gi.repository import Adw, Gdk, Gio, Gtk
from .define import RES_PATH
from .components import Shortcuts

resource = f"{RES_PATH}/window.ui"

def create_main_window(application: Adw.Application):
  builder = Gtk.Builder.new_from_resource(resource)
  settings = application.utils.settings
  window = builder.get_object("window")
  content = builder.get_object("content")
  menu_button = builder.get_object("menu_button")

  def load_window_state():
    settings.bind(
      key="width",
      object=window,
      property="default-width",
      flags=Gio.SettingsBindFlags.DEFAULT,
    )
    settings.bind(
      key="height",
      object=window,
      property="default-height",
      flags=Gio.SettingsBindFlags.DEFAULT,
    )
    settings.bind(
      key="is-maximized",
      object=window,
      property="maximized",
      flags=Gio.SettingsBindFlags.DEFAULT,
    )
    settings.bind(
      key="is-fullscreen",
      object=window,
      property="fullscreened",
      flags=Gio.SettingsBindFlags.DEFAULT,
    )
    window.set_help_overlay(Shortcuts())

  load_window_state()
  window.set_application(application)
  window.set_icon_name(application.get_application_id())
  return window
