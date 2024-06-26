IMissileExternalAero
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.IMissileExternalAero

   object
   
   Interface used to access the External aerodynamics options for a missile.

.. py:currentmodule:: IMissileExternalAero

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileExternalAero.set_filepath`
              - Set the filepath for the external aero file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileExternalAero.reload`
              - Reload the external aero file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileExternalAero.filepath`
              - Get the filepath for the external aero file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileExternalAero.reference_area`
              - Gets or sets the area of the lifting surface of the missile.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileExternalAero.can_set_reference_area`
              - Check whether you can set the reference area or whether it is specified in the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileExternalAero.is_valid`
              - Check whether the filepath is valid.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IMissileExternalAero


Property detail
---------------

.. py:property:: filepath
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileExternalAero.filepath
    :type: str

    Get the filepath for the external aero file.

.. py:property:: reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileExternalAero.reference_area
    :type: float

    Gets or sets the area of the lifting surface of the missile.

.. py:property:: can_set_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileExternalAero.can_set_reference_area
    :type: bool

    Check whether you can set the reference area or whether it is specified in the file.

.. py:property:: is_valid
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileExternalAero.is_valid
    :type: bool

    Check whether the filepath is valid.


Method detail
-------------


.. py:method:: set_filepath(self, filepath: str) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileExternalAero.set_filepath

    Set the filepath for the external aero file.

    :Parameters:

    **filepath** : :obj:`~str`

    :Returns:

        :obj:`~str`

.. py:method:: reload(self) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileExternalAero.reload

    Reload the external aero file.

    :Returns:

        :obj:`~str`





