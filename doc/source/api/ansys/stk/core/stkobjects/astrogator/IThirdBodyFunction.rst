IThirdBodyFunction
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction

   object
   
   Properties for a Third Body propagator function. The IAgComponentInfo object returned by the mode property can be cast to IAgVAGravityFieldFunction or IAgVAPointMassFunction depending on the selected ModeType.

.. py:currentmodule:: IThirdBodyFunction

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction.set_mode_type`
              - Set the third body gravity mode.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction.third_body_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction.ephem_source`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction.mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction.mode_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction.ephemeris_source_warning`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IThirdBodyFunction


Property detail
---------------

.. py:property:: third_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction.third_body_name
    :type: str

    Gets or sets the selected third body model.

.. py:property:: ephem_source
    :canonical: ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction.ephem_source
    :type: EPHEM_SOURCE

    Source for the third body's ephemeris.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction.mode
    :type: IComponentInfo

    Get the third body gravity mode. The IAgComponentInfo object returned by this property can be cast to IAgVAGravityFieldFunction or IAgVAPointMassFunction depending on the selected ModeType.

.. py:property:: mode_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction.mode_type
    :type: THIRD_BODY_MODE

    Get the third body gravity mode type.

.. py:property:: ephemeris_source_warning
    :canonical: ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction.ephemeris_source_warning
    :type: str

    Returns a warning message if the Ephemeris source and the gravity are not compatible.


Method detail
-------------






.. py:method:: set_mode_type(self, mode: THIRD_BODY_MODE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction.set_mode_type

    Set the third body gravity mode.

    :Parameters:

    **mode** : :obj:`~THIRD_BODY_MODE`

    :Returns:

        :obj:`~None`



