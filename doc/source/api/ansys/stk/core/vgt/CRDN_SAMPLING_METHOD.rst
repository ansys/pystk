CRDN_SAMPLING_METHOD
====================

.. py:class:: ansys.stk.core.vgt.CRDN_SAMPLING_METHOD

   IntEnum


.. py:currentmodule:: CRDN_SAMPLING_METHOD

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported sampling method.

            * - :py:attr:`~FIXED_STEP`
              - Fixed step sampling method.

            * - :py:attr:`~RELATIVE_TOLERANCE`
              - Relative tolerance method uses a combination of relative and absolute tolerance changes in scalar values between samples.

            * - :py:attr:`~CURVATURE_TOLERANCE`
              - Curvature tolerance also uses changes in slope between samples.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CRDN_SAMPLING_METHOD


