IProgressTrackCancel
====================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.IProgressTrackCancel

   Control for progress tracker.

.. py:currentmodule:: IProgressTrackCancel

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IProgressTrackCancel.update_progress`
              - Update progress.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IProgressTrackCancel.cancel_requested`
              - Get whether or not cancel was requested.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import IProgressTrackCancel


Property detail
---------------

.. py:property:: cancel_requested
    :canonical: ansys.stk.core.stkrfchannelmodeler.IProgressTrackCancel.cancel_requested
    :type: bool

    Get whether or not cancel was requested.


Method detail
-------------


.. py:method:: update_progress(self, progress: int, message: str) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.IProgressTrackCancel.update_progress

    Update progress.

    :Parameters:

        **progress** : :obj:`~int`

        **message** : :obj:`~str`


    :Returns:

        :obj:`~None`

