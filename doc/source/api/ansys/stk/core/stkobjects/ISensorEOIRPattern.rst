ISensorEOIRPattern
==================

.. py:class:: ansys.stk.core.stkobjects.ISensorEOIRPattern

   object
   
   IAgSnEOIRPattern Interface for a sensor pattern.

.. py:currentmodule:: ISensorEOIRPattern

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRPattern.line_of_site_jitter`
              - The standard deviation of the Gaussian model LineOfSiteJitter for the sensor in angular space for the specified integration time.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRPattern.processing_level`
              - The tap point output ProcessingLevel for the sensor specifying the stage in the imaging pipeline to produce simulated images and output files.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRPattern.use_motion_blur`
              - The status flag for determining if the sensor should apply coarse motion blur to the simulated images or not.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRPattern.bands`
              - Get the collection of Bands for the sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRPattern.jitter_type`
              - Type of jitter specification.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRPattern.jitter_data_file`
              - Jitter description data file.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRPattern.jitter_data_file_spatial_sampling`
              - Jitter data file spatial sampling.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRPattern.jitter_data_file_frequency_sampling`
              - Jitter data file frequency sampling.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRPattern.along_scan_smear_rate`
              - Gets or sets the along-scan smear rate of the EOIR sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRPattern.across_scan_smear_rate`
              - Gets or sets the across-scan smear rate of the EOIR sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRPattern.scan_mode`
              - Type of scan mode specification.


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
    :type: ISensorEOIRBandCollection

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


