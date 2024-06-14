IAtmosphereModel
================

.. py:class:: IAtmosphereModel

   object
   
   Interface used to access the atmosphere model for a mission, scenario, or procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~copy`
              - Copy the atmosphere model.
            * - :py:meth:`~paste`
              - Paste the atmosphere model.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~atmosphere_model_type_string`
            * - :py:meth:`~atmosphere_model_source`
            * - :py:meth:`~mode_as_basic`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAtmosphereModel


Property detail
---------------

.. py:property:: atmosphere_model_type_string
    :canonical: ansys.stk.core.stkobjects.aviator.IAtmosphereModel.atmosphere_model_type_string
    :type: str

    Gets or sets the atmosphere model type as a string value.

.. py:property:: atmosphere_model_source
    :canonical: ansys.stk.core.stkobjects.aviator.IAtmosphereModel.atmosphere_model_source
    :type: "WIND_ATMOS_MODEL_SOURCE"

    Gets or sets the atmosphere model source.

.. py:property:: mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.IAtmosphereModel.mode_as_basic
    :type: "IAgAvtrAtmosphereModelBasic"

    Get the options for a Basic Atmosphere model.


Method detail
-------------






.. py:method:: copy(self) -> None

    Copy the atmosphere model.

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> None

    Paste the atmosphere model.

    :Returns:

        :obj:`~None`

