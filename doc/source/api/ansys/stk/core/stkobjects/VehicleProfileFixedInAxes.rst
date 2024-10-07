VehicleProfileFixedInAxes
=========================

.. py:class:: ansys.stk.core.stkobjects.VehicleProfileFixedInAxes

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeProfile`

   Fixed in Axes attitude profile: maintains a constant orientation of the body-fixed axes with respect to the specified reference axes, using the selected coordinate type.

.. py:currentmodule:: VehicleProfileFixedInAxes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleProfileFixedInAxes.orientation`
              - Get the orientation of the body-fixed axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleProfileFixedInAxes.reference_axes`
              - Reference axes with respect to which the body-fixed axes are oriented. The satellite's body axes or any axes dependent upon the satellite's body axes are invalid for this attitude profile; all other axes are valid choices for the reference axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleProfileFixedInAxes.available_reference_axes`
              - Returns the available reference axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleProfileFixedInAxes


Property detail
---------------

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.VehicleProfileFixedInAxes.orientation
    :type: IOrientation

    Get the orientation of the body-fixed axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.stkobjects.VehicleProfileFixedInAxes.reference_axes
    :type: str

    Reference axes with respect to which the body-fixed axes are oriented. The satellite's body axes or any axes dependent upon the satellite's body axes are invalid for this attitude profile; all other axes are valid choices for the reference axes.

.. py:property:: available_reference_axes
    :canonical: ansys.stk.core.stkobjects.VehicleProfileFixedInAxes.available_reference_axes
    :type: list

    Returns the available reference axes.


