IAntennaModelItuS731
====================

.. py:class:: IAntennaModelItuS731

   object
   
   Provide access to the properties and methods defining an ITU-R S731 antenna model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~mainlobe_gain`
            * - :py:meth:`~efficiency`
            * - :py:meth:`~diameter`
            * - :py:meth:`~use_mainlobe_model`
            * - :py:meth:`~sidelobe_mask_level`
            * - :py:meth:`~sidelobe_relative_to_mainlobe`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelItuS731


Property detail
---------------

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS731.mainlobe_gain
    :type: float

    Gets or sets the main-lobe gain.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS731.efficiency
    :type: float

    Gets or sets the efficiency.

.. py:property:: diameter
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS731.diameter
    :type: float

    Gets or sets the diameter.

.. py:property:: use_mainlobe_model
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS731.use_mainlobe_model
    :type: bool

    Gets or sets the option for enabling the mainlobe model.

.. py:property:: sidelobe_mask_level
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS731.sidelobe_mask_level
    :type: float

    Gets or sets the sidelobe mask level.

.. py:property:: sidelobe_relative_to_mainlobe
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS731.sidelobe_relative_to_mainlobe
    :type: bool

    Gets or set the flag indicating that the sidelobe mask level is relative to the mainlobe level.


