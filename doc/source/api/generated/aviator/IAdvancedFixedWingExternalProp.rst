IAdvancedFixedWingExternalProp
==============================

.. py:class:: IAdvancedFixedWingExternalProp

   object
   
   Interface used to access the options for the External Prop File powerplant strategy in the advanced fixed wing tool.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_filepath`
              - Set the filepath for the external aero file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~filepath`
            * - :py:meth:`~is_valid`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingExternalProp


Property detail
---------------

.. py:property:: filepath
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingExternalProp.filepath
    :type: str

    Get the filepath for the external aero file.

.. py:property:: is_valid
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingExternalProp.is_valid
    :type: bool

    Check whether the filepath is valid.


Method detail
-------------


.. py:method:: set_filepath(self, filepath:str) -> str

    Set the filepath for the external aero file.

    :Parameters:

    **filepath** : :obj:`~str`

    :Returns:

        :obj:`~str`


