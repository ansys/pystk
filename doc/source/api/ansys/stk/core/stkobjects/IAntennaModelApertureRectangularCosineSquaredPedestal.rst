IAntennaModelApertureRectangularCosineSquaredPedestal
=====================================================

.. py:class:: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal

   object
   
   Provide access to the properties and methods defining a rectangular cosine squared pedestal aperture antenna model.

.. py:currentmodule:: IAntennaModelApertureRectangularCosineSquaredPedestal

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.compute_mainlobe_gain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.mainlobe_gain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.backlobe_gain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.efficiency`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.use_backlobe_as_mainlobe_atten`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.input_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.x_dimension`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.y_dimension`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.x_beamwidth`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.y_beamwidth`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.pedestal_level`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelApertureRectangularCosineSquaredPedestal


Property detail
---------------

.. py:property:: compute_mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.compute_mainlobe_gain
    :type: bool

    Gets or sets the option for computing the mainlobe gain.

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.mainlobe_gain
    :type: float

    Gets or sets the mainlobe gain.

.. py:property:: backlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.backlobe_gain
    :type: float

    Gets or sets the backlobe gain.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.efficiency
    :type: float

    Gets or sets the efficiency.

.. py:property:: use_backlobe_as_mainlobe_atten
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.use_backlobe_as_mainlobe_atten
    :type: bool

    Gets or sets the option for using the back lobe gain as a main lobe gain attenuation.

.. py:property:: input_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.input_type
    :type: RECTANGULAR_APERTURE_INPUT_TYPE

    Gets or sets the input type.

.. py:property:: x_dimension
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.x_dimension
    :type: float

    Gets or sets the x dimension.

.. py:property:: y_dimension
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.y_dimension
    :type: float

    Gets or sets the y dimension.

.. py:property:: x_beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.x_beamwidth
    :type: typing.Any

    Gets or sets the x beamwidth.

.. py:property:: y_beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.y_beamwidth
    :type: typing.Any

    Gets or sets the y beamwidth.

.. py:property:: pedestal_level
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosineSquaredPedestal.pedestal_level
    :type: float

    Gets or sets the pedestal level.


