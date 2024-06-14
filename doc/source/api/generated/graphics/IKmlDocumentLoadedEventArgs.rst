IKmlDocumentLoadedEventArgs
===========================

.. py:class:: IKmlDocumentLoadedEventArgs

   object
   
   The event is raised when a KML document has been loaded.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~document`
            * - :py:meth:`~exception`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IKmlDocumentLoadedEventArgs


Property detail
---------------

.. py:property:: document
    :canonical: ansys.stk.core.graphics.IKmlDocumentLoadedEventArgs.document
    :type: "IAgStkGraphicsKmlDocument"

    Gets the KML document associated with the load event.

.. py:property:: exception
    :canonical: ansys.stk.core.graphics.IKmlDocumentLoadedEventArgs.exception
    :type: str

    Returns an error message, if an error occurred while loading the KML; otherwise an empty string.


