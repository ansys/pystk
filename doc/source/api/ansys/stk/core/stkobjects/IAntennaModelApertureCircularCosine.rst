IAntennaModelApertureCircularCosine
===================================

.. py:class:: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine

   object
   
   Provide access to the properties and methods defining a circular cosine aperture antenna model.

.. py:currentmodule:: IAntennaModelApertureCircularCosine

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.compute_mainlobe_gain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.mainlobe_gain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.backlobe_gain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.efficiency`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.use_backlobe_as_mainlobe_atten`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.input_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.diameter`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.beamwidth`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelApertureCircularCosine


Property detail
---------------

.. py:property:: compute_mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.compute_mainlobe_gain
    :type: bool

    Gets or sets the option for computing the mainlobe gain.

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.mainlobe_gain
    :type: float

    Gets or sets the mainlobe gain.

.. py:property:: backlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.backlobe_gain
    :type: float

    Gets or sets the backlobe gain.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.efficiency
    :type: float

    Gets or sets the efficiency.

.. py:property:: use_backlobe_as_mainlobe_atten
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.use_backlobe_as_mainlobe_atten
    :type: bool

    Gets or sets the option for using the back lobe gain as a main lobe gain attenuation.

.. py:property:: input_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.input_type
    :type: CIRCULAR_APERTURE_INPUT_TYPE

    Gets or sets the input type.

.. py:property:: diameter
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.diameter
    :type: float

    Gets or sets the diameter.

.. py:property:: beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosine.beamwidth
    :type: typing.Any

    Gets or sets the beamwidth.


