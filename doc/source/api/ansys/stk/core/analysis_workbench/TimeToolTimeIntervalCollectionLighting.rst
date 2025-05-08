TimeToolTimeIntervalCollectionLighting
======================================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionLighting

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalCollection`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.

.. py:currentmodule:: TimeToolTimeIntervalCollectionLighting

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionLighting.location`
              - The location point to compute sunlight, penumbra and umbra.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionLighting.eclipsing_bodies`
              - A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionLighting.use_object_eclipsing_bodies`
              - When true, configure eclipsing bodies list based on that of parent STK Object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalCollectionLighting


Property detail
---------------

.. py:property:: location
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionLighting.location
    :type: IVectorGeometryToolPoint

    The location point to compute sunlight, penumbra and umbra.

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionLighting.eclipsing_bodies
    :type: list

    A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.

.. py:property:: use_object_eclipsing_bodies
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionLighting.use_object_eclipsing_bodies
    :type: bool

    When true, configure eclipsing bodies list based on that of parent STK Object.


