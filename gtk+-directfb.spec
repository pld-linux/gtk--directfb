Summary:	The Gimp Toolkit with DirectFB Support
Summary(pl.UTF-8):	Gimp Toolkit ze wsparciem dla DirectFB
Name:		gtk+-directfb
Version:	1.3.4
Release:	2
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://www.directfb.org/download/GTK+-DirectFB/%{name}-%{version}.tar.gz
# Source0-md5:	37c6e6d9ea32ac57f192413bb46b13a6
#Patch0:	%{name}-info.patch
#Patch1:	%{name}-ahiguti.patch
Patch2:		%{name}-strip.patch
URL:		http://directfb.org/
Requires:	glib >= %{version}
Requires:	iconv
#BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-tools
BuildRequires:	glib-devel >= %{version}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr
%define		_infodir	/usr/share/info
%define		_sysconfdir	%{_datadir}

%description
GTK+ with DirectFB support.

%description -l pl.UTF-8
Biblioteka GTK+ wraz ze wsparciem dla DirectFB

%package devel
Summary:	GTK+-DirectFB header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do GTK+-DirectFB
Group:		Development/Libraries
# Every program using GTK+ should get a list of libraries to link with by
# executing `gtk-config --libs`. All libraries listed below are returned by
# this call, so they are required by every program compiled with GTK+.
#Requires:	XFree86-devel
Requires:	autoconf >= 2.13
Requires:	automake >= 1.4
Requires:	glib-devel >= %{version}
Requires:	%{name} = %{epoch}:%{version}
Requires:	libtool >= 1.3.2

%description devel
Header files and development documentation for the GtK+ libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek GTK+.

%package static
Summary:	GTK+ static libraries
Summary(pl.UTF-8):	Biblioteki statyczne GTK+
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
GTK+ static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne GTK+

%prep
%setup  -q
#%%patch0 -p1
#%%patch1 -p1
%patch -P2 -p0

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-debug=no \
	--enable-shm \
	--with-xinput=directfb

%{__make} m4datadir=%{_aclocaldir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%dir %{_sysconfdir}/gtk
%lang(az) %{_sysconfdir}/gtk/gtkrc.az
%lang(be) %{_sysconfdir}/gtk/gtkrc.be
%lang(bg) %{_sysconfdir}/gtk/gtkrc.bg*
%lang(cs) %{_sysconfdir}/gtk/gtkrc.cs
%lang(cy) %{_sysconfdir}/gtk/gtkrc.cy
%lang(el) %{_sysconfdir}/gtk/gtkrc.el
%lang(eo) %{_sysconfdir}/gtk/gtkrc.eo
%lang(et) %{_sysconfdir}/gtk/gtkrc.et
%lang(ga) %{_sysconfdir}/gtk/gtkrc.ga
%lang(he) %{_sysconfdir}/gtk/gtkrc.he*
%lang(hr) %{_sysconfdir}/gtk/gtkrc.hr
%lang(hu) %{_sysconfdir}/gtk/gtkrc.hu
%lang(hy) %{_sysconfdir}/gtk/gtkrc.hy
%lang(ja) %{_sysconfdir}/gtk/gtkrc.ja
%lang(ka) %{_sysconfdir}/gtk/gtkrc.ka*
%lang(ko) %{_sysconfdir}/gtk/gtkrc.ko
%lang(lt) %{_sysconfdir}/gtk/gtkrc.lt
%lang(lv) %{_sysconfdir}/gtk/gtkrc.lv
%lang(mi) %{_sysconfdir}/gtk/gtkrc.mi
%lang(mk) %{_sysconfdir}/gtk/gtkrc.mk
%lang(pl) %{_sysconfdir}/gtk/gtkrc.pl
%lang(ro) %{_sysconfdir}/gtk/gtkrc.ro
%lang(ru) %{_sysconfdir}/gtk/gtkrc.ru*
%lang(sk) %{_sysconfdir}/gtk/gtkrc.sk
%lang(sr) %{_sysconfdir}/gtk/gtkrc.sp
%lang(sl) %{_sysconfdir}/gtk/gtkrc.sl
%lang(sq) %{_sysconfdir}/gtk/gtkrc.sq
%lang(sr) %{_sysconfdir}/gtk/gtkrc.sr
%lang(th) %{_sysconfdir}/gtk/gtkrc.th
%lang(tr) %{_sysconfdir}/gtk/gtkrc.tr
%lang(uk) %{_sysconfdir}/gtk/gtkrc.uk
%lang(vi) %{_sysconfdir}/gtk/gtkrc.vi*
%lang(yi) %{_sysconfdir}/gtk/gtkrc.yi
%lang(zh) %{_sysconfdir}/gtk/gtkrc.zh*
%lang(be,bg,mk,ru,sr,uk) %{_sysconfdir}/gtk/gtkrc.cp1251
%lang(he,yi) %{_sysconfdir}/gtk/gtkrc.cp1255
%lang(cs,hr,hu,pl,ro,sk,sl,sq,sr) %{_sysconfdir}/gtk/gtkrc.iso-8859-2
%lang(bg,mk,ru,sr,uk) %{_sysconfdir}/gtk/gtkrc.iso-8859-5
%lang(et,lt,lv) %{_sysconfdir}/gtk/gtkrc.iso-8859-13
%lang(br,cy,ga) %{_sysconfdir}/gtk/gtkrc.iso-8859-14
%{_sysconfdir}/gtk/gtkrc.iso-8859-15

%dir %{_libdir}/gtk
%dir %{_libdir}/gtk/themes
%dir %{_libdir}/gtk/themes/engines
%dir %{_sysconfdir}/themes

%{_sysconfdir}/themes/Default

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_bindir}/*
%{_pkgconfigdir}/*
%{_includedir}/*
%{_infodir}/*info*
%{_aclocaldir}/*.m4
%{_mandir}/man1/gtk-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
