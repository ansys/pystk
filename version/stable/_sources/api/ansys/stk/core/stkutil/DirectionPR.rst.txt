DirectionPR
===========

.. py:class:: ansys.stk.core.stkutil.DirectionPR

   Bases: :py:class:`~ansys.stk.core.stkutil.IDirection`

   Pitch-Roll (PR) direction sequence.

.. py:currentmodule:: DirectionPR

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.DirectionPR.pitch`
              - Pitch angle. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.DirectionPR.roll`
              - Roll angle. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.DirectionPR.sequence`
              - PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import DirectionPR


Property detail
---------------

.. py:property:: pitch
    :canonical: ansys.stk.core.stkutil.DirectionPR.pitch
    :type: typing.Any

    Pitch angle. Uses Angle Dimension.

.. py:property:: roll
    :canonical: ansys.stk.core.stkutil.DirectionPR.roll
    :type: typing.Any

    Roll angle. Uses Angle Dimension.

.. py:property:: sequence
    :canonical: ansys.stk.core.stkutil.DirectionPR.sequence
    :type: PRSequence

    PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified.


