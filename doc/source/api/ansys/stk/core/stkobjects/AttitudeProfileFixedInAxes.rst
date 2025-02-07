AttitudeProfileFixedInAxes
==========================

.. py:class:: ansys.stk.core.stkobjects.AttitudeProfileFixedInAxes

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeProfile`

   Fixed in Axes attitude profile: maintains a constant orientation of the body-fixed axes with respect to the specified reference axes, using the selected coordinate type.

.. py:currentmodule:: AttitudeProfileFixedInAxes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeProfileFixedInAxes.orientation`
              - Get the orientation of the body-fixed axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeProfileFixedInAxes.reference_axes`
              - Reference axes with respect to which the body-fixed axes are oriented. The satellite's body axes or any axes dependent upon the satellite's body axes are invalid for this attitude profile; all other axes are valid choices for the reference axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeProfileFixedInAxes.available_reference_axes`
              - Return the available reference axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AttitudeProfileFixedInAxes


Property detail
---------------

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.AttitudeProfileFixedInAxes.orientation
    :type: IOrientation

    Get the orientation of the body-fixed axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.stkobjects.AttitudeProfileFixedInAxes.reference_axes
    :type: str

    Reference axes with respect to which the body-fixed axes are oriented. The satellite's body axes or any axes dependent upon the satellite's body axes are invalid for this attitude profile; all other axes are valid choices for the reference axes.

.. py:property:: available_reference_axes
    :canonical: ansys.stk.core.stkobjects.AttitudeProfileFixedInAxes.available_reference_axes
    :type: list

    Return the available reference axes.


