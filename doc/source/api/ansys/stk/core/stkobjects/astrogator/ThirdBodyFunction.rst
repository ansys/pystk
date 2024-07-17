ThirdBodyFunction
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   ThirdBody propagator function.

.. py:currentmodule:: ThirdBodyFunction

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction.set_mode_type`
              - Set the third body gravity mode.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction.third_body_name`
              - Gets or sets the selected third body model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction.ephem_source`
              - Source for the third body's ephemeris.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction.mode`
              - Get the third body gravity mode. The IAgComponentInfo object returned by this property can be cast to IAgVAGravityFieldFunction or IAgVAPointMassFunction depending on the selected ModeType.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction.mode_type`
              - Get the third body gravity mode type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction.ephemeris_source_warning`
              - Returns a warning message if the Ephemeris source and the gravity are not compatible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ThirdBodyFunction


Property detail
---------------

.. py:property:: third_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction.third_body_name
    :type: str

    Gets or sets the selected third body model.

.. py:property:: ephem_source
    :canonical: ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction.ephem_source
    :type: EPHEM_SOURCE

    Source for the third body's ephemeris.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction.mode
    :type: IComponentInfo

    Get the third body gravity mode. The IAgComponentInfo object returned by this property can be cast to IAgVAGravityFieldFunction or IAgVAPointMassFunction depending on the selected ModeType.

.. py:property:: mode_type
    :canonical: ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction.mode_type
    :type: THIRD_BODY_MODE

    Get the third body gravity mode type.

.. py:property:: ephemeris_source_warning
    :canonical: ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction.ephemeris_source_warning
    :type: str

    Returns a warning message if the Ephemeris source and the gravity are not compatible.


Method detail
-------------






.. py:method:: set_mode_type(self, mode: THIRD_BODY_MODE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction.set_mode_type

    Set the third body gravity mode.

    :Parameters:

    **mode** : :obj:`~THIRD_BODY_MODE`

    :Returns:

        :obj:`~None`



