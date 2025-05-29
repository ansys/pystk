STKEngine
=========

.. py:class:: ansys.stk.core.stkengine.STKEngine

   object

   Initialize and manage the STK Engine application.

.. py:currentmodule:: STKEngine


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkengine.STKEngine.start_application`
              - Initialize STK Engine in-process and return the instance.
                
                Must only be used once per Python process.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkengine import STKEngine


Method detail
-------------

.. py:method:: start_application(no_graphics: bool = True) -> STKEngineApplication
    :canonical: ansys.stk.core.stkengine.STKEngine.start_application

    Initialize STK Engine in-process and return the instance.
    
    Must only be used once per Python process.

    :Parameters:

        **no_graphics** : :obj:`~bool`


    :Returns:

        :obj:`~STKEngineApplication`


