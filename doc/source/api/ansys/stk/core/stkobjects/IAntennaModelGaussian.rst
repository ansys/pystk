IAntennaModelGaussian
=====================

.. py:class:: IAntennaModelGaussian

   object
   
   Provide access to the properties and methods defining a gaussian antenna model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~input_type`
            * - :py:meth:`~diameter`
            * - :py:meth:`~beamwidth`
            * - :py:meth:`~mainlobe_gain`
            * - :py:meth:`~backlobe_gain`
            * - :py:meth:`~use_backlobe_as_mainlobe_atten`
            * - :py:meth:`~efficiency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelGaussian


Property detail
---------------

.. py:property:: input_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelGaussian.input_type
    :type: ANTENNA_MODEL_INPUT_TYPE

    Gets or sets the input type.

.. py:property:: diameter
    :canonical: ansys.stk.core.stkobjects.IAntennaModelGaussian.diameter
    :type: float

    Gets or sets the diameter.

.. py:property:: beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelGaussian.beamwidth
    :type: typing.Any

    Gets or sets the beamwidth.

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelGaussian.mainlobe_gain
    :type: float

    Gets or sets the main-lobe gain.

.. py:property:: backlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelGaussian.backlobe_gain
    :type: float

    Gets or sets the back-lobe gain.

.. py:property:: use_backlobe_as_mainlobe_atten
    :canonical: ansys.stk.core.stkobjects.IAntennaModelGaussian.use_backlobe_as_mainlobe_atten
    :type: bool

    Gets or sets the use back-lobe gain as main-lobe attenuation flag.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.IAntennaModelGaussian.efficiency
    :type: float

    Gets or sets the efficiency.


