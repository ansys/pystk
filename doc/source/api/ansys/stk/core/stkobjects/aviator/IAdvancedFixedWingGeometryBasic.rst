IAdvancedFixedWingGeometryBasic
===============================

.. py:class:: IAdvancedFixedWingGeometryBasic

   object
   
   Interface used to access the options for a basic geometry wing in the advanced fixed wing tool.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_aspect_ratio`
              - Set the aspect ratio of the aircraft.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~aspect_ratio`
            * - :py:meth:`~wing_sweep`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingGeometryBasic


Property detail
---------------

.. py:property:: aspect_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingGeometryBasic.aspect_ratio
    :type: float

    Get the aspect ratio of the aircraft.

.. py:property:: wing_sweep
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingGeometryBasic.wing_sweep
    :type: typing.Any

    Gets or sets the wing sweep of the aircraft.


Method detail
-------------


.. py:method:: set_aspect_ratio(self, aspectRatio:float) -> None

    Set the aspect ratio of the aircraft.

    :Parameters:

    **aspectRatio** : :obj:`~float`

    :Returns:

        :obj:`~None`



