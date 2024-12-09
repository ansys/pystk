ProcedureSuperProcedure
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureSuperProcedure

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a super procedure.

.. py:currentmodule:: ProcedureSuperProcedure

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureSuperProcedure.get_as_procedure`
              - Get the procedure interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureSuperProcedure.load_procedures_from_clipboard`
              - Load procedures from the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureSuperProcedure.load_procedures_from_file`
              - Load procedures from a file.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureSuperProcedure



Method detail
-------------

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureSuperProcedure.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

.. py:method:: load_procedures_from_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureSuperProcedure.load_procedures_from_clipboard

    Load procedures from the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: load_procedures_from_file(self, filepath: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureSuperProcedure.load_procedures_from_file

    Load procedures from a file.

    :Parameters:

    **filepath** : :obj:`~str`

    :Returns:

        :obj:`~None`

