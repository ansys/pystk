IVehicleProfileFixedInAxes
==========================

.. py:class:: IVehicleProfileFixedInAxes

   IVehicleAttitudeProfile
   
   Fixed in Axes attitude profile: maintains a constant orientation of the body-fixed axes with respect to the specified reference axes, using the selected coordinate type.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~orientation`
            * - :py:meth:`~reference_axes`
            * - :py:meth:`~available_reference_axes`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleProfileFixedInAxes


Property detail
---------------

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.IVehicleProfileFixedInAxes.orientation
    :type: IAgOrientation

    Get the orientation of the body-fixed axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.stkobjects.IVehicleProfileFixedInAxes.reference_axes
    :type: str

    Reference axes with respect to which the body-fixed axes are oriented. The satellite's body axes or any axes dependent upon the satellite's body axes are invalid for this attitude profile; all other axes are valid choices for the reference axes.

.. py:property:: available_reference_axes
    :canonical: ansys.stk.core.stkobjects.IVehicleProfileFixedInAxes.available_reference_axes
    :type: list

    Returns the available reference axes.


