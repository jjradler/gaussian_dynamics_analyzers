# Gaussian Ehrenfest Log Parser and Analysis Tools

This is a collection of scripts that I used in July 2017 to parse the logfiles
and generate time-series and waterfall plots for the Ehrenfest dynamics diPt
publication. David has another set (probably sitting in his gscratch account if
you wanted to poke around in there) that might work a bit better.

Admittedly, these are hacky and were just for personal use -- so don't judge me
TOO harshly for their structure. I want to refactor them and put them in a
package with Josh's really lovely Gaussian Realtime Parse program.

-------------------------------------------------------------------------------
Description of Contents:

1.> ``dipole_tseries_gen.sh``:
    Language:  bash
    Function:  Generates a dipole time series for the x, y, and z components
               as well as the total time-evolving electronic dipole moment by
               parsing a Real-Time or Ehrenfest job logfile and formatting the
               output as column vectors with time indices. Garbage should be
               collected automatically.
    Input Args: *.log file entered in CLI
    Output:     Four *.txt files corresponding to each time series.


2.> ``ke_tseries_gen.sh``:
    Language:  bash
    Function:  Generates a time-indexed series of total system kinetic energy
               values for a dynamics simulation in Gaussian.
    Input Args: *.log file entered in CLI
    Output:    ``ke_tseries.txt``


3.> ``geometry_grab.sh``:
    Language:   bash
    Function:   Extracts time and nuclear positions of Pt atoms in an Ehrenfest
                dynamics simulation.


4.> ``distance_calc.py``
    Language:   Python 2
    Function:   Acts as an auxiliary script that works in conjunction with
                ``geometry_grab.sh``.  As a personal note -- I think that if
                anything should be refactored into one script first, it would be
                this one and ``geometry_grab.sh``.


5.> ``ehrenfest_spectra.py``
    Language:   Python 2
    Function:   Generates time-resolved DFT spectrum as an array of time steps
                (across) with the frequency spectra at each step represented as
                column arrays (down). The frequency values are generated as
                ``omega_list_*_*.txt``. This data is formatted with import to
                Excel or IgorPro in mind.

                Note also that this version of the script includes zero-padding
                by default, which will smooth and broaded the spectral traces
                artificially. It will need minor modifications to remove the
                zero padding.
    Input:      The dipole time series. This can be done for any of the four
                outputfiles from ``dipole_tseries_gen.sh``.
    Output:     Two files -- one is the frequencies with respect to time step.
                The other is the frequency bin values as a column array.


6.> ``sum_components_dipole.py``
    Language:   Python
    Function:   Performs an elementwise addition of time-resolved frequency
                spectra. This version adds all three into a ``total`` spectrum,
                but removing or commenting out an argument will make it such
                that you can add only two. I have tried this, and it works
                alright, even though it's hacky and kind of annoying...

--------------------------------------------------------------------------------

I hope you find this helpful. One day I'll fix it so it isn't a kit-bashed
amalgamation of two different languages.

-J.
07/31/18
