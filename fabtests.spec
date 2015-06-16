Summary:	Test suite for libfabric API
Summary(pl.UTF-8):	Zestaw testów dla API libfabric
Name:		fabtests
Version:	1.0.0
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	https://www.openfabrics.org/downloads/ofi/%{name}-%{version}.tar.bz2
# Source0-md5:	7fd1d947b90c36a2e2993497ba65bb51
URL:		https://github.com/ofiwg/fabtests
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.11
BuildRequires:	libfabric-devel >= 1.0.0
BuildRequires:	libtool >= 2:2
Requires:	libfabric >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fabtests provides a set of examples that uses libfabric - a
high-performance fabric software library.

%description -l pl.UTF-8
Fabtests to zbiór przykładów wykorzystujących libfabric - bibliotekę
wysoko wydajnych usług sieci typu fabric.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# don't package plain unit tests
%{__rm} $RPM_BUILD_ROOT%{_bindir}/fi_{av_test,cmatose,cq_data,dgram*,dom_test,eq_test,msg*,poll,rc_pingpong,rdm*,scalable_ep,size_left_test,ud_pingpong}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/runfabtests.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING
%attr(755,root,root) %{_bindir}/fabtest
%attr(755,root,root) %{_bindir}/fi_info
%{_mandir}/man7/fabtests.7*
