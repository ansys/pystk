IStkRfcmProgressTrackCancel
===========================

.. py:class:: ansys.stk.core.rfcm.IStkRfcmProgressTrackCancel

   Control for progress tracker.

.. py:currentmodule:: IStkRfcmProgressTrackCancel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmProgressTrackCancel.update_progress`
              - Update progress.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmProgressTrackCancel.cancel_requested`
              - Gets whether or not cancel was requested.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.rfcm import IStkRfcmProgressTrackCancel


Property detail
---------------

.. py:property:: cancel_requested
    :canonical: ansys.stk.core.rfcm.IStkRfcmProgressTrackCancel.cancel_requested
    :type: bool

    Gets whether or not cancel was requested.


Method detail
-------------


.. py:method:: update_progress(self, progress: int, message: str) -> None
    :canonical: ansys.stk.core.rfcm.IStkRfcmProgressTrackCancel.update_progress

    Update progress.

    :Parameters:

    **progress** : :obj:`~int`
    **message** : :obj:`~str`

    :Returns:

        :obj:`~None`

