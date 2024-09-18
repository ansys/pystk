.. title:: PySTK docs

.. meta::
    :description: PySTK provides a Python API to interact with Ansys Systems Tool Kit (STK).
    :keywords: PySTK, STK, AGI, Ansys, Python, API, MBSE, Satellite, Space, Mission, Analysis, Astrodynamics, Orbit, Propagation, Coverage, Access, Conjunction, Maneuver, Sensor, Communication, Ground Station, Facility, Facility, Scenario, Chain, Vector, Point, Area, Grid, Region, Terrain, Vehicle, Aircraft, Ship, Submarine, Missile

.. figure:: _static/logo.png
    :align: center
    :width: 300px 
   
PySTK provides a Python API to interact with `Ansys Systems Tool Kit`_ (STK). STK provides a physics-based modeling environment for analyzing platforms and payloads in a realistic mission context. 

.. grid:: 2

    .. grid-item-card:: Getting started :fa:`person-running`
        :link: getting-started
        :link-type: doc

        Step-by-step guidelines on how to set up your environment to work with
        PySTK. Build your own Docker image for STK, install PySTK, and verify
        your environment.

    .. grid-item-card:: User guide :fa:`book-open-reader`
        :link: user-guide
        :link-type: doc

        Learn about the capabilities, features, and key topics in PySTK. This
        guide provides useful background information and explanations.

.. jinja:: main_toctree

    {% if build_api or build_examples %}
    .. grid:: 2
    
       {% if build_api %}
       .. grid-item-card:: API reference :fa:`book-bookmark`
           :link: api
           :link-type: doc
    
           A detailed guide describing the PySTK API. This guide documents all the
           methods and properties for each interface, class, and
           enumerations of each PySTK module.
        {% endif %}
      
       {% if build_examples %}
       .. grid-item-card:: Gallery of examples :fa:`laptop-code`
           :link: examples
           :link-type: doc
    
           Learn how to use PySTK for creating custom applications and automating
           your existing STK workflows. This guide contains a gallery of examples
           showing how to integrate PySTK with other popular tools in the Python
           ecosystem.
        {% endif %}
    {% endif %}


.. jinja:: main_toctree

    .. toctree::
       :hidden:
       :maxdepth: 3
    
       getting-started
       user-guide
       {% if build_examples %}
       examples
       {% endif %}
       {% if build_api %}
       api
       {% endif %}
       artifacts



**Release version 0.1.dev0**
