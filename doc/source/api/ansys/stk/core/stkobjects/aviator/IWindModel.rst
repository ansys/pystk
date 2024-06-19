IWindModel
==========

.. py:class:: IWindModel

   object
   
   Interface used to access the wind model for a mission, scenario, or procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~copy`
              - Copy the wind model.
            * - :py:meth:`~paste`
              - Paste the wind model.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~wind_model_type`
            * - :py:meth:`~wind_model_type_string`
            * - :py:meth:`~wind_model_source`
            * - :py:meth:`~mode_as_constant`
            * - :py:meth:`~mode_as_adds`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IWindModel


Property detail
---------------

.. py:property:: wind_model_type
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModel.wind_model_type
    :type: WIND_MODEL_TYPE

    Gets or sets the wind model type.

.. py:property:: wind_model_type_string
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModel.wind_model_type_string
    :type: str

    Gets or sets the wind model type as a string value. Use this for custom models.

.. py:property:: wind_model_source
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModel.wind_model_source
    :type: WIND_ATMOS_MODEL_SOURCE

    Gets or sets the wind model source.

.. py:property:: mode_as_constant
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModel.mode_as_constant
    :type: IAgAvtrWindModelConstant

    Get the options for a Constant Bearing/Speed wind model.

.. py:property:: mode_as_adds
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModel.mode_as_adds
    :type: IAgAvtrWindModelADDS

    Get the options for a NOAA ADDS Service wind model.


Method detail
-------------









.. py:method:: copy(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModel.copy

    Copy the wind model.

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModel.paste

    Paste the wind model.

    :Returns:

        :obj:`~None`

