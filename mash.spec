%define api	0.2
%define major	0
%define libname	%mklibname %{name} %{api} %{major}
%define girname	%mklibname %{name}-gir %{api}
%define devname	%mklibname -d %{name}

Summary:	A library for using real 3D models within a Clutter scene
Name:		mash
Version:	0.2.0
Release:	8
License:	LGPLv2+
Group:		System/Libraries
Url:		http://wiki.clutter-project.org/wiki/Mash
Source0:	http://source.clutter-project.org/sources/mash/0.2/mash-%{version}.tar.xz

# From Fedora:
# Already sent upstream for review,
# see http://lists.clutter-project.org/pipermail/clutter-devel-list/2011-March/000196.html
Patch0:		0001-Use-the-system-version-of-rply-if-available.patch
BuildRequires:	rply-devel
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(mx-1.0)

%description
Mash is a small library for using real 3D models within a Clutter
scene. Models can be exported from Blender or other 3D modeling
software as PLY files and then used as actors. It also supports a
lighting model with animatable lights.

%package -n %{libname}
Summary:	A library for using real 3D models within a Clutter scene
Group:		System/Libraries

%description -n %{libname}
Mash is a small library for using real 3D models within a Clutter
scene. Models can be exported from Blender or other 3D modeling
software as PLY files and then used as actors. It also supports a
lighting model with animatable lights.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains libraries and header files needed for
development of programs using %{name}.

%prep
%setup -q
%apply_patches
autoreconf -vf

%build
%configure2_5x \
	--disable-static \
	--disable-silent-rules

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Mash-%{api}.typelib

%files -n %{devname}
%doc README NEWS AUTHORS
%doc %{_datadir}/gtk-doc/html/mash
%{_includedir}/%{name}-%{api}
%{_libdir}/lib%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_datadir}/gir-1.0/Mash-%{api}.gir

