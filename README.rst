SpectroScope
=================

Spectrum analyzer for multiple SDR platforms (GUI for soapy_power,
hackrf_sweep, rtl_power, rx_power and other backends). SpectroScope is a fork
and continuation of the orphaned QSpectrumanalyzer project.



Screenshots
-----------

.. image:: https://konung-yaropolk.github.io/spectroscope/spectroscope_screenshot.png

.. image:: https://konung-yaropolk.github.io/spectroscope/spectroscope_screenshot2.png

Requirements
------------

- Python >= 3.3
- PyQt4 / PyQt5 / PyQt6 / PySide / PySide2
- QtPy (https://github.com/spyder-ide/qtpy)
- PyQtGraph (http://www.pyqtgraph.org)
- soapy_power (https://github.com/xmikos/soapy_power)
- Optional: hackrf / rtl-sdr / rtl_power_fftw / rx_tools

Backends
--------

Default backend
***************

- **soapy_power** (https://github.com/xmikos/soapy_power)

``soapy_power`` is the default and recommended universal SDR backend in SpectroScope.
It is based on `SoapySDR <https://github.com/pothosware/SoapySDR>`_ and supports
nearly all SDR platforms (RTL-SDR, HackRF, Airspy, SDRplay, LimeSDR, bladeRF,
USRP and some other SDR devices). It is highly configurable (see additional parameters
help in *Settings* menu) and supports short acquisition time for
near real-time continuous measurement.

Other backends
**************

- **hackrf_sweep** (https://github.com/mossmann/hackrf)

``hackrf_sweep`` backend enables wideband spectrum monitoring by rapidly retuning the radio
without requiring individual tuning requests from the host computer. This allows unprecedented
sweep rate of 8 GHz per second. Only HackRF is supported.

- **rtl_power_fftw** (https://github.com/AD-Vega/rtl-power-fftw)

``rtl_power_fftw`` is alternative backend for RTL-SDR devices and has various
benefits over ``rtl_power``. E.g. better FFT performance (thanks to
use of ``fftw`` library) and possibility to use short acquisition time
for near real-time continuous measurement (minimum interval in original
``rtl_power`` is 1 second).

- **rtl_power** (https://github.com/keenerd/rtl-sdr)

``rtl_power`` is original backend for RTL-SDR devices. There are better alternatives now, but
if you want to use it, you should use `Keenerds fork of rtl-sdr <https://github.com/keenerd/rtl-sdr>`_
(latest Git revision), because ``rtl_power`` in original rtl-sdr package (from osmocom.org)
is broken (especially when used with cropping).

- **rx_power** (https://github.com/rxseger/rx_tools) *[unsupported]*

``rx_power`` (part of ``rx_tools``) is also based on SoapySDR (like default ``soapy_power`` backend)
and therefore supports nearly all SDR platforms. But it is much slower than soapy_power, doesn't support
near real-time continuous measurement (minimum interval is 1 second, same as ``rtl_power``)
and is buggy. Backend is currently unsupported, if you want to fix it, patches are welcome.

Usage
-----

Start SpectroScope by running ``spectroscope``.

You can choose which backend you want to use in *File* -> *Settings*
(or *Application menu* -> *Preferences* on Mac OS X), default is
``soapy_power``. Device, sample rate, bandwidth, LNB LO, path to backend executable
and additional backend parameters can be also manually specified there. You can
also set waterfall plot history size. Default is 100 lines, be aware that
really large sweeps (with a lot of bins) would require a lot of system
memory, so don't make this number too big.

Controls should be intuitive, but if you want consistent results, you should
turn off automatic gain control (set gain to some fixed number) and also set
crop to 20% or more. For finding out ppm correction factor for your rtl-sdr
stick, use `kalibrate-rtl <https://github.com/steve-m/kalibrate-rtl>`_.

You can move and zoom plot with mouse, change plot settings or export plots
from right-click menu. Waterfall plot black/white levels and color lookup
table can be changed in mini-histogram widget (on *Levels* tab).

Installation
------------

Arch Linux:
***********

Stable version:
::

    git clone https://aur.archlinux.org/spectroscope.git
    cd spectroscope
    makepkg -sri

Git master branch:
::

    git clone https://aur.archlinux.org/spectroscope-git.git
    cd spectroscope-git
    makepkg -sri

Or simply use `pacaur <https://aur.archlinux.org/packages/pacaur>`_ (or any other AUR helper)
which will also automatically install all SpectroScope dependencies:
::

    pacaur -S spectroscope
    pacaur -S spectroscope-git

Ubuntu:
*******
::

    # Add SoapySDR PPA to your system
    sudo add-apt-repository -y ppa:myriadrf/drivers

    # Update list of packages
    sudo apt-get update

    # Install basic dependencies
    sudo apt-get install python3-pip python3-pyqt5 python3-numpy python3-scipy soapysdr python3-soapysdr

    # Install SoapySDR drivers for your hardware (e.g. RTL-SDR, Airspy, HackRF, LimeSDR, etc.)
    sudo apt-get install soapysdr-module-rtlsdr soapysdr-module-airspy soapysdr-module-hackrf soapysdr-module-lms7

    git clone https://github.com/konung-yaropolk/spectroscope.git
    cd spectroscope
    pip3 install --user .

``spectroscope`` and ``soapy_power`` executables will be then placed in
``~/.local/bin`` directory, you can add it to your PATH in ``~/.bashrc``.



Todo:
-----

- save FFT history (allow big waterfall plot saved to file e.g. bitmap(png, etc) and raw floating-point data(hdf5, etc.))
- automatic peak detection / highlighting
- display average noise level
- frequency markers / bookmarks with notes (even importing and exporting .csv file with
  predefined channels, etc.)
- sellectable collormaps e.g. viridis, plasma, turbo
