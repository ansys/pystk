IAntennaBeam
============

.. py:class:: ansys.stk.core.stkobjects.IAntennaBeam

   object
   
   Provide access to an antenna beam.

.. py:currentmodule:: IAntennaBeam

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.id`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.active`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.frequency`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.supported_antenna_models`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.antenna_model_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.antenna_model`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.orientation`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.enable_polarization`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.polarization`


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
    :type: IAntennaModel

    Gets the current antenna model.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.orientation
    :type: IOrientation

    Gets the antenna orientation.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.polarization
    :type: IPolarization

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


