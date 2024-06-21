IAntennaModelApertureRectangularUniform
=======================================

.. py:class:: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform

   object
   
   Provide access to the properties and methods defining a rectangular uniform aperture antenna model.

.. py:currentmodule:: IAntennaModelApertureRectangularUniform

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.compute_mainlobe_gain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.mainlobe_gain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.backlobe_gain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.efficiency`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.use_backlobe_as_mainlobe_atten`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.input_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.x_dimension`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.y_dimension`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.x_beamwidth`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.y_beamwidth`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelApertureRectangularUniform


Property detail
---------------

.. py:property:: compute_mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.compute_mainlobe_gain
    :type: bool

    Gets or sets the option for computing the mainlobe gain.

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.mainlobe_gain
    :type: float

    Gets or sets the mainlobe gain.

.. py:property:: backlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.backlobe_gain
    :type: float

    Gets or sets the backlobe gain.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.efficiency
    :type: float

    Gets or sets the efficiency.

.. py:property:: use_backlobe_as_mainlobe_atten
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.use_backlobe_as_mainlobe_atten
    :type: bool

    Gets or sets the option for using the back lobe gain as a main lobe gain attenuation.

.. py:property:: input_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.input_type
    :type: RECTANGULAR_APERTURE_INPUT_TYPE

    Gets or sets the input type.

.. py:property:: x_dimension
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.x_dimension
    :type: float

    Gets or sets the x dimension.

.. py:property:: y_dimension
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.y_dimension
    :type: float

    Gets or sets the y dimension.

.. py:property:: x_beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.x_beamwidth
    :type: typing.Any

    Gets or sets the x beamwidth.

.. py:property:: y_beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularUniform.y_beamwidth
    :type: typing.Any

    Gets or sets the y beamwidth.


