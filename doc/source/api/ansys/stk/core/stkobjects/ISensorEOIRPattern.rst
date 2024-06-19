ISensorEOIRPattern
==================

.. py:class:: ISensorEOIRPattern

   object
   
   IAgSnEOIRPattern Interface for a sensor pattern.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~line_of_site_jitter`
            * - :py:meth:`~processing_level`
            * - :py:meth:`~use_motion_blur`
            * - :py:meth:`~bands`
            * - :py:meth:`~jitter_type`
            * - :py:meth:`~jitter_data_file`
            * - :py:meth:`~jitter_data_file_spatial_sampling`
            * - :py:meth:`~jitter_data_file_frequency_sampling`
            * - :py:meth:`~along_scan_smear_rate`
            * - :py:meth:`~across_scan_smear_rate`
            * - :py:meth:`~scan_mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorEOIRPattern


Property detail
---------------

.. py:property:: line_of_site_jitter
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRPattern.line_of_site_jitter
    :type: float

    The standard deviation of the Gaussian model LineOfSiteJitter for the sensor in angular space for the specified integration time.

.. py:property:: processing_level
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRPattern.processing_level
    :type: SENSOR_EOIR_PROCESSING_LEVELS

    The tap point output ProcessingLevel for the sensor specifying the stage in the imaging pipeline to produce simulated images and output files.

.. py:property:: use_motion_blur
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRPattern.use_motion_blur
    :type: bool

    The status flag for determining if the sensor should apply coarse motion blur to the simulated images or not.

.. py:property:: bands
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRPattern.bands
    :type: IAgSnEOIRBandCollection

    Get the collection of Bands for the sensor.

.. py:property:: jitter_type
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRPattern.jitter_type
    :type: SENSOR_EOIR_JITTER_TYPES

    Type of jitter specification.

.. py:property:: jitter_data_file
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRPattern.jitter_data_file
    :type: str

    Jitter description data file.

.. py:property:: jitter_data_file_spatial_sampling
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRPattern.jitter_data_file_spatial_sampling
    :type: float

    Jitter data file spatial sampling.

.. py:property:: jitter_data_file_frequency_sampling
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRPattern.jitter_data_file_frequency_sampling
    :type: float

    Jitter data file frequency sampling.

.. py:property:: along_scan_smear_rate
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRPattern.along_scan_smear_rate
    :type: float

    Gets or sets the along-scan smear rate of the EOIR sensor.

.. py:property:: across_scan_smear_rate
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRPattern.across_scan_smear_rate
    :type: float

    Gets or sets the across-scan smear rate of the EOIR sensor.

.. py:property:: scan_mode
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRPattern.scan_mode
    :type: SENSOR_EOIR_SCAN_MODES

    Type of scan mode specification.


