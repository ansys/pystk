IElementConfigurationLinear
===========================

.. py:class:: IElementConfigurationLinear

   object
   
   Provide access to the properties and methods defining a linear element configuration.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~num_elements`
            * - :py:meth:`~spacing`
            * - :py:meth:`~tilt_angle`
            * - :py:meth:`~max_look_angle`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IElementConfigurationLinear


Property detail
---------------

.. py:property:: num_elements
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationLinear.num_elements
    :type: int

    Gets or sets the number of elements on the perimiter of the circle.

.. py:property:: spacing
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationLinear.spacing
    :type: float

    Gets or sets the spacing between adjacent elements in wavelengths.

.. py:property:: tilt_angle
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationLinear.tilt_angle
    :type: typing.Any

    Gets or sets the tilt angle.

.. py:property:: max_look_angle
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationLinear.max_look_angle
    :type: typing.Any

    Gets the maximum look angle.


