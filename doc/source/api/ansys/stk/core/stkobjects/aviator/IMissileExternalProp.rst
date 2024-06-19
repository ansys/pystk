IMissileExternalProp
====================

.. py:class:: IMissileExternalProp

   object
   
   Interface used to access the External Prop file options for a missile.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_filepath`
              - Set the filepath for the external prop file.
            * - :py:meth:`~reload`
              - Reload the external prop file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~filepath`
            * - :py:meth:`~no_thrust_when_no_fuel`
            * - :py:meth:`~is_valid`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IMissileExternalProp


Property detail
---------------

.. py:property:: filepath
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileExternalProp.filepath
    :type: str

    Get the filepath for the external prop file.

.. py:property:: no_thrust_when_no_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileExternalProp.no_thrust_when_no_fuel
    :type: bool

    Opt to have no thrust if the fuel is empty.

.. py:property:: is_valid
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileExternalProp.is_valid
    :type: bool

    Check whether the filepath is valid.


Method detail
-------------


.. py:method:: set_filepath(self, filepath: str) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileExternalProp.set_filepath

    Set the filepath for the external prop file.

    :Parameters:

    **filepath** : :obj:`~str`

    :Returns:

        :obj:`~str`

.. py:method:: reload(self) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileExternalProp.reload

    Reload the external prop file.

    :Returns:

        :obj:`~str`




