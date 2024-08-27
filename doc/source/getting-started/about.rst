About
#####

PySTK is the next generation Python API for Ansys Systems Toolkit (STK). Its
main advantages and features include:

- **Remote API using gRPC**: In addition to traditional OLE communication
  with STK, the STK Python API has optional gRPC communication for
  out-of-process or remote interaction with STK.

- **Better namings:** API objects no longer have prefixes in their
  class names and methods. This improves readability, making your code easy to
  read and to maintain.

- **PyAnsys compliance:** the API integrates with the rest of the `PyAnsys`_,
  allowing users to connect STK with other Ansys products.
