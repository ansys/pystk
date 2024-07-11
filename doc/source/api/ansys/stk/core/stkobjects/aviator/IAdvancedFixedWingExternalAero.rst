IAdvancedFixedWingExternalAero
==============================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingExternalAero

   object
   
   Interface used to access the options for an external file aerodynamic strategy in the advanced fixed wing tool.

.. py:currentmodule:: IAdvancedFixedWingExternalAero

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingExternalAero.set_filepath`
              - Set the filepath for the external aero file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingExternalAero.filepath`
              - Get the filepath for the external aero file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingExternalAero.is_valid`
              - Check whether the filepath is valid.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingExternalAero


Property detail
---------------

.. py:property:: filepath
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingExternalAero.filepath
    :type: str

    Get the filepath for the external aero file.

.. py:property:: is_valid
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingExternalAero.is_valid
    :type: bool

    Check whether the filepath is valid.


Method detail
-------------


.. py:method:: set_filepath(self, filepath: str) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingExternalAero.set_filepath

    Set the filepath for the external aero file.

    :Parameters:

    **filepath** : :obj:`~str`

    :Returns:

        :obj:`~str`


