IMCSSequence
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.IMCSSequence

   Properties for a Sequence segment.

.. py:currentmodule:: IMCSSequence

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSequence.apply_script`
              - Apply the script.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSequence.repeat_count`
              - Get or set the number of times that the sequence will be executed. A sequence that is repeated is executed immediately subsequent to the previous execution of the sequence. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSequence.generate_ephemeris`
              - If true, the sequence generates ephemeris and displays it in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSequence.segments`
              - Get the list of segments defined for the sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSequence.sequence_state_to_pass`
              - State To Pass To Next Segment - the state of the sequence to pass.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSequence.scripting_tool`
              - Return the Scripting tool for the sequence.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMCSSequence


Property detail
---------------

.. py:property:: repeat_count
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSequence.repeat_count
    :type: int

    Get or set the number of times that the sequence will be executed. A sequence that is repeated is executed immediately subsequent to the previous execution of the sequence. Dimensionless.

.. py:property:: generate_ephemeris
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSequence.generate_ephemeris
    :type: bool

    If true, the sequence generates ephemeris and displays it in the 2D and 3D Graphics windows.

.. py:property:: segments
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSequence.segments
    :type: MCSSegmentCollection

    Get the list of segments defined for the sequence.

.. py:property:: sequence_state_to_pass
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSequence.sequence_state_to_pass
    :type: SequenceStateToPass

    State To Pass To Next Segment - the state of the sequence to pass.

.. py:property:: scripting_tool
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSequence.scripting_tool
    :type: ScriptingTool

    Return the Scripting tool for the sequence.


Method detail
-------------









.. py:method:: apply_script(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSequence.apply_script

    Apply the script.

    :Returns:

        :obj:`~None`

