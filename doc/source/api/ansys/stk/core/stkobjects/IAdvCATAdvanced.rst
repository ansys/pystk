IAdvCATAdvanced
===============

.. py:class:: IAdvCATAdvanced

   object
   
   AdvCAT Advanced properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~advanced_ellipsoid`
            * - :py:meth:`~pre_filters`
            * - :py:meth:`~use_log_file`
            * - :py:meth:`~log_file_name`
            * - :py:meth:`~use_correlation_file`
            * - :py:meth:`~correlation_file`
            * - :py:meth:`~use_cross_reference_db`
            * - :py:meth:`~cross_reference_db`
            * - :py:meth:`~use_ssc_hard_body_radius_file`
            * - :py:meth:`~ssc_hard_body_radius_file`
            * - :py:meth:`~show_msg_in_msg_viewer`
            * - :py:meth:`~force_repropagation_on_load`
            * - :py:meth:`~compute_on_load`
            * - :py:meth:`~allow_partial_ephemeris`
            * - :py:meth:`~remove_secondary_by_ssc`
            * - :py:meth:`~max_sample_step_size`
            * - :py:meth:`~min_sample_step_size`
            * - :py:meth:`~conjunction_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAdvCATAdvanced


Property detail
---------------

.. py:property:: advanced_ellipsoid
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.advanced_ellipsoid
    :type: IAgAdvCATAdvEllipsoid

    Get AdvCAT advanced ellipsoid properties.

.. py:property:: pre_filters
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.pre_filters
    :type: IAgAdvCATPreFilters

    Get AdvCAT filter settings.

.. py:property:: use_log_file
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.use_log_file
    :type: bool

    Use the log file.

.. py:property:: log_file_name
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.log_file_name
    :type: str

    Name of the Log File.

.. py:property:: use_correlation_file
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.use_correlation_file
    :type: bool

    Flag to specify Use of Correlation File.

.. py:property:: correlation_file
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.correlation_file
    :type: str

    Correlation File Path.

.. py:property:: use_cross_reference_db
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.use_cross_reference_db
    :type: bool

    Flag to specify Use of Cross Reference Database.

.. py:property:: cross_reference_db
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.cross_reference_db
    :type: str

    Cross Reference Database Path.

.. py:property:: use_ssc_hard_body_radius_file
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.use_ssc_hard_body_radius_file
    :type: bool

    Flag to specify Use of SSC Reference File.

.. py:property:: ssc_hard_body_radius_file
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.ssc_hard_body_radius_file
    :type: str

    SSC Reference File Path.

.. py:property:: show_msg_in_msg_viewer
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.show_msg_in_msg_viewer
    :type: bool

    Flag to specify whether to write messages to message viewer.

.. py:property:: force_repropagation_on_load
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.force_repropagation_on_load
    :type: bool

    Flag to force repropagation on load.

.. py:property:: compute_on_load
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.compute_on_load
    :type: bool

    Flag to force compute on load.

.. py:property:: allow_partial_ephemeris
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.allow_partial_ephemeris
    :type: bool

    Flag to allow computation even when ephemeris does not completely overlap analysis interval.

.. py:property:: remove_secondary_by_ssc
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.remove_secondary_by_ssc
    :type: bool

    Removes from cosniseration any secondary whose SSC number is the same as the primary.

.. py:property:: max_sample_step_size
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.max_sample_step_size
    :type: float

    Maximum step size used in sampling.

.. py:property:: min_sample_step_size
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.min_sample_step_size
    :type: float

    Minimum step size used in sampling.

.. py:property:: conjunction_type
    :canonical: ansys.stk.core.stkobjects.IAdvCATAdvanced.conjunction_type
    :type: ADV_CAT_CONJUNCTION_TYPE

    Mode for computing events involving conjunction TCA.


