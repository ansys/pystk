IKmlGraphics
============

.. py:class:: IKmlGraphics

   object
   
   Provide loading and unloading of kml documents for a particular central body.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~load_document`
              - Load a kml document from a uri.
            * - :py:meth:`~load_document_string`
              - Load a kml document from a Uri.
            * - :py:meth:`~load`
              - Load a kml document from a string containing the document.
            * - :py:meth:`~load_document_async`
              - Load a kml document asynchronously from a uri. The document loaded event is raised when the document is loaded.
            * - :py:meth:`~load_document_async_string`
              - Load a kml document asynchronously from a Uri. The document loaded event is raised when the document is loaded.
            * - :py:meth:`~load_async`
              - Load a kml document asynchronously from a string containing the document. The document loaded event is raised when the document is loaded.
            * - :py:meth:`~unload`
              - Unloads a kml document. All associated visual features will be removed from the Scene. Once a KmlDocument is unloaded, it is no longer valid and will throw when accessing properties or methods.
            * - :py:meth:`~unload_all`
              - Unloads all kml documents associated with this central body. All associated visual features will be removed from the Scene. Once a KmlDocument is unloaded, it is no longer valid and will throw when accessing properties or methods.
            * - :py:meth:`~Subscribe`
              - """Return an IKmlGraphicsEventHandler that is subscribed to handle events associated with this instance of IKmlGraphics."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~documents`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IKmlGraphics


Property detail
---------------

.. py:property:: documents
    :canonical: ansys.stk.core.graphics.IKmlGraphics.documents
    :type: IAgStkGraphicsKmlDocumentCollection

    The collection of kml documents that are currently loaded.


Method detail
-------------


.. py:method:: load_document(self, kmlUri: str) -> IKmlDocument
    :canonical: ansys.stk.core.graphics.IKmlGraphics.load_document

    Load a kml document from a uri.

    :Parameters:

    **kmlUri** : :obj:`~str`

    :Returns:

        :obj:`~IKmlDocument`

.. py:method:: load_document_string(self, kmlUri: str) -> IKmlDocument
    :canonical: ansys.stk.core.graphics.IKmlGraphics.load_document_string

    Load a kml document from a Uri.

    :Parameters:

    **kmlUri** : :obj:`~str`

    :Returns:

        :obj:`~IKmlDocument`

.. py:method:: load(self, kmlDocument: str) -> IKmlDocument
    :canonical: ansys.stk.core.graphics.IKmlGraphics.load

    Load a kml document from a string containing the document.

    :Parameters:

    **kmlDocument** : :obj:`~str`

    :Returns:

        :obj:`~IKmlDocument`

.. py:method:: load_document_async(self, kmlUri: str) -> None
    :canonical: ansys.stk.core.graphics.IKmlGraphics.load_document_async

    Load a kml document asynchronously from a uri. The document loaded event is raised when the document is loaded.

    :Parameters:

    **kmlUri** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: load_document_async_string(self, kmlUri: str) -> None
    :canonical: ansys.stk.core.graphics.IKmlGraphics.load_document_async_string

    Load a kml document asynchronously from a Uri. The document loaded event is raised when the document is loaded.

    :Parameters:

    **kmlUri** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: load_async(self, kmlDocument: str) -> None
    :canonical: ansys.stk.core.graphics.IKmlGraphics.load_async

    Load a kml document asynchronously from a string containing the document. The document loaded event is raised when the document is loaded.

    :Parameters:

    **kmlDocument** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: unload(self, kmlDocument: IKmlDocument) -> None
    :canonical: ansys.stk.core.graphics.IKmlGraphics.unload

    Unloads a kml document. All associated visual features will be removed from the Scene. Once a KmlDocument is unloaded, it is no longer valid and will throw when accessing properties or methods.

    :Parameters:

    **kmlDocument** : :obj:`~IKmlDocument`

    :Returns:

        :obj:`~None`

.. py:method:: unload_all(self) -> None
    :canonical: ansys.stk.core.graphics.IKmlGraphics.unload_all

    Unloads all kml documents associated with this central body. All associated visual features will be removed from the Scene. Once a KmlDocument is unloaded, it is no longer valid and will throw when accessing properties or methods.

    :Returns:

        :obj:`~None`

