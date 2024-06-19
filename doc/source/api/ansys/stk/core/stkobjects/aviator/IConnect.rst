IConnect
========

.. py:class:: IConnect

   object
   
   Interface used to send connect commands to Aviator objects.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~execute_command`
              - Send a connect command to an Aviator object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IConnect



Method detail
-------------

.. py:method:: execute_command(self, command: str) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.aviator.IConnect.execute_command

    Send a connect command to an Aviator object.

    :Parameters:

    **command** : :obj:`~str`

    :Returns:

        :obj:`~typing.Any`

