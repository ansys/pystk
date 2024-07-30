AdvCATAdvanced
==============

.. py:class:: ansys.stk.core.stkobjects.AdvCATAdvanced

   Bases: 

   AdvCAT advanced properties.

.. py:currentmodule:: AdvCATAdvanced

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.advanced_ellipsoid`
              - Get AdvCAT advanced ellipsoid properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.pre_filters`
              - Get AdvCAT filter settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.use_log_file`
              - Use the log file.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.log_file_name`
              - Name of the Log File.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.use_correlation_file`
              - Flag to specify Use of Correlation File.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.correlation_file`
              - Correlation File Path.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.use_cross_reference_db`
              - Flag to specify Use of Cross Reference Database.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.cross_reference_db`
              - Cross Reference Database Path.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.use_ssc_hard_body_radius_file`
              - Flag to specify Use of SSC Reference File.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.ssc_hard_body_radius_file`
              - SSC Reference File Path.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.show_message_in_message_viewer`
              - Flag to specify whether to write messages to message viewer.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.force_repropagation_on_load`
              - Flag to force repropagation on load.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.compute_on_load`
              - Flag to force compute on load.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.allow_partial_ephemeris`
              - Flag to allow computation even when ephemeris does not completely overlap analysis interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.remove_secondary_by_ssc`
              - Removes from cosniseration any secondary whose SSC number is the same as the primary.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.max_sample_step_size`
              - Maximum step size used in sampling.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.min_sample_step_size`
              - Minimum step size used in sampling.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAdvanced.conjunction_type`
              - Mode for computing events involving conjunction TCA.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AdvCATAdvanced


Property detail
---------------

.. py:property:: advanced_ellipsoid
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.advanced_ellipsoid
    :type: IAdvCATAdvancedEllipsoid

    Get AdvCAT advanced ellipsoid properties.

.. py:property:: pre_filters
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.pre_filters
    :type: IAdvCATPreFilters

    Get AdvCAT filter settings.

.. py:property:: use_log_file
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.use_log_file
    :type: bool

    Use the log file.

.. py:property:: log_file_name
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.log_file_name
    :type: str

    Name of the Log File.

.. py:property:: use_correlation_file
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.use_correlation_file
    :type: bool

    Flag to specify Use of Correlation File.

.. py:property:: correlation_file
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.correlation_file
    :type: str

    Correlation File Path.

.. py:property:: use_cross_reference_db
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.use_cross_reference_db
    :type: bool

    Flag to specify Use of Cross Reference Database.

.. py:property:: cross_reference_db
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.cross_reference_db
    :type: str

    Cross Reference Database Path.

.. py:property:: use_ssc_hard_body_radius_file
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.use_ssc_hard_body_radius_file
    :type: bool

    Flag to specify Use of SSC Reference File.

.. py:property:: ssc_hard_body_radius_file
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.ssc_hard_body_radius_file
    :type: str

    SSC Reference File Path.

.. py:property:: show_message_in_message_viewer
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.show_message_in_message_viewer
    :type: bool

    Flag to specify whether to write messages to message viewer.

.. py:property:: force_repropagation_on_load
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.force_repropagation_on_load
    :type: bool

    Flag to force repropagation on load.

.. py:property:: compute_on_load
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.compute_on_load
    :type: bool

    Flag to force compute on load.

.. py:property:: allow_partial_ephemeris
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.allow_partial_ephemeris
    :type: bool

    Flag to allow computation even when ephemeris does not completely overlap analysis interval.

.. py:property:: remove_secondary_by_ssc
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.remove_secondary_by_ssc
    :type: bool

    Removes from cosniseration any secondary whose SSC number is the same as the primary.

.. py:property:: max_sample_step_size
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.max_sample_step_size
    :type: float

    Maximum step size used in sampling.

.. py:property:: min_sample_step_size
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.min_sample_step_size
    :type: float

    Minimum step size used in sampling.

.. py:property:: conjunction_type
    :canonical: ansys.stk.core.stkobjects.AdvCATAdvanced.conjunction_type
    :type: ADV_CAT_CONJUNCTION_TYPE

    Mode for computing events involving conjunction TCA.


