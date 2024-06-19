IAntennaBeam
============

.. py:class:: IAntennaBeam

   object
   
   Provide access to an antenna beam.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~id`
            * - :py:meth:`~active`
            * - :py:meth:`~frequency`
            * - :py:meth:`~supported_antenna_models`
            * - :py:meth:`~antenna_model_name`
            * - :py:meth:`~antenna_model`
            * - :py:meth:`~orientation`
            * - :py:meth:`~enable_polarization`
            * - :py:meth:`~polarization`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaBeam


Property detail
---------------

.. py:property:: id
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.id
    :type: str

    Gets or sets the antenna beam identifier.

.. py:property:: active
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.active
    :type: bool

    Gets or sets the beam active flag.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.frequency
    :type: float

    Gets or sets the beam frequency.

.. py:property:: supported_antenna_models
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.supported_antenna_models
    :type: list

    Gets an array of supported antenna model names.

.. py:property:: antenna_model_name
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.antenna_model_name
    :type: str

    Gets or sets the current antenna model by name.

.. py:property:: antenna_model
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.antenna_model
    :type: IAgAntennaModel

    Gets the current antenna model.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.orientation
    :type: IAgOrientation

    Gets the antenna orientation.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.polarization
    :type: IAgPolarization

    Gets the polarization.


Method detail
-------------















.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`


