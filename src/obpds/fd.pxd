cimport numpy as np

cdef inline double fdm9h(double phi)
cdef inline double fdm7h(double phi)
cdef inline double fdm5h(double phi)
cdef inline double fdm3h(double phi)
cdef inline double fdm1h(double phi)
cdef inline double fd1h(double phi)
cdef inline double fd3h(double phi)
cdef inline double fd5h(double phi)
cdef inline double fd7h(double phi)
cdef inline double fd9h(double phi)
cdef inline double fd11h(double phi)
cdef inline double fd13h(double phi)
cdef inline double fd15h(double phi)
cdef inline double fd17h(double phi)
cdef inline double fd19h(double phi)
cdef inline double fd21h(double phi)
cdef inline double dfd1h(double phi)
cdef inline double gfd1h(double phi, double alpha)
cdef inline double dgfd1h(double phi, double alpha)
cdef void vfd1h(np.ndarray[double] phi, np.ndarray[double] out)
cdef void vdfd1h(np.ndarray[double] phi, np.ndarray[double] out)
cdef void vgfd1h(np.ndarray[double] phi, np.ndarray[double] alpha,
            np.ndarray[double] out)
cdef void vdgfd1h(np.ndarray[double] phi, np.ndarray[double] alpha,
            np.ndarray[double] out)
