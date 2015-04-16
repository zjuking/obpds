#
#   Copyright (c) 2015, Scott J Maddox
#
#   This file is part of Open Band Parameters Device Simulator (OBPDS).
#
#   OBPDS is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   OBPDS is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with OBPDS.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from numpy import exp, log


__all__ = ['fermi_p', 'fermi_n', 'inv_fermi_p', 'inv_fermi_n']


def fermi_p(psi, Vp, phi_p, nieffref, Vt):
    return nieffref*exp((-psi+Vp+phi_p)/Vt)

def fermi_n(psi, Vn, phi_n, nieffref, Vt):
    return nieffref*exp((psi+Vn-phi_n)/Vt)

def inv_fermi_p(psi, Vp, p, nieffref, Vt):
    return psi - Vp + log(p / nieffref)*Vt

def inv_fermi_n(psi, Vn, n, nieffref, Vt):
    return psi + Vn - log(n / nieffref)*Vt