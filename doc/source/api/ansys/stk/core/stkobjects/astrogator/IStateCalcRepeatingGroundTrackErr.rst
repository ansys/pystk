IStateCalcRepeatingGroundTrackErr
=================================

.. py:class:: IStateCalcRepeatingGroundTrackErr

   object
   
   Properties for a RepeatingGroundTrackEquatorError calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:meth:`~disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:meth:`~is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_name`
            * - :py:meth:`~reference_longitude`
            * - :py:meth:`~repeat_count`
            * - :py:meth:`~control_parameters_available`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcRepeatingGroundTrackErr


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRepeatingGroundTrackErr.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: reference_longitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRepeatingGroundTrackErr.reference_longitude
    :type: typing.Any

    Gets or sets the longitude at the equator to be used as a reference for the repeating ground track. Uses Angle Dimension.

.. py:property:: repeat_count
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRepeatingGroundTrackErr.repeat_count
    :type: float

    Gets or sets the number of orbits before the ground track repeats over the same longitude. Dimensionless.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRepeatingGroundTrackErr.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------







.. py:method:: enable_control_parameter(self, param:"CONTROL_REPEATING_GROUND_TRACK_ERR") -> None

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_REPEATING_GROUND_TRACK_ERR"`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param:"CONTROL_REPEATING_GROUND_TRACK_ERR") -> None

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_REPEATING_GROUND_TRACK_ERR"`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param:"CONTROL_REPEATING_GROUND_TRACK_ERR") -> bool

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~"CONTROL_REPEATING_GROUND_TRACK_ERR"`

    :Returns:

        :obj:`~bool`


