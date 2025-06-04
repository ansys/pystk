MissileExternalPropulsion
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.MissileExternalPropulsion

   Class defining the External propulsion options for a missile.

.. py:currentmodule:: MissileExternalPropulsion

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileExternalPropulsion.set_filepath`
              - Set the filepath for the external prop file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileExternalPropulsion.reload`
              - Reload the external prop file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileExternalPropulsion.filepath`
              - Get the filepath for the external prop file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileExternalPropulsion.no_thrust_when_no_fuel`
              - Opt to have no thrust if the fuel is empty.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileExternalPropulsion.is_valid`
              - Check whether the filepath is valid.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import MissileExternalPropulsion


Property detail
---------------

.. py:property:: filepath
    :canonical: ansys.stk.core.stkobjects.aviator.MissileExternalPropulsion.filepath
    :type: str

    Get the filepath for the external prop file.

.. py:property:: no_thrust_when_no_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.MissileExternalPropulsion.no_thrust_when_no_fuel
    :type: bool

    Opt to have no thrust if the fuel is empty.

.. py:property:: is_valid
    :canonical: ansys.stk.core.stkobjects.aviator.MissileExternalPropulsion.is_valid
    :type: bool

    Check whether the filepath is valid.


Method detail
-------------


.. py:method:: set_filepath(self, filepath: str) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.MissileExternalPropulsion.set_filepath

    Set the filepath for the external prop file.

    :Parameters:

        **filepath** : :obj:`~str`


    :Returns:

        :obj:`~str`

.. py:method:: reload(self) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.MissileExternalPropulsion.reload

    Reload the external prop file.

    :Returns:

        :obj:`~str`




