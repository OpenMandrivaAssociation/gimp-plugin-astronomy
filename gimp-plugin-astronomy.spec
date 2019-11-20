%define         moname        %{name}
%define         plugindir     %{_libdir}/gimp/2.0/plug-ins
%define         scriptdir     %{_datadir}/gimp/2.0/scripts

Name:           gimp-plugin-astronomy
Version:        0.9
Release:        1
Summary:        Astronomy plugins for the GIMP graphic editor
License:        GPLv2+
Group:          Graphics/Editors and Converters

URL:            http://hennigbuam.de/georg/gimp.html
Source0:        http://www.hennigbuam.de/georg/downloads/%{name}-%{version}.tar.bz2

BuildRequires:  intltool
BuildRequires:  pkgconfig(gimp-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
Requires:       gimp


%description
Gimp Astronomy is a set of plug-ins for the Gimp graphic editor
intended for astronomical image processing. They support various basic
and more advanced tasks such as aligning and stacking images with
arithmetic, geometric, median, or sigma mean, removing dark frames and
dividing by a flat field. Some plug-gins are designed for creating
synthetic stars distribution or synthetic galaxy images.


%prep
%setup -q
%autopatch -p1

%build
autoreconf -fi
export LIBS="-lm"
%configure \
    CPPFLAGS=-D_XOPEN_SOURCE=700
%make_build


%install
%make_install INSTALLDIR="%{buildroot}/%{plugindir}" \
      LOCALEDIR="%{buildroot}/%{_datadir}/locale"
%find_lang %{moname}


%files -f %{moname}.lang
%doc README AUTHORS
%{scriptdir}/*.scm
%{plugindir}/astronomy-*
%{_docdir}/gimp-plugin-astronomy

