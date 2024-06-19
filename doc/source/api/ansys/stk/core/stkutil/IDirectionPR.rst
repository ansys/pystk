IDirectionPR
============

.. py:class:: IDirectionPR

   IDirection
   
   Interface for Pitch-Roll (PR) direction sequence.

.. py:currentmodule:: ansys.stk.core.stkutil

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~pitch`
            * - :py:meth:`~roll`
            * - :py:meth:`~sequence`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IDirectionPR


Property detail
---------------

.. py:property:: pitch
    :canonical: ansys.stk.core.stkutil.IDirectionPR.pitch
    :type: typing.Any

    Pitch angle. Uses Angle Dimension.

.. py:property:: roll
    :canonical: ansys.stk.core.stkutil.IDirectionPR.roll
    :type: typing.Any

    Roll angle. Uses Angle Dimension.

.. py:property:: sequence
    :canonical: ansys.stk.core.stkutil.IDirectionPR.sequence
    :type: PR_SEQUENCE

    PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified.


